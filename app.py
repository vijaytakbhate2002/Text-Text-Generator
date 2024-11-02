from flask import Flask, render_template, request, jsonify
from text_process.text_generator import TextGenerator
import json
import logging
import jinja2

logging.basicConfig(
    filename="model_log.log",
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

with open("data.json", 'r') as file:
    data = json.loads(file.read())

with open("UI_data.json", 'r') as UI_file:
    UI_data = json.loads(UI_file.read())

UI_data['PROMPT'] = UI_data['TASK'] = data['API'] = data['MODEL'] = ""

app = Flask(__name__)

@app.route('/bot')
def bot():
    return render_template('navbar_templates/chat.html', task = '-'.join(UI_data['TASK'].split(' ')) + "...")

@app.route("/api_access")
def api_access():
    return render_template("api_access.html")

@app.route("/task", methods=['GET', 'POST'])
def user_option():
    UI_data["TASK"] = request.form.get("action") 
    logging.info(f"UI Rquest = {request.form.get("action")}")
    logging.info(f"Task generation successfull selected task is = {UI_data["TASK"]}, FROM HTML = {request.form.get("action")}")
    UI_data["PROMPT"] = data[UI_data["TASK"]] if UI_data["TASK"] in data.keys() and UI_data["TASK"] is not None else 'Just Chat'
    logging.info("task page is loading ...")
    return render_template("navbar_templates/chat.html", task = '-'.join(UI_data['TASK'].split(' ')) + "...")

@app.route("/model_info", methods=['GET', 'POST'])
def model_info():
    UI_data['API'] = request.form.get("api_key")
    UI_data['MODEL'] = request.form.get('model_name')
    with open("UI_data.json", 'w') as file:
        json.dump(UI_data, file)

    logging.info(f"api access successfull with api = {UI_data['API']} and model = {UI_data['MODEL']}")
    return bot()

@app.route("/query", methods=['GET', 'POST'])
def text_processor():
    user_input = UI_data["PROMPT"] + request.form.get("user_input")
    try:
        logging.info("Calling api ...")
        generator = TextGenerator(api=UI_data['API'].strip(), model=UI_data['MODEL'].strip())
        logging.info(f"TextGenerator successfull with aip = {UI_data['API']}")
        generator.create_client()
        logging.info("create_client successfull ..")
        generator.build_completion(user_input=user_input)
        logging.info("build_completion successfull ..")
        response = generator.generate()
        logging.info("Response Generated successfully..- from flask")
        return render_template("navbar_templates/chat.html", response=response)
    except Exception as e:
        raise(e)
        return render_template("navbar_templates/chat.html", response="Transformer is not working, or you may have reached the API usage limit.")

@app.route('/')
def user_guide():
    logging.info("user_guide page is loading ...")
    return render_template('navbar_templates/user_guide.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
