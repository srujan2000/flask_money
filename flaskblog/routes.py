from flask.helpers import flash
from wtforms.validators import Email
from flaskblog import app,db
from flask import render_template, url_for, redirect, request,abort
from flaskblog.forms import SpentForm,RecForm,LoginForm
from flaskblog.models import Spec, Rec, Login
from flask_login import login_required,current_user,login_user,logout_user

@app.route("/")
@app.route("/home")
def home():
    total_spent = 0 
    total_recieved = 0
    spent = Spec.query.all()
    recieved = Rec.query.all()
    
    for s in spent:
        total_spent = total_spent + int(s.amount)
    
    for r in recieved:
        total_recieved = total_recieved + int(r.amount)

    total = total_recieved - total_spent
    return render_template('home.html',total_rec=total_recieved,total_spec =total_spent,total = total)


@app.route("/recieved")
@login_required
def recieved():
    total = Rec.query.all()
    return render_template('recieved.html',rec = total)


@app.route("/spent")
@login_required
def spent():
    total = Spec.query.all()
    return render_template('spent.html',spent = total)


@app.route("/spentForm",methods = ['GET','POST'])
@login_required
def spentForm():
    form = SpentForm()
    
    if form.validate_on_submit():
        # return f'<h1>{form.date.data},{form.amount.data},{form.wher.data},{form.purchased.data}<h1>'

        spent = Spec(date = form.date.data,amount=form.amount.data,wher = form.wher.data,pur =form.purchased.data )

        db.session.add(spent)
        db.session.commit()
        
        return redirect(url_for('spent'))


    return render_template('spentForm.html',form=form)

@app.route("/recievedForm",methods = ['GET','POST'])
@login_required
def recForm():
    form = RecForm()

    if form.validate_on_submit():
    #    return f'<h1>{form.date.data},{form.amount.data},{form.fro.data},{form.reason.data}<h1>'
       
        rec = Rec(date = form.date.data,amount=form.amount.data,fro = form.fro.data,reason =form.reason.data )

        db.session.add(rec)
        db.session.commit()
        
        return redirect(url_for('recieved'))

    return render_template('recForm.html',form=form)

@app.route("/Login",methods=['GET','POST'])
def login():

      if current_user.is_authenticated:
        return redirect(url_for('home'))

      form = LoginForm()
      
      if form.validate_on_submit():
          user = Login.query.filter_by(email = form.email.data).first()

          if user and (user.password == form.password.data):
              login_user(user)
              return redirect(url_for('home'))
      return render_template('login.html',form=form)

@app.route("/Logout",methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/CheckRec/<int:rec_id>")
@login_required
def check_rec(rec_id):
    rec = Rec.query.get_or_404(rec_id)
    return render_template('check_rec.html',rec = rec)

@app.route("/CheckSpent/<int:spec_id>")
@login_required
def check_spent(spec_id):
    spec = Spec.query.get_or_404(spec_id)
    return render_template('check_spent.html',spec = spec)

@app.route("/Rec/int:<rec_id>/update",methods=['GET','POST'])
@login_required
def update_rec(rec_id):
    
    rec = Rec.query.get_or_404(rec_id)

    form = RecForm()

    if form.validate_on_submit():
        rec.date = form.date.data
        rec.amount = form.amount.data
        rec.fro  = form.fro.data
        rec.reason = form.reason.data

        db.session.commit()
        flash('It has been Updated','success')
        return redirect(url_for('home'))

    elif request.method == 'GET':
         form.date.data = rec.date
         form.amount.data = rec.amount
         form.fro.data = rec.fro
         form.reason.data = rec.reason

    return render_template('recForm.html',form=form)

@app.route("/Spent/int:<spec_id>/update",methods=['GET','POST'])
@login_required
def update_spec(spec_id):
    
    spec = Spec.query.get_or_404(spec_id)

    form = SpentForm()

    if form.validate_on_submit():
        spec.date = form.date.data
        spec.amount = form.amount.data
        spec.wher  = form.wher.data
        spec.pur = form.purchased.data

        db.session.commit()
        flash('It has been Updated','success')
        return redirect(url_for('home'))

    elif request.method == 'GET':
         form.date.data = spec.date
         form.amount.data = spec.amount
         form.wher.data = spec.wher
         form.purchased.data = spec.pur

    return render_template('spentForm.html',form=form)



@app.route("/Rec/int:<rec_id>/delete",methods=['GET','POST'])
@login_required
def delete_rec(rec_id):
    rec = Rec.query.get_or_404(rec_id)
    db.session.delete(rec)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/Spent/int:<spec_id>/delete",methods=['GET','POST'])
@login_required
def delete_spec(spec_id):
    spec = Spec.query.get_or_404(spec_id)
    db.session.delete(spec)
    db.session.commit()
    return redirect(url_for('home'))


