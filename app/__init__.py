from flask import Flask, render_template
from flask_migrate import Migrate
from app.extensions import db
from app.routes.user import user_bp

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuração do app
    app.config.from_object('config')

    # Inicialização do banco de dados e migrações
    migrate.init_app(app, db)

    # Registrando o blueprint
    app.register_blueprint(user_bp, url_prefix='/users')

    @app.route('/')
    def index():
        return render_template('index.html')

    # Garante que os modelos sejam registrados
    with app.app_context():
        from app.models import User  # Importe aqui para registrar os modelos

    db.init_app(app)
    return app