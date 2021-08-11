from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route("/hello")
def user_service_hello():
    return make_response(jsonify(
        {
            "msg": "Hello from User Service!"
        }
    ), 200)
