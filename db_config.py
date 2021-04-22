from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = "tux"
app.config['MYSQL_DATABASE_PASSWORD'] = "licet@123"
app.config['MYSQL_DATABASE_DB'] = "opencloud"
app.config['MYSQL_DATABASE_HOST'] = "vpn.opencloud.pattarai.in"
mysql.init_app(app)
