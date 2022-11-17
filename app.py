from flask import Flask, request, jsonify
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        with counter.get_lock():
            counter.value += 1
            out = counter.value
        return ('', 204)
    else:
        out = counter.value
        return jsonify(count=out)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
