from flask import Flask
from routes.email_routes import email_bp
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "dev-secret-key")

    app.register_blueprint(email_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug = True)