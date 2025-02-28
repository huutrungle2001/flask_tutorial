from flask_migrate import Migrate
from sys import exit
from decouple import config
from apps import create_app, db, SQLALCHEMY_DATABASE_URI
from apps.models import *


DEBUG = config('DEBUG', default=True, cast=bool)


app = create_app()

Migrate(app, db)

app.logger.info('DEBUG       = ' + str(DEBUG))
app.logger.info('Environment = ' + "DEBUG")
app.logger.info('DBMS        = ' + SQLALCHEMY_DATABASE_URI)

if __name__ == "__main__":
    app.run(port=5500, debug=DEBUG)
