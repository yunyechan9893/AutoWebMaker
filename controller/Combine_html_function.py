from flask import request, jsonify
from controller import api
from model import gpt
from model.gpt.params import Params
from model.gpt.prompt import System, User


@api.route('/html_function', methods=['POST'])
def create_html_function():
    system_prompt = System('hi').join_architecture_function()
    
    user = User.join_architecture_function()
    msg = gpt.create_message(system_prompt)
    print("file_flow_chart===============")
    print(msg)
    print("file_flow_chart===============")
    gpt.put_query_message(msg, user)

    gpt_params = Params(
        temperature=1, 
        max_tokens=14000, 
        top_p=1.0, 
        best_of=1, 
        frequency_penalty=1, 
        presence_penalty=0.0
    ) 

    
    print(msg)
    answer = gpt.get_gpt_answer(gpt.model, gpt_params, msg)
    print(answer)
    
    return answer
