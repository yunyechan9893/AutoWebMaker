from flask import Blueprint

api = Blueprint('api',  # 별칭, 해당 블루프린트 밑에서 정의된 
                    __name__,   # 고정
                    url_prefix='/api',             # 모든 URL 앞에 /main이 추가된다
    )

from controller import file_architecture
from controller import file_flow_chart
from controller import Combine_html_function
