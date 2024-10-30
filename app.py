from flask import Flask, render_template, request, jsonify
from text_process.text_generator import TextGenerator
import json
import logging
logging.basicConfig(
    filename="model_log.log",
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

with open("data.json", 'r') as file:
    data = json.load(file)

app = Flask(__name__)

MODEL = None
API_KEY = None
TASK = None
PROMPT = ""

@app.route("/task", methods=['POST'])
def user_option():
    global TASK, PROMPT
    TASK = request.form.get("action") 
    logging.info(f"Task generation successfull selected task is = {TASK}")
    PROMPT = data[TASK] if TASK in data and TASK is not None else ''
    return render_template("chat.html")

@app.route("/api-access", methods=['POST'])
def api_access():
    global MODEL, API_KEY  
    MODEL = request.form.get("model_name")
    API_KEY = request.form.get("api_key")
    return render_template("chat.html")

@app.route("/query", methods=['POST'])
def text_processor():
    user_input = PROMPT + request.form.get("user_input")
    try:
        logging.info("Calling api ...")
        generator = TextGenerator(api=API_KEY.strip())
        logging.info(f"TextGenerator successfull with aip = {API_KEY} and model = {MODEL} ..")
        generator.create_client()
        logging.info("create_client successfull ..")
        generator.build_completion(user_input=user_input)
        logging.info("build_completion successfull ..")
        response = generator.generate()
        logging.info("Response Generated successfully..")
        return render_template("chat.html", response=response)
    except Exception as e:
        return render_template("chat.html", response="Transformer is not working, or you may have reached the API usage limit.")

@app.route("/")
def home_page():
    return render_template("user_log_in.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
