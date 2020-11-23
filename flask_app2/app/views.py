from app import app
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField
from flask import render_template,redirect, url_for
from testing.Database import db
class DataInsert(FlaskForm):
    firstname = StringField('first Name')
    lastname = StringField('last Name')
    age = IntegerField('age')
    submit = SubmitField('submit')
@app.route('/data', methods=['GET','POST'])
def index():
    form = DataInsert()
    if form.validate_on_submit():
        db.sumbit_tester(form.firstname.data, form.lastname.data, form.age.data)
        return redirect(url_for('viewdata'))

    return render_template('insert_data.html',form=form)

@app.route('/data/view')
def viewdata():
    data = db.Pull_Tester()
    return render_template('viewdata.html',data=data)