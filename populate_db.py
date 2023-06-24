from home import app, food_db
from home import FoodItem

# populate database woooo
# i can probbaly just include this in home.py to avoid circular dependencies
# if that causes problems ill move it


def populate_food_items():
    with app.app_context():
        # Create the food items
        pizza = FoodItem(name='Pizza', description='gluten')
        burger = FoodItem(name='Burger', description='gluten')
        salad = FoodItem(name='Salad', description='nuts')

        # Add the food items to the database
        food_db.session.add(pizza)
        food_db.session.add(burger)
        food_db.session.add(salad)

        # Commit the changes to the database
        food_db.session.commit()


# Call the function to populate the food items database
populate_food_items()
