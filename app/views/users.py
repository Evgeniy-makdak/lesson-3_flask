# from flask import render_template, request
#
# from app.database import db
# from app.models import Employeer
# from main import appl
#
#
# @appl.get('/')
# def al_users():
#     employees = Employeer.query.all()
#     return render_template(
#         # 'index.html',
#         'templates_with_jinja/index.html',
#         employees=employees,
#     )
#
#
# @appl.post('/insert')
# def insert():
#     user = Employeer(name=request.form['name'], email=request.form['email'], phone=request.form['phone'])
#     db.session.add(user)
#     db.session.commit()
#
#     return al_users()
#
#
# @appl.post('/update')
# def update():
#     user = Employeer.query.get(int(request.form['id']))
#     user.name = request.form['name']
#     user.email = request.form['email']
#     user.phone = request.form['phone']
#     db.session.add(user)
#     db.session.commit()
#
#     return al_users()
#
#
# @appl.route('/delete/<int:id>')
# def delete(id):
#     user = Employeer.query.get(id)
#     db.session.delete(user)
#     db.session.commit()
#
#     return al_users()