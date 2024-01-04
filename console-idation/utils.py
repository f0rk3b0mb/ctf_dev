from functools import wraps
from flask import session, redirect, url_for

#login check

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("web.login"))
        return func(*args, **kwargs)
    return decorated_function




def filter(filename):
    if "../" in filename:
        return filename.replace("../", "")
    else:
        return filename