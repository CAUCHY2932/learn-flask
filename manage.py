# coding: utf-8
from flask_migrate import Migrate
import os
from application import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app=app)


@app.shell_context_processor
def make_shell_context():
    pass


@app.cli.command()
def deploy():
    pass


if __name__ == '__main__':
    app.run(debug=True)
