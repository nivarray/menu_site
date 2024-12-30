from flask import Flask, render_template

app = Flask(__name__)

# price_dict = {'1 Cookie': f"{5:.2f}",
#               '4 Cookies': f"{18:.2f}",
#               '6 Cookies': f"{25:.2f}",
#               '12 Cookies': f"{40:.2f}"}

# Menu data
"""Update for all cookies, and add images. Make description sound more enticing"""
menu_items = [
    {
        'name': 'Chocolate Chip Cookie',
        'details':{
            'description': 'Big, soft brown sugar cookie made with semisweet chocolate chips and mini chocolate chips sprinkled with coarse sea salt.',
            'image_url': 'static/images/Chocolate_Chip.png', 
            'Availability':'In Stock!'
        },
        'pricing': {'1 Cookie': f"{5:.2f}",
              '4 Cookies': f"{18:.2f}",
              '6 Cookies': f"{25:.2f}",
              '12 Cookies': f"{40:.2f}"},
    },
    {
        'name': 'Biscoff Cookie',
        'details': {
            'description': 'Brown sugar cookie made with crushed Biscoff biscuits stuffed with Biscoff cookie butter.',
            'image_url': 'static/images/Biscoff_Butter.PNG', 
            'Availability':'In Stock!'
        },
        'pricing': {'1 Cookie': f"{5:.2f}",
              '4 Cookies': f"{18:.2f}",
              '6 Cookies': f"{25:.2f}",
              '12 Cookies': f"{40:.2f}"},       
    },
    {
        'name': 'S’mores Cookie',
        'details': {
            'description': 'Chocolate chip cookie stuffed with a graham cracker, Hershey’s chocolate, and a jumbo marshmallow. Topped with mini marshmallows, chopped milk chocolate bar pieces, and graham cracker crumbs.',
            'image_url': 'static/images/Smores.png', 
            'Availability':'In Stock!'
        },
        'pricing': {'1 Cookie': f"{5:.2f}",
              '4 Cookies': f"{18:.2f}",
              '6 Cookies': f"{25:.2f}",
              '12 Cookies': f"{40:.2f}"},
    },
    {
        'name': 'Fruity Pebbles Cookie',
        'details': {
            'description': 'A buttery, soft cookie loaded with roasted pecans and a hint of vanilla, offering a delightful crunch in every bite.',
            'image_url': 'static/images/Fruity_Pebbles.png', 
            'Availability':'In Stock!'
        },
        'pricing': {'1 Cookie': f"{5:.2f}",
              '4 Cookies': f"{18:.2f}",
              '6 Cookies': f"{25:.2f}",
              '12 Cookies': f"{40:.2f}"},
    },
    {
        'name': 'Cranberry Oatmeal Cookie',
        'details': {
            'description': 'Moist oatmeal spice cookie mixed with dried cranberries and white chocolate chips. Optional macadamia nuts.',
            'image_url': 'static/images/Oatmeal_Cranberry.png', 
            'Availability':'In Stock!'            

        },
        'pricing': {'1 Cookie': f"{5:.2f}",
              '4 Cookies': f"{18:.2f}",
              '6 Cookies': f"{25:.2f}",
              '12 Cookies': f"{40:.2f}"},
    },
    {
        'name': 'White Chocolate Macadamia Cookie',
        'details': {
            'description': 'Brown sugar cookie made with freshly chopped buttery rich macadamia nuts and white chocolate chips.',
            'image_url': 'static/images/White_Chocolate_Macadamia.png', 
            'Availability':'In Stock!'
        },
        'pricing': {'1 Cookie': f"{5:.2f}",
              '4 Cookies': f"{18:.2f}",
              '6 Cookies': f"{25:.2f}",
              '12 Cookies': f"{40:.2f}"},
    },
    {
        'name': 'Red Velvet Cookie',
        'details': {
            'description': 'Luscious moist red velvet cake cookie mixed with white chocolate chips.',
            'image_url': 'static/images/Red_Velvet.PNG', 
            'Availability':'In Stock!'
        },
        'pricing': {'1 Cookie': f"{5:.2f}",
              '4 Cookies': f"{18:.2f}",
              '6 Cookies': f"{25:.2f}",
              '12 Cookies': f"{40:.2f}"},
    },
    {
        'name': 'Pumpkin Snickerdoodle Cookie',
        'details': {
            'description': 'Brown butter pumpkin spice cookie covered in cinnamon sugar.',
            'image_url': 'static/images/Pumpkin_Snickerdoodle.png', 
            'Availability':'In Stock!'
        },
        'pricing': {'1 Cookie': f"{5:.2f}",
              '4 Cookies': f"{18:.2f}",
              '6 Cookies': f"{25:.2f}",
              '12 Cookies': f"{40:.2f}"},

    },
    {
        'name': 'Apple Pie Cookie',
        'details': {
            'description': 'Soft vanilla spiced cookie with buttery pie crust pieces and freshly chopped juicy honeycrisps.',
            'image_url': 'static/images/Apple_Pie.png', 
            'Availability':'In Stock!'
        },
        'pricing': {'1 Cookie': f"{5:.2f}",
              '4 Cookies': f"{18:.2f}",
              '6 Cookies': f"{25:.2f}",
              '12 Cookies': f"{40:.2f}"},
    },
    {
        'name': 'M&M’s® Cookie',
        'details': {
            'description': 'Brown sugar chocolate chip cookie made with M&M’s® milk chocolate candies.',
            'image_url': 'static/images/M&M\'s.png', 
            'Availability':'In Stock!'
        },
        'pricing': {'1 Cookie': f"{5:.2f}",
              '4 Cookies': f"{18:.2f}",
              '6 Cookies': f"{25:.2f}",
              '12 Cookies': f"{40:.2f}"},
    },
    {
        'name': 'Peanut Butter Cookie',
        'details': {
            'description': 'The perfect peanut butter cookie. Soft, chewy interior. Crispy exterior.',
            'image_url': 'static/images/Peanut_Butter.png',
            'Availability':'In Stock!'
        },
        'pricing': {'1 Cookie': f"{5:.2f}",
              '4 Cookies': f"{18:.2f}",
              '6 Cookies': f"{25:.2f}",
              '12 Cookies': f"{40:.2f}"},
    }
    ]


# Main page is menu page for now
@app.route('/')
def menu_page():
    return render_template('menu.html', menu_items=menu_items)

# Redirects user to cookies page
@app.route('/cookies')
def cookies_page():
    return render_template('menu.html', menu_items=menu_items) 

# Indicates that script is being executed directly, good practice. meaning this will run when running "flask app" on terminal.
if __name__ == '__main__': # Checks if script is being run directly
    app.run(host="0.0.0.0", port=5000, debug=True) # server starts in debug mode