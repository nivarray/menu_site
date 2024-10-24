from flask import Flask, render_template

app = Flask(__name__)


# Menu data
"""Update for all cookies, and add images. Make description sound more enticing"""
menu_items = [
    {
        'name': 'Chocolate Chip Cookie',
        'description': 'Classic chocolate chip cookie with gooey chocolate chips.',
        'price': '$2.50',
        #'image_url': 'static/images/chocolate_chip_cookie.jpg' 
    },
    {
        'name': 'Oatmeal Raisin Cookie',
        'description': 'Hearty oatmeal cookie with plump raisins.',
        'price': '$2.00',
        #'image_url': 'static/images/oatmeal_raisin_cookie.jpg'
    }]

# main page is menu page
@app.route('/')
def menu_page():
    return render_template('menu.html', menu_items=menu_items)

# Indicates that script is being executed directly, good practice. meaning this will run when running "flask app" on terminal.
if __name__ == '__main__': # Checks if script is being run directly
    app.run(debug=True) # server starts in debug mode