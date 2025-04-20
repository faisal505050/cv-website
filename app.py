from flask import Flask, render_template, send_file
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download-cv")
def download_cv():
    return send_file("static/Faisal_Saad_Alharbi_CV.pdf", as_attachment=True)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)