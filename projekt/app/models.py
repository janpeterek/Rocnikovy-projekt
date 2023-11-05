import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, LargeBinary, String, Enum, Numeric, func
from sqlalchemy.orm import relationship

mindate = datetime.date(datetime.MINYEAR, 1, 1)


class User(Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    registration_date = Column(Date, nullable=False)
    rating_count = Column(Integer, default=0)

    visits = relationship('Visit', backref='user', lazy=True)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"



class Visit(Model):
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    food = Column(Enum('svíčková', 'guláš', 'řízek', name='food_enum'), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    rating = relationship('Rating', lazy=True, back_populates='visit')
    chef_rating = relationship('ChefRating', lazy=True, back_populates='visit')

    def __repr__(self):
        return f"Visit(id={self.id}, date={self.date}, price={self.price}, food='{self.food}', user_id={self.user_id})"



class Rating(Model):
    id = Column(Integer, primary_key=True)
    stars = Column(Enum('1', '2', '3', '4', '5', name='rating_enum'), nullable=False)
    comment = Column(String(500))

    visit_id = Column(Integer, ForeignKey('visit.id'), nullable=False)
    visit = relationship('Visit', back_populates='rating')
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"Rating(id={self.id}, stars={self.stars}, comment='{self.comment}', visit_id={self.visit_id}, restaurant_id={self.restaurant_id})"



class ChefRating(Model):
    id = Column(Integer, primary_key=True)
    stars = Column(Enum('1', '2', '3', '4', '5', name='rating_enum'), nullable=False)
    comment = Column(String(500))

    visit_id = Column(Integer, ForeignKey('visit.id'), nullable=False)
    visit = relationship('Visit', back_populates='chef_rating')
    chef_id = Column(Integer, ForeignKey('chef.id'), nullable=False)
    chef = relationship('Chef', back_populates='chef_ratings')

    def __repr__(self):
        return f"ChefRating(id={self.id}, stars={self.stars}, comment='{self.comment}', visit_id={self.visit_id}, chef_id={self.chef_id})"



class Restaurant(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    opening_year = Column(Integer)
    average_rating = Column(Numeric, default=0.0, onupdate=func.coalesce(func.avg(Rating.stars), 0))
    chefs = relationship('Chef', backref='restaurant', lazy=True)
    website = Column(String(100))
    ico = Column(String(15))
    phone = Column(String(20))
    opening_hours = Column(String(100))

    ratings = relationship('Rating', backref='restaurant', lazy=True)

    def __repr__(self):
        return self.name



class Chef(Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    contact = Column(String(100))

    working_restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    chef_ratings = relationship('ChefRating', back_populates='chef')
    average_rating = Column(Numeric, default=0.0, onupdate=func.coalesce(func.avg(ChefRating.stars), 0))
    favorite_foods = relationship('FavoriteFood', back_populates='chef')

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"



class FavoriteFood(Model):
    id = Column(Integer, primary_key=True)
    food_name = Column(String(100), nullable=False)
    chef_id = Column(Integer, ForeignKey('chef.id'), nullable=False)
    chef = relationship('Chef', back_populates='favorite_foods')

    def __repr__(self):
        return self.food_name








class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class Vyrobce(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class Contact(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    address = Column(String(564))
    birthday = Column(Date, nullable=True)
    personal_phone = Column(String(20))
    personal_celphone = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey("contact_group.id"), nullable=False)
    contact_group = relationship("ContactGroup")
    gender_id = Column(Integer, ForeignKey("gender.id"), nullable=False)
    gender = relationship("Gender")

    def __repr__(self):
        return self.name

    def month_year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, 1, 1)
