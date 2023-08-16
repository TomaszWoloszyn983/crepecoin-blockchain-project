from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my_secret_key'
    print('website/init runs')

    return app

