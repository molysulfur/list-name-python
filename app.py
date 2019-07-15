import os
from flask import Flask , render_template
from src.database import DB
from src.routes import route

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'src/templates')

app = Flask(__name__,template_folder=template_path)

DB.init()

app.register_blueprint(route.get_blueprint())

if __name__ == "__main__":
    app.run(debug="true")