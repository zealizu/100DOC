from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def to_dict(self):
        cafe = {column.name:getattr(self,column.name) for column in self.__table__.columns}
        return cafe
with app.app_context():
    db.create_all()

def str_to_bool(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in ['true', '1', 'yes']
    return False  # Or raise an error if you want strict handling

@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random():
    cafes = db.session.execute(db.select(Cafe))
    all_cafes = cafes.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe= {
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })
    

@app.route("/all")
def all():
    cafes= db.session.execute(db.select(Cafe))
    all_cafes = cafes.scalars().all()
    cafes=[]
    for cafe in all_cafes:
        cafes.append(cafe.to_dict())
    return jsonify(cafes)
    
    
@app.route("/search")
def search():
    try:
        location = request.args.get("loc").title()
        cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    except AttributeError:
        return jsonify(error="Bad request"),400
# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name= request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url= request.form.get("img_url"),
        location= request.form.get("location"),
        seats= request.form.get("seats"),
        has_toilet= str_to_bool(request.form.get("has_toilet")),
        has_wifi= str_to_bool(request.form.get("has_wifi")),
        has_sockets= str_to_bool(request.form.get("has_sockets")),
        can_take_calls= str_to_bool(request.form.get("can_take_calls")),
        coffee_price= request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    update_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == int(cafe_id))).scalar()
    try:
        update_cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(success="Successfully updated the price"),200
    except AttributeError: 
        return jsonify(error={"Not Found": "Sorry the cafe with that id was not found in the database"}),404
    

# HTTP DELETE - Delete Record

@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.get(Cafe, cafe_id)
        if cafe is None:
            return jsonify(error={"Not Found": "Sorry, no cafe with that ID"}), 404

        db.session.delete(cafe)
        db.session.commit()
        return jsonify(success="Successfully deleted the cafe"), 200
    else:
        return jsonify(error="Sorry that's not allowed, make sure you have the correct api-key"),403
        
    


if __name__ == '__main__':
    app.run(debug=True)
