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
                        "name": "거래소",
                        "sub_file": [],
                        "sub_folder": [
                        {
                            "name": "app",
                            "sub_file": [
                            "routes.py",
                            "models.py",
                            "controllers.py"
                            ],
                            "sub_folder": [
                            {
                                "name": "static",
                                "sub_file": [],
                                "sub_folder": [
                                {
                                    "name": "css",
                                    "sub_file": [
                                    "style.css",
                                    "main.css"
                                    ],
                                    "sub_folder": []
                                },
                                {
                                    "name": "js",
                                    "sub_file": [
                                    "script.js",
                                    "main.js"
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
                            "index.html",
                            "login.html",
                            "register.html"
                            ],
                            "sub_folder": []
                        }
                        ]
                    }
                    ]
                },
                "project_name": "거래"
            })

    system_prompt = System('hi').get_file_flow_chart(architecture)
    
    user = User.get_file_flow_chart()
    msg = gpt.create_message(system_prompt)

    gpt.put_query_message(msg, user)

    gpt_params = Params(
        temperature=0.8, 
        max_tokens=3000, 
        top_p=1.0, 
        best_of=1, 
        frequency_penalty=0.7, 
        presence_penalty=0.0
    ) 

    
    print(msg)
    answer = gpt.get_gpt_answer(gpt.model, gpt_params, msg)
    print(answer)
    
    return answer
