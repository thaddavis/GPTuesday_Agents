from http.client import HTTPException
import json
from flask import Flask
from flask_cors import CORS
from routes.call_conversational_rag_agent_2 import (
    call_conversational_rag_agent_2_blueprint,
)
from routes.call_plan_and_execute_agent import (
    call_plan_and_execute_agent_blueprint,
)

from routes.test_streaming import test_streaming_blueprint
from routes.verify_password import verify_password_blueprint
from routes.test import test_blueprint

app = Flask(__name__)
app.register_blueprint(verify_password_blueprint)  # BASIC AUTH
app.register_blueprint(test_blueprint)  # LEVEL 0
# app.register_blueprint(call_conversational_agent_blueprint)  # LEVEL 1
# app.register_blueprint(call_hwchase17_conversational_agent_blueprint)  # LEVEL 2
# app.register_blueprint(call_code_interpreter_blueprint)  # LEVEL 3
# app.register_blueprint(call_conversational_rag_agent_blueprint)  # LEVEL 4
app.register_blueprint(test_streaming_blueprint)  # LEVEL 5
app.register_blueprint(call_conversational_rag_agent_2_blueprint)  # LEVEL 6
# app.register_blueprint(call_plan_and_execute_agent_blueprint)  # LEVEL 7

CORS(app)


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    print(e)
    response.content_type = "application/json"
    return response
