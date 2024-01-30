from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

user = "tad@cmdlabs.io"
pw = "1234xyz"
users = {user: generate_password_hash(pw)}

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username) or "", password)
    return False
