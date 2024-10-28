from flask import Flask, render_template, request
from text_process.text_generator import TextGenerator
from config.config import API_KEY

app = Flask(__name__)

@app.route("/query", methods=['GET', 'POST'])
def textProcessor():
    print(request.form.get("user_input"))
    user_input = request.form.get("user_input")
    try:
        generator = TextGenerator(api=API_KEY)
        generator.create_client()
        generator.build_completion(user_input=user_input)
        response = generator.generate()
        return render_template("chat.html", response=response)
    except:
        return render_template("chat.html", response="Transformer is not working, or you may have reached the API usage limit.")
    
@app.route("/")
def homePage():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
