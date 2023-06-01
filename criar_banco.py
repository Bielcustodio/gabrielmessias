from nomedosite import database, app
from nomedosite.models import Usuario, Foto

with app.app_context():
    database.create_all()

