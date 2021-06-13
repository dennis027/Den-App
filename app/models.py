
from flask_script import Manager
from . import db
class Review:
    all_reviews = []

    def __init__(self,pitches_id,title,imageurl,review):
        self.pitches_id = pitches_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_reviews(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()            
    @classmethod
    def get_reviews(cls,id):
        response =[]
        for review in cls.all_reviews:
            if review.poster_id == id:
                response.append(review)
        return response  

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    role_id=db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'user {self.username}'  



#....
# @manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,User = User )
# if __name__ == '__main__':
#     manager.run()

class Role(db.Model):
    __tablename__='roles'

    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(255))
    user= db.relationship('User', backref= 'role',lazy="dynamic")

    def __repr__(self):
        return f'User{self.name}'