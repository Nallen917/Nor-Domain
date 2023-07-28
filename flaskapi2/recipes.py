from flask import Flask, render_template, request

app = Flask(__name__)

# Here are my Sample recipes data
recipes = {
    'chicken': [
        'Grilled Chicken',
        'Chicken Curry',
        'Chicken Alfredo'
    ],
    'vegetarian': [
        'Vegetable Stir Fry',
        'Vegetarian Pizza',
        'Vegetable Curry'
    ],
    'caribbean': [
        'Jerk Chicken',
        'Caribbean Rice and Beans',
        'Plantains with Black Bean Sauce'
    ]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recipe_type = request.form['recipe_type']
        # recipe_type var will be equal to either "chicken", "vegetarian", or "carribbean"
        matching_recipes = recipes.get(recipe_type, [])
 
        return render_template('recipes.html', recipe_type=recipe_type, recipes=matching_recipes)
                                                           # "chicken"          list of recipes []
    return render_template('form.html')

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=2224)

