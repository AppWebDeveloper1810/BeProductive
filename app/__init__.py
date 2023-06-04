from flask import Flask

app = Flask(__name__)

# Import and register blueprints/routes
from app.routes import main_blueprint
app.register_blueprint(main_blueprint)
