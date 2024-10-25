from flask import Flask, render_template

app = Flask(__name__)


# Menu data
"""Update for all cookies, and add images. Make description sound more enticing"""
menu_items = [
    {
        'name': 'Chocolate Chip Cookie',
        'description': 'Classic chocolate chip cookie with gooey chocolate chips.',
        'price': '$2.50',
        'image_url': 'static/images/kitten.png' 
    },
    {
        'name': 'Oatmeal Raisin Cookie',
        'description': 'Hearty oatmeal cookie with plump raisins.',
        'price': '$2.00',
        'image_url': 'static/images/capy.jpg'
    },
    {
        'name': 'Butter Pecan Cookie',
        'description': 'A buttery, soft cookie loaded with roasted pecans and a hint of vanilla, offering a delightful crunch in every bite.',
        'price': '$2.00',
        'image_url': 'static/images/angry_gunter.png'
    }]

# main page is menu page
@app.route('/')
def menu_page():
    return render_template('menu.html', menu_items=menu_items)

# Indicates that script is being executed directly, good practice. meaning this will run when running "flask app" on terminal.
if __name__ == '__main__': # Checks if script is being run directly
    app.run(debug=True) # server starts in debug mode