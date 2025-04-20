from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    print(f"رسالة جديدة من {name} - {email}: {message}")
    return render_template('index.html', success=True)

if __name__ == "__main__":
    app.run(debug=True)