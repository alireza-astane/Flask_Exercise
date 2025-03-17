from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/greet", methods=["GET"])
def greet():
    print(request.args)
    name = request.args.get("name", "Guest")
    return jsonify({"message": f"Hello, {name}!"})


if __name__ == "__main__":
    app.run(debug=True)
