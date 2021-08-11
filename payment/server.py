from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route("/hello")
def payment_service_hello():
    return make_response(jsonify(
        {
            "msg": "Hello from Payment Service!"
        }
    ), 200)
