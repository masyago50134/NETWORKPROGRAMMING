from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)


USERS = {
    "admin": "1234",
}


ITEMS = {
    1: {"name": "T-shirt", "price": 20, "color": "red"},
    2: {"name": "Jeans", "price": 50, "color": "blue"},
}


def check_auth(username, password):
    return USERS.get(username) == password


def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper





@app.route("/items", methods=["GET", "POST"])
@requires_auth
def items():
    if request.method == "GET":
        return jsonify(ITEMS)

    if request.method == "POST":
        data = request.json
        new_id = max(ITEMS.keys(), default=0) + 1
        ITEMS[new_id] = data
        return jsonify({"id": new_id, "item": data}), 201



@app.route("/items/<int:item_id>", methods=["GET", "PUT", "DELETE"])
@requires_auth
def item_by_id(item_id):
    if item_id not in ITEMS:
        return jsonify({"error": "Item not found"}), 404

    if request.method == "GET":
        return jsonify(ITEMS[item_id])

    if request.method == "PUT":
        ITEMS[item_id] = request.json
        return jsonify({"id": item_id, "item": ITEMS[item_id]})

    if request.method == "DELETE":
        del ITEMS[item_id]
        return jsonify({"message": "Item deleted"})


if __name__ == "__main__":
    app.run(port=8000)
