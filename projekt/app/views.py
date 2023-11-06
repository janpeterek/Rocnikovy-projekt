import calendar

from flask_appbuilder import ModelView
from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Contact, ContactGroup, Gender, Vyrobce, User, Visit, Rating, Chef, Restaurant, ChefRating, FavoriteFood


def fill_gender():
    try:
        db.session.add(Gender(name="Male"))
        db.session.add(Gender(name="Female"))
        db.session.commit()
    except Exception:
        db.session.rollback()


class UserView(ModelView):
    datamodel = SQLAInterface(User)

    list_columns = ['id', 'first_name', 'last_name', 'registration_date', 'rating_count']

    base_order = ("last_name", "asc")


class VisitView(ModelView):
    datamodel = SQLAInterface(Visit)

    list_columns = ['id', 'date', 'price', 'food', 'user.first_name', 'user.last_name']

    base_order = ("date", "asc")

class RatingView(ModelView):
    datamodel = SQLAInterface(Rating)

    list_columns = ['id', 'stars', 'comment', 'visit.date', 'restaurant.name']

    base_order = ("stars", "asc")

class ChefView(ModelView):
    datamodel = SQLAInterface(Chef)

    list_columns = ['id', 'first_name', 'last_name', 'birth_date', 'average_rating', 'photo']

    list_columns = ['photo_img_thumbnail', 'name']
    
    show_columns = ['photo_img','name']

    base_order = ("last_name", "asc")


class RestaurantView(ModelView):
    datamodel = SQLAInterface(Restaurant)

    list_columns = ['id', 'name', 'address', 'opening_year', 'average_rating', 'phone']

    base_order = ("name", "asc")

class ChefRatingView(ModelView):
    datamodel = SQLAInterface(ChefRating)

    list_columns = ['id', 'stars', 'comment', 'visit.date', 'chef.first_name', 'chef.last_name']

    base_order = ("stars", "asc")



    


class FavoriteFoodView(ModelView):
    datamodel = SQLAInterface(FavoriteFood)

    list_columns = ['id', 'food_name', 'chef.first_name', 'chef.last_name']

    base_order = ("food_name", "asc")


class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    list_columns = ["name", "personal_celphone", "birthday", "contact_group.name"]

    base_order = ("name", "asc")
    show_fieldsets = [
        ("Summary", {"fields": ["name", "gender", "contact_group"]}),
        (
            "Personal Info",
            {
                "fields": [
                    "address",
                    "birthday",
                    "personal_phone",
                    "personal_celphone",
                ],
                "expanded": False,
            },
        ),
    ]

    add_fieldsets = [
        ("Summary", {"fields": ["name", "gender", "contact_group"]}),
        (
            "Personal Info",
            {
                "fields": [
                    "address",
                    "birthday",
                    "personal_phone",
                    "personal_celphone",
                ],
                "expanded": False,
            },
        ),
    ]

    edit_fieldsets = [
        ("Summary", {"fields": ["name", "gender", "contact_group"]}),
        (
            "Personal Info",
            {
                "fields": [
                    "address",
                    "birthday",
                    "personal_phone",
                    "personal_celphone",
                ],
                "expanded": False,
            },
        ),
    ]

class VyrobceView(ModelView):
    datamodel = SQLAInterface(Vyrobce)

class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]


class ContactChartView(GroupByChartView):
    datamodel = SQLAInterface(Contact)
    chart_title = "Grouped contacts"
    label_columns = ContactModelView.label_columns
    chart_type = "PieChart"

    definitions = [
        {"group": "contact_group", "series": [(aggregate_count, "contact_group")]},
        {"group": "gender", "series": [(aggregate_count, "contact_group")]},
    ]


def pretty_month_year(value):
    return calendar.month_name[value.month] + " " + str(value.year)


def pretty_year(value):
    return str(value.year)


class ContactTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Contact)

    chart_title = "Grouped Birth contacts"
    chart_type = "AreaChart"
    label_columns = ContactModelView.label_columns
    definitions = [
        {
            "group": "month_year",
            "formatter": pretty_month_year,
            "series": [(aggregate_count, "group")],
        },
        {
            "group": "year",
            "formatter": pretty_year,
            "series": [(aggregate_count, "group")],
        },
    ]


appbuilder.add_view(
    UserView,
    "Seznam uživatelů",
    icon="fa-users-line",
    category="Uživatelé",
    category_icon="fa-envelope"
)

appbuilder.add_view(
    VisitView,
    "Seznam návštěv",
    icon="fa-folder-open-o",
    category="Návštěvy",
    category_icon="fa-solid fa-shop"
)

appbuilder.add_view(
    RatingView,
    "Seznam hodnocení",
    icon="fa-regular fa-star",
    category="Hodnocení",
    category_icon="fa-star"
)

appbuilder.add_view(
    ChefRatingView,
    "Seznam hodnocení kuchaře",
    icon="fa-regular fa-star",
    category="Hodnocení",
    category_icon="fa-star"
)

appbuilder.add_view(
    RestaurantView,
    "Seznam restaurací",
    icon="fa-folder-open-o",
    category="Restaurace",
    category_icon="fa-cutlery"
)

appbuilder.add_view(
    ChefView,
    "Seznam šéfkuchařů",
    icon="fa-users",
    category="Šéfkuchaři",
    category_icon="fa-kitchen-set"
)

appbuilder.add_view(
    FavoriteFoodView,
    "Seznam oblíbených jídel",
    icon="fa-cutlery",
    category="Oblíbená jídla",
    category_icon="fa-pizza-slice"
)






