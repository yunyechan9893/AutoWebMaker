from flask import Flask
from config.config import DevelopmentConfig as conf


def create_app():
    app = Flask(__name__)
    init_env( app )
    init_blueprint( app )

    return app

def init_env( app ):
    app.config['OPEN_API_KEY'] = conf.OPENAI_API_SECRET_KEY

def init_blueprint( app ):
    from controller import api

    app.register_blueprint(api)

if __name__=='__main__':
    if conf.DEBUG :
        app = create_app()
        app.run(host='0.0.0.0', debug=True)
