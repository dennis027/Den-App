from app.forms import ReviewForm
from flask import render_template,request,redirect,url_for
from app import app
from .models import reviews
Review = reviews.Review
#Views
@app.route('/' ,methods=['GET', 'POST'])
def index():
    '''
    view root page function that returns index page and its data
    '''
    title = 'Home -Welcome to Deman App where you will get the best User Experience'

    
    return render_template('index.html',title=title)

def new_review(id):
    form=(ReviewForm)
    #poster=get_poster(Id)
    if form.validate_on_submit():
        title=form.title.data
        review=form.review.data
        new_review=Review (title, review)
        new_review.save_review()
        return redirect(url_for("poster",id=poster.id))
    title= f'{poster.id} review'  
    return render_template('new_review.html', title=title,review_form=form)




