from flask import Flask
from task_orchestrator.router import routes

import json


app = Flask(__name__)
routes(app)
