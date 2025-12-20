from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    selected_encoding = None
    input_text = ""

    if request.method == "POST":
        selected_encoding = request.form.get("encoding")
        input_text = request.form.get("text")
        type = request.form.get("further-type")


    return render_template(
            "index.html",
        encoding=selected_encoding,
        text=input_text
    )

if __name__ == "__main__":
    app.run(debug=True)
