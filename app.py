from flask import Flask, render_template

app = Flask(__name__)


# Menu data
"""Update for all cookies, and add images. Make description sound more enticing"""
menu_items = [
    {
        'name': 'Chocolate Chip Cookie',
        'description': 'Classic chocolate chip cookie with gooey chocolate chips.',
        'price': '$2.50',
        'image_url': 'static/images/Chocolate_Chip.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'M&M’s Cookie',
        'description': 'Hearty oatmeal cookie with plump raisins.',
        'price': '$2.00',
        'image_url': 'static/images/Biscoff_Butter.PNG', 
        'Availability':'In Stock!'
    },
    {
        'name': 'S’mores Cookie',
        'description': 'A buttery, soft cookie loaded with roasted pecans and a hint of vanilla, offering a delightful crunch in every bite.',
        'price': '$2.00',
        'image_url': 'static/images/Smores.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'Fruity Pebbles Cookie',
        'description': 'A buttery, soft cookie loaded with roasted pecans and a hint of vanilla, offering a delightful crunch in every bite.',
        'price': '$2.00',
        'image_url': 'static/images/Fruity_Pebbles.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'Cranberry Oatmeal Cookie',
        'description': 'A buttery, soft cookie loaded with roasted pecans and a hint of vanilla, offering a delightful crunch in every bite.',
        'price': '$2.00',
        'image_url': 'static/images/Oatmeal_Cranberry.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'White Chocolate Macadamia Cookie',
        'description': 'A buttery, soft cookie loaded with roasted pecans and a hint of vanilla, offering a delightful crunch in every bite.',
        'price': '$2.00',
        'image_url': 'static/images/White_Chocolate_Macadamia.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'Pumpkin Snickerdoodle Cookie',
        'description': 'A buttery, soft cookie loaded with roasted pecans and a hint of vanilla, offering a delightful crunch in every bite.',
        'price': '$2.00',
        'image_url': 'static/images/angry_gunter.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'Apple Pie Cookie',
        'description': 'A buttery, soft cookie loaded with roasted pecans and a hint of vanilla, offering a delightful crunch in every bite.',
        'price': '$2.00',
        'image_url': 'static/images/angry_gunter.png', 
        'Availability':'In Stock!'
    },
    ]


# main page is menu page
@app.route('/')
def menu_page():
    return render_template('menu.html', menu_items=menu_items)

# Indicates that script is being executed directly, good practice. meaning this will run when running "flask app" on terminal.
if __name__ == '__main__': # Checks if script is being run directly
    app.run(debug=True) # server starts in debug mode