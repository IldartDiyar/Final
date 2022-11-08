from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from apio import *
app = Flask(__name__)


def setterr(username="", flag=False):
    global authg
    global UserData
    authg = flag
    UserData = username


@app.route('/')
def index():
    try:
        authg
        if authg:
            return redirect('home')
        else:
            return redirect('login')
    except:
        setterr()
        return redirect('login')
    return render_template("index.html")


@app.route('/home', methods=["GET"])
def home():
    foods = getter_all_api(UserData)
    print(foods)

    return render_template("home.html", foods=foods)


@app.route('/insert', methods=["POST"])
def insert():
    if request.method == "POST":
        newItem = request.form.get("item")
        print(newItem)
        insert_apio(UserData, newItem)
        return redirect('/home')


@app.route("/update", methods=["POST"])
def update():

    if request.method == "POST":
        newItem = request.form.get("newItem")
        oldItem = request.form.get("oldItem")
        update_api(newItem, oldItem, UserData)
        return redirect("/home")


@app.route("/delete", methods=["POST"])
def delete():
    if request.method == "POST":
        item = request.form.get("item")
        delete_api(item, UserData)
        return redirect("/home")


@app.route('/login', methods=["GET", "POST"])
def login():

    msg = ''
    if authg:
        return redirect(url_for('home'))
    if request.method == "POST":
        username = request.form['login']
        password = request.form['password']
        user = check_credo_API(username, password)
        if user == False:
            msg = 'Account does not exist'
        elif user == True:
            setterr(username, True)
            print(username)
            print(user)
            return redirect('home')
        else:
            msg = 'Invalid email address or password!'
    return render_template("login.html",  msg=msg)


@app.route('/registration', methods=["GET", "POST"])
def registration():
    if authg:
        return redirect(url_for('home'))
    msg = ''
    if request.method == "POST":
        print("start")
        username = request.form['login']
        password = request.form['password']
        password1 = request.form['password1']
        if password1 == password1:
            user = InsertApi(username, password)
        else:
            msg = 'Check password'
        if user == False:
            msg = 'Come again in 2 hours'
        elif user == True:
            return redirect("/login")
        else:
            msg = 'Something wrong'
    return render_template("registration.html", msg=msg)


@ app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/login")


if __name__ == "__main__":

    app.run(debug=True)
