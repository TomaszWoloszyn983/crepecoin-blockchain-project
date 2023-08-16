from flask import Flask

def get_chain():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my_secret_key'
    print('blockchain/init runs')

    return app