

from flask import Flask, render_template, jsonify, request
from agent import run_conversation

app = Flask(__name__)

@app.route("/process_message", methods=["post"])
def process_message_func1():
    msg=request.json['message']
    print("we are getting",msg)
    resp = run_conversation(msg)
    return jsonify({"response": resp})



@app.route("/")
def index():
    template_path = app.jinja_env.loader.get_source(app, "index.html")
    print(f"Trying to load template from: {template_path}")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
   # template_path = app.jinja_env.loader.get_source(app, "index.html")
    #print(f"Trying to load template from: {template_path}")