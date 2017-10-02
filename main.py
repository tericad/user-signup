from flask import Flask, request, redirect, render_template

app=Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', title="Signup")

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ""
    email_error = ''

    if len(username) < 3 or len(username) > 20 or " " in username:
        username = ''
        password = ''
        verify_password = ''
        username_error = 'Username is required: It must be between 3-20 charachters with no spaces.'
    if len(password) < 3 or len(password) > 20 or " " in password:
        password = ''
        password_error = 'Password is required: It must be between 3-20 charachters with no spaces.'
    if verify_password != password:
        password = ''
        verify_password = ''
        verify_password_error = "Verify password is required: It must match your password exactly."
    if len(email) > 0:
        if len(email) < 3 or len(email) > 20 or " " in email or '@' not in email or '.' not in email:
            email = ''
            password = ''
            verify_password = ''
            email_error = 'Email addresses must be between 3-20 charachters long with no spaces. A @ and a . are also required.'
    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/welcome?username=' + username)
    else:
        return render_template('index.html', username_error=username_error, 
    password_error=password_error, verify_password_error=verify_password_error,
    email_error=email_error, username=username, password=password, 
    verify_password=verify_password, email=email)
        
@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


if __name__ == '__main__':
    app.run()
