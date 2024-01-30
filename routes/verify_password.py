from flask import Blueprint
from basic_auth.index import auth

verify_password_blueprint = Blueprint("verify_password_blueprint", __name__)


@verify_password_blueprint.route("/verify_password", methods=["POST"])
@auth.login_required
def login():
    return "Hello, World!"
