from flask import Blueprint, render_template,render_template_string, redirect, url_for, request, session
from database import db, bcrypt , User
from utils import login_required 
import datetime

web = Blueprint('web', __name__)
api = Blueprint('api', __name__)


@web.route("/")
def index():
    return redirect(url_for("web.login"))


@web.before_request
def before_request():
    if 'user_id' in session and session.permanent:
        session.modified = True
    allowed_endpoints = ['web.login', 'web.register', 'web.index']
    if not session.get('user_id') and request.endpoint not in allowed_endpoints:
        return redirect(url_for('web.login'))





@web.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Check if the user exists
        user = User.query.filter(User.email == email).first()

        if user:
                if bcrypt.check_password_hash(user.password, password):
                    session["user_id"] = user.id
                    session["username"] = user.username
                    return redirect(url_for("web.dashboard"))  # Redirect to the profile route
                else:
                    return render_template("login.html", message="Incorrect username or password")
        else:
            return render_template("login.html", message="Incorrect username or password")

    return render_template("login.html")


@web.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")


        # Check if the username is already taken
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template("register.html",message="Username already taken. Please choose another username.")
        else:
            # Hash the password and create a new user
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            new_user = User(username=username,password=hashed_password , email=email, date_registered=datetime.date.today())
            db.session.add(new_user)
            db.session.commit()
            return render_template("login.html", message="Await admin approval") # Redirect to the login route

    return render_template("register.html")


@web.route("/dashboard")
@login_required
def dashboard():
    user = request.args.get('username')
    if user:
        return render_template("dashboard.html", username=render_template_string(user))
    else:
        return render_template("dashboard.html", username=session.get('username'))
    

@web.route("/logout")
def logout():
    session.pop("user_id",None)
    session.pop("username",None)
    session.pop("role",None)
    return redirect(url_for("web.login")) 