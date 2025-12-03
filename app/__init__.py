from flask import Flask
print("INIT FILE RAN")

def create_app():
    print("CREATE_APP CALLED")
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    return app