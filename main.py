from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random, os

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

cafes=[]
ApiKey= os.environ.get("APIKEY")

## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr (self, column.name)
        return dictionary
        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr (self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# All route
@app.route("/all")
def get_all_coffees():
    with app.app_context ():
        result = db.session.execute (db.select (Cafe))
        all_cafes = result.scalars().all()
    # List Comprehension
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

# Random route
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    #Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=random_cafe.to_dict())

# Search route
@app.route("/search")
def search_location():
    location = request.args.get("loc")
    with app.app_context ():
        result = db.session.execute (db.select (Cafe).where (Cafe.location == location))
        all_cafes = result.scalars().all()
    if not all_cafes:
        return jsonify({
            "error": {
                "Not Found" : " Sorry, we don't have a coffee at that location."
            }
        })
    else:
     return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])

# Add route
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# Update price route
# Updating the price of a cafe based on a particular id:
# http://127.0.0.1:8000/update-price/CAFE_ID?new_price=$5.67
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        ## Just add the code after the jsonify method. 200 = Ok
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        #404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

# Delete a Cafe based on a particular id
# http://127.0.0.1:8000/report-closed/CAFE_ID?api-key=TopSecretKey
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_closed_cafe(cafe_id):
    cafe = db.get_or_404 (Cafe, cafe_id)
    api_key = request.args.get ("api-key")
    if api_key==os.environ.get("APIKEY"):
        if cafe:
            db.session.delete (cafe)
            db.session.commit ()
            return  jsonify(response={"success": "Successfully deleted Cafe."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify (error={"Not Found": "Sorry that's not allowed, make sure you have the correct api-key."}), 403

if __name__ == '__main__':
    app.run(debug=True, port=8000)
