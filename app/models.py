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
