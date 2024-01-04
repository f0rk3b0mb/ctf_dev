from flask import Flask
from database import db, bcrypt
from blueprints.routes import web, api
from database import User
from datetime import timedelta
#from flask_sslify import SSLify

app = Flask(__name__)
#sslify = SSLify(app)

app.permanent_session_lifetime = timedelta(minutes=5)

# Load your Flask app configuration here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.secret_key = 'b79ddb52b4ed9ba612526393879ae823' # should be sored in environ

# Initialize Flask extensions
db.init_app(app)
bcrypt.init_app(app)

# Register your blueprints
app.register_blueprint(web, url_prefix='/')
app.register_blueprint(api, url_prefix='/api')

# Function to insert a default record
def add_default_record():
    with app.app_context():
        default_user = User(username="ping",password="$2b$12$0hkmhncqXOpQu5NFLAFBCeDyV8q1ndtGDf/LP5dictM4szbwlUg4q" , email="ping@ping.com")
        db.session.add(default_user)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()  #for testing purposes
        db.create_all()
        add_default_record()  # for testing purposes
    app.run(host="0.0.0.0", port=1234)
