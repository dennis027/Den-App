from app import auth
from .forms import ReviewForm,UpdateProfile
from flask import render_template,request,redirect,url_for,flash,abort
from . import main
from flask_login import login_required,login_user,logout_user
from ..models import User
from .. import db 


#Views
@main.route('/' ,methods=['GET', 'POST'])
def index():

    '''
    view root page function that returns index page and its data
    ''' 
    title = 'Home -Welcome to Deman App where you will get the best User Experience'

    
    return render_template('index.html',title=title)

# def new_review(id):
#     form=(ReviewForm)
#     #poster=get_poster(Id)
#     if form.validate_on_submit():
#         title=form.title.data
#         review=form.review.data
#         new_review=Review (title, review)
#         new_review.save_review()
#         return redirect(url_for("poster",id=poster.id))
#     title= f'{poster.id} review'  
#     return render_template('new_review.html', title=title,review_form=form)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)    


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    
