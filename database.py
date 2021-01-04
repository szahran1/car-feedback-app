from app import db, Feedback

feedback = Feedback.query.all()
print(feedback[3].customer)
print(feedback[3].dealer)
print(feedback[3].rating)
print(feedback[3].comments)