from flask import Flask, render_template, request
from app.config import Config
from app.database import db
from app.models import Employeer


def create_app(config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application):
    db.init_app(application)
    db.create_all()


app_config = Config()
appl = create_app(app_config)
configure_app(appl)


@appl.get('/')
def al_users():
    employees = Employeer.query.all()
    return render_template(
        # 'index.html',
        'templates_with_jinja/index.html',
        employees=employees,
    )


@appl.post('/insert')
def insert():
    user = Employeer(name=request.form['name'], email=request.form['email'], phone=request.form['phone'])
    db.session.add(user)
    db.session.commit()

    return al_users()


@appl.post('/update')
def update():
    user = Employeer.query.get(int(request.form['id']))
    user.name = request.form['name']
    user.email = request.form['email']
    user.phone = request.form['phone']
    db.session.add(user)
    db.session.commit()

    return al_users()


@appl.route('/delete/<int:id>')
def delete(id):
    user = Employeer.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return al_users()


if __name__ == '__main__':
    appl.run()
