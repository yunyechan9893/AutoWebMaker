from flask import request, jsonify
from controller import api
from model import gpt
from model.gpt.params import Params
from model.gpt.prompt import System, User


@api.route('/file_flow_chart', methods=['POST'])
def create_file_flow_chart():
    # file_chart_json = request.get_json()
    # file_chart = file_chart_json.get('flow_chart', "")
    # flie_chart = file_chart.replace("-", "\t")
    # print(flie_chart)

    # system = request.get_json()
    # system_prompt, formatted_functions = System(system).get_architecture_prompt()

    architecture = jsonify({
        "file_architecture": {
            "folder": [
            {
                "name": "가계",
                "sub_file": [
                "config.py",
                "run.py"
                ],
                "sub_folder": [
                {
                    "name": "app",
                    "sub_file": [
                    "main.py",
                    "models.py",
                    "views.py",
                    "forms.py"
                    ],
                    "sub_folder": [
                    {
                        "name": "static",
                        "sub_file": [],
                        "sub_folder": [
                        {
                            "name": "css",
                            "sub_file": [
                            "style.css"
                            ],
                            "sub_folder": [
                            {
                                "name": "img",
                                "sub_file": [
                                "logo.png"
                                ],
                                "sub_folder": []
                            }
                            ]
                        },
                        {
                            "name": "js",
                            "sub_file": [
                            "script.js"
                            ],
                            "sub_folder": []
                        }
                        ]
                    }
                    ]
                },
                {
                    "name": "templates",
                    "sub_file": [
                    "base.html",
                    "home.html",
                    "login.html"
                    ],
                    "sub_folder": []
                }
                ]
            }
            ]
        },
        "project_name": "가계"
        })

    system_prompt = System('hi').get_file_flow_chart(architecture)
    
    user = User.get_file_flow_chart()
    msg = gpt.create_message(system_prompt)
    print("file_flow_chart===============")
    print(msg)
    print("file_flow_chart===============")
    gpt.put_query_message(msg, user)

    gpt_params = Params(
        temperature=0.8, 
        max_tokens=8000, 
        top_p=1.0, 
        best_of=1, 
        frequency_penalty=0.7, 
        presence_penalty=0.0
    ) 

    
    print(msg)
    answer = gpt.get_gpt_answer(gpt.model, gpt_params, msg)
    print(answer)
    
    return answer
