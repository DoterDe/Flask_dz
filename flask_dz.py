from flask import Flask, render_template, request , make_response, abort
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/choose', methods = ['POST', 'GET'])
def choose():
    if request.method == 'POST':
        ch = request.form.get('Rus')
        ch1 = request.form.get('English')
        response = None
        if ch is not None:
            response = make_response(render_template('rus.html'))
            response.set_cookie('choice', 'Rus')
        elif ch1 is not None:
            response = make_response(render_template('index.html'))
            response.set_cookie('choice', 'English')
        else:
            response = make_response(render_template('index.html'))
        return response

@app.route('/russetcookie', methods = ['POST', 'GET'])
def russetcookie():
    if request.method == 'POST':
        user = request.form['nm']
        response = make_response(render_template('rusreadcookie.html'))
        response.set_cookie('userID', user)
        return response
    else:
        abort(500)


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        response = make_response(render_template('readcookie.html'))
        response.set_cookie('userID', user)
        return response
    else:
        abort(500)

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'

if __name__ == "__main__":
    app.run(debug=True)
