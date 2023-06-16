from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("All authors must have a name")
        return name
    
    @validates('phone_number')
    def validate_phone_number(self, key, phone):
        if len(phone) != 10:
            raise ValueError("Must be exactly 10 characters")
        return phone
        


class Post(db.Model):
    __tablename__ = 'posts'

    @validates('title')
    def validate_title(self, key, title):
        if title is None:
            raise ValueError("All posts must have a title")
        return title
    
    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError("Post content must be at least 250 characters")
        return content
    
    @validates('summary')
    def validate_summary(self, key, content):
        if len(content) >= 250:
            raise ValueError("Post summary must be less than 250 characters")
        return content
    
    @validates('category')
    def validate_category(self, key, category):
        if category not in ['Fiction', 'Non-Fiction']:
            raise ValueError('Must be fiction or Non-Fiction')
        return category

    @validates('title')
    def validate_title(self, key, title):
        keywords = ["Won't Believe", "Secret", "Top", "Guess"]
        if any(keyword in title for keyword in keywords):
            return title
        raise ValueError("Must have one of the keywords!")
    

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
