from flask import Flask
from rutas.inicio import inicio
from rutas.login import login
from rutas.principal import principal
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message


app = Flask(__name__)


mail=Mail(app)

Bootstrap(app)

app.config['SECRET_KEY']='uasyiasazxasd'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://kie1gzz0394fzns9:e56znrit4sbwzopm@eanl4i1omny740jw.cbetxkdyhwsb.us-east-1.rds.amazonaws.com/gn1gxbbmvesc7rvk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'diasconciencia@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

SQLAlchemy(app)


app.register_blueprint(inicio)
app.register_blueprint(login)
app.register_blueprint(principal)


