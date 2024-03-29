from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    users = [{"name": "Иван", "email": "ivan@example.com"}, {"name": "Анна", "email": "anna@example.com"}]
    return render_template('home.html', users=users)




if __name__ == "__main__":
    app.run(debug=True)
