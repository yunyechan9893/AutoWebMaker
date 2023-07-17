from flask import request, jsonify
from controller import api
from model import gpt
from model.gpt.params import Params
from model.gpt.prompt import System, User



@api.route('/file_architecture', methods=['POST'])
def create_file_architecture():
    system = request.get_json()
    system_prompt, formatted_functions = System(system).get_architecture_prompt()
    
    user = User.get_architecture_prompt()
    msg = gpt.create_message(system_prompt)

    gpt.put_query_message(msg, user)

    gpt_params = Params(
        temperature=1.0, 
        max_tokens=3000, 
        top_p=1.0, 
        best_of=1, 
        frequency_penalty=1.0, 
        presence_penalty=0.0
    ) 

    answer = gpt.get_gpt_answer(gpt.model, gpt_params, msg)

    structure = parse_structure(answer)
    project_name = structure['name']
    structure_json = get_file_architecture_json(project_name, structure)
    
    print(formatted_functions)
    return structure_json


def line_to_dict(line):
    indent = line.count('-')
    name = line.replace('-', '').strip().replace('/', '')
    return indent, {"name": name, "sub_file": [], "sub_folder": []}

def add_to_structure(structure, element, indent):
    if not structure:
        structure.append((indent, element))
    elif indent > structure[-1][0]:
        structure[-1][1]["sub_folder"].append(element)
        structure.append((indent, element))
    elif indent == structure[-1][0]:
        structure[-2][1]["sub_folder"].append(element)
        structure.append((indent, element))
    else:
        while indent <= structure[-1][0]:
            structure.pop()
        structure[-1][1]["sub_folder"].append(element)
        structure.append((indent, element))

def parse_structure(structure_str):
    lines = [line for line in structure_str.split('\n') if line.strip() and line.strip().startswith('-')]
    structure = []
    for line in lines:
        # '#' 기호로 시작하는 주석을 제거합니다.
        if '#' in line:
            line = line[:line.index('#')]
        if "/" in line:
            indent, element = line_to_dict(line)
            add_to_structure(structure, element, indent)
        else:
            indent, name = line.count('-'), line.replace('-', '').strip()
            if structure and indent > structure[-1][0]:
                structure[-1][1]["sub_file"].append(name)
            elif structure and indent == structure[-1][0]:
                structure[-2][1]["sub_file"].append(name)
    return structure[0][1]

def get_file_architecture_json(project_name, structure):
    data = {
        "project_name": project_name,
        "file_architecture": {
            "folder": [structure]
        }
    }
    
    return jsonify(data)
