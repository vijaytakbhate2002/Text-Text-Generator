from flask import Flask, render_template, request
from markupsafe import Markup
from text_process.text_generator import TextGenerator
import json

with open("data.json", 'r') as file:
    data = json.loads(file.read())

with open("UI_data.json", 'r') as UI_file:
    UI_data = json.loads(UI_file.read())

UI_data['PROMPT'] = UI_data['TASK'] = data['API'] = data['MODEL'] = ""
placeholder = "Ask me anything ..."

app = Flask(__name__)

@app.route('/bot')
def bot(response:str="", query_input:str=""):
    global placeholder, UI_data
    placeholder = '-'.join(UI_data['TASK'].split(' ')) + "..."
    return render_template('chat.html', task = placeholder, response=response, query_input=query_input)

@app.route("/api_access")
def api_access():
    return render_template("api_access.html")

@app.route("/task", methods=['POST'])
def user_option():
    UI_data["TASK"] = request.form.get("action") 
    UI_data["PROMPT"] = data[UI_data["TASK"]] if UI_data["TASK"] in data.keys() and UI_data["TASK"] is not None else 'Just Chat'
    with open("UI_data.json", 'w') as file:
        json.dump(UI_data, file)
    return bot()

@app.route("/model_info", methods=['GET', 'POST'])
def model_info():
    UI_data['API'] = request.form.get("api_key")
    UI_data['MODEL'] = request.form.get('model_name')
    with open("UI_data.json", 'w') as file:
        json.dump(UI_data, file)
    return bot()

@app.route("/query", methods=['GET', 'POST'])
def text_processor():
    user_input = UI_data["PROMPT"] + request.form.get("user_input")
    query_input="You: " + request.form.get("user_input")
    try:
        generator = TextGenerator(api=UI_data['API'].strip(), model=UI_data['MODEL'].strip())
        generator.create_client()
        generator.build_completion(user_input=user_input)
        response = generator.generate()
        if len(response.strip()) == 0:
            response = Markup(
                "You entered wrong model name or You have hit the API usage limit."
                "Check it from the NVIDIA website: "
                "<a href='https://build.nvidia.com/nvidia/llama-3_1-nemotron-70b-instruct' target='_blank'>"
                "NVIDIA API Page</a>"
            )
        return bot(response=response, query_input=query_input)
    except:
        response = Markup(
                "You have hit the API usage limit. "
                "Recreate your API from the NVIDIA website: "
                "<a href='https://build.nvidia.com/nvidia/llama-3_1-nemotron-70b-instruct' target='_blank'>"
                "NVIDIA API Page</a>"
            )
        return bot(response=response, query_input=query_input)


@app.route('/')
def user_guide():
    return render_template('user_guide.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
