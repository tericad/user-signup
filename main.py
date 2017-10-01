from flask import Flask, request, redirect, render_template

app=Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', title="Signup")





if __name__ == '__main__':
    app.run()
