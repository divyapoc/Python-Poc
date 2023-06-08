from flask import Flask, render_template

inv = Flask(__name__)
@inv.route('/')
def func():
    tech = [{"invention": "Electricity", "inventor": "Benjamin Franklin"},
            {"invention": "Electric Bulb", "inventor": "Thomas Edison"},
            {"invention": "Mobile Phone" , "inventor":"Martin Cooper" },
            {"invention":"Refrigerator","inventor":"William Cullen"}]
    return render_template('invention.html', tech=tech)

if __name__ == '__main__':
    inv.run(port=6001)