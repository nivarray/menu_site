from flask import Flask, render_template

app = Flask(__name__)


# Menu data
"""Update for all cookies, and add images. Make description sound more enticing"""
menu_items = [
    {
        'name': 'Chocolate Chip Cookie',
        'description': 'Big, soft brown sugar cookie made with semisweet chocolate chips and mini chocolate chips sprinkled with coarse sea salt.',
        'price': '$2.50',
        'image_url': 'static/images/Chocolate_Chip.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'Biscoff Cookie',
        'description': 'Brown sugar cookie made with crushed Biscoff biscuits stuffed with Biscoff cookie butter.',
        'price': '$2.00',
        'image_url': 'static/images/Biscoff_Butter.PNG', 
        'Availability':'In Stock!'
    },
    {
        'name': 'S’mores Cookie',
        'description': 'Chocolate chip cookie stuffed with a graham cracker, Hershey’s chocolate, and a jumbo marshmallow. Topped with mini marshmallows, chopped milk chocolate bar pieces, and graham cracker crumbs.',
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
        'description': 'Moist oatmeal spice cookie mixed with dried cranberries and white chocolate chips. Optional macadamia nuts.',
        'price': '$2.00',
        'image_url': 'static/images/Oatmeal_Cranberry.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'White Chocolate Macadamia Cookie',
        'description': 'Brown sugar cookie made with freshly chopped buttery rich macadamia nuts and white chocolate chips.',
        'price': '$2.00',
        'image_url': 'static/images/White_Chocolate_Macadamia.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'Red Velvet Cookie',
        'description': 'Luscious moist red velvet cake cookie mixed with white chocolate chips.',
        'price': '$2.00',
        'image_url': 'static/images/Red_Velvet.PNG', 
        'Availability':'In Stock!'
    },
    {
        'name': 'Pumpkin Snickerdoodle Cookie',
        'description': 'Brown butter pumpkin spice cookie covered in cinnamon sugar.',
        'price': '$2.00',
        'image_url': 'static/images/Pumpkin_Snickerdoodle.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'Apple Pie Cookie',
        'description': 'Soft vanilla spiced cookie with buttery pie crust pieces and freshly chopped juicy honeycrisps.',
        'price': '$2.00',
        'image_url': 'static/images/Apple_Pie.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'M&M’s® Cookie',
        'description': 'Brown sugar chocolate chip cookie made with M&M’s® milk chocolate candies.',
        'price': '$2.00',
        'image_url': 'static/images/M&M\'s.png', 
        'Availability':'In Stock!'
    },
    {
        'name': 'Peanut Butter Cookie',
        'description': 'The perfect peanut butter cookie. Soft, chewy interior. Crispy exterior.',
        'price': '$2.00',
        'image_url': 'NEEDS IMAGE', 
        'Availability':'In Stock!'
    }
    ]


# main page is menu page
@app.route('/')
def menu_page():
    return render_template('menu.html', menu_items=menu_items)

# Indicates that script is being executed directly, good practice. meaning this will run when running "flask app" on terminal.
if __name__ == '__main__': # Checks if script is being run directly
    app.run(debug=True) # server starts in debug mode