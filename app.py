from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_bcrypt import generate_password_hash, check_password_hash

from DB import User, Cars, Bikes, Trucks

app = Flask(__name__)
app.secret_key = "123124125126TREES"


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        userName = request.form["u_name"]
        userEmail = request.form["u_email"]
        userPassword = request.form["u_password"]
        encryptedUserPassword = generate_password_hash(userPassword)
        User.create(name=userName, email=userEmail, password=encryptedUserPassword)

        flash("ACCOUNT CREATED SUCCESSFULLY")

    return render_template('signup.html')


@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userEmail = request.form["u_email"]
        userPassword = request.form["u_pass"]

        try:
            user = User.get(User.email == userEmail)
            encryptedPassword = user.password

            if check_password_hash(encryptedPassword, userPassword):
                flash("YOU HAVE LOGGED IN SUCCESSFULLY")

                session["loggedIn"] = True
                session["userName"] = user.name
                flash("CORRECT EMAIL/PASSWORD")
                return redirect(url_for("home"))

        except:
            flash("WRONG EMAIL/PASSWORD")

    return render_template("login.html")


@app.route("/home")
def home():
    if not session["loggedIn"]:
        return redirect(url_for("login"))

    return render_template("home.html")


@app.route("/addcars", methods=["GET", "POST"])
def addcars():
    if not session["loggedIn"]:
        return redirect(url_for("login"))

    if request.method == "POST":
        carMake = request.form["make"]
        carModel = request.form["model"]
        carYom = request.form["yom"]
        carPower = request.form["power"]
        carPrice = request.form["price"]
        Cars.create(make=carMake, model=carModel, yom=carYom, power=carPower, price=carPrice)

    return render_template("addcars.html")


@app.route("/addbikes", methods=["GET", "POST"])
def addbikes():
    if not session["loggedIn"]:
        return redirect(url_for("login"))

    if request.method == "POST":
        bikeMake = request.form["make"]
        bikeModel = request.form["model"]
        bikeYom = request.form["yom"]
        bikePower = request.form["power"]
        bikePrice =  request.form["price"]
        Bikes.create(make=bikeMake, model=bikeModel, yom=bikeYom, power=bikePower, price=bikePrice)

    return render_template("addbikes.html")


@app.route("/addtrucks", methods=["GET", "POST"])
def addtrucks():
    if not session["loggedIn"]:
        return redirect(url_for("login"))

    if request.method == "POST":
        truckMake = request.form["make"]
        truckModel = request.form["model"]
        truckYom = request.form["yom"]
        truckPower = request.form["power"]
        truckPrice = request.form["price"]
        Trucks.create(make=truckMake, model=truckModel, yom=truckYom, power=truckPower, price=truckPrice)

        flash("Updated")

    return render_template("addtrucks.html")


@app.route('/update/<int:id>', methods=["GET", "POST"])
def updatebikes(id):
    if not session.get("loggedIn"):
        return redirect(url_for("login"))
    bike = Bikes.get(Bikes.id == id)

    if request.method == "POST":
        updatedBikeMake = request.form["make"]
        updatedBikeModel = request.form["model"]
        updatedBikeYom = request.form["yom"]
        updateBikePrice = request.form["price"]
        updatedBikePower = request.form["power"]
        bike.make = updatedBikeMake
        bike.model = updatedBikeModel
        bike.yom = updatedBikeYom
        bike.price = updateBikePrice
        bike.power = updatedBikePower

        bike.save()

        flash("Bike details updated")
        return redirect(url_for("bikes"))
    return render_template("updatedbikes.html")


@app.route('/update/<int:id>', methods=["POST", "GET"])
def updatecars(id):
    if not session.get("loggedIn"):
        return redirect(url_for("login"))
    car = Cars.get(Cars.id == id)

    if request.method == "POST":
        updatedCarMake = request.form["make"]
        updatedCarModel = request.form["model"]
        updatedCarYom = request.form["yom"]
        updatedCarPrice = request.form["price"]
        updatedCarPower = request.form["power"]
        car.make = updatedCarMake
        car.model = updatedCarModel
        car.yom = updatedCarYom
        car.price = updatedCarPrice
        car.power = updatedCarPower

        car.save()

        flash("Car details updated")
        return redirect(url_for("cars"))
    return render_template("updatedcars.html")


@app.route('/update/<int:id>', methods=["POST", "GET"])
def updatetrucks(id):
    if not session.get("loggedIn"):
        return redirect(url_for("login"))
    truck = Trucks.get(Trucks.id == id)

    if request.method == "POST":
        updatedTruckMake = request.form["make"]
        updatedTruckModel = request.form["model"]
        updatedTruckYom = request.form["yom"]
        updatedTruckPrice = request.form["price"]
        updatedTruckPower = request.form["power"]
        truck.make = updatedTruckMake
        truck.model = updatedTruckModel
        truck.yom = updatedTruckYom
        truck.price = updatedTruckPrice
        truck.power = updatedTruckPrice

        truck.save()

        flash("Truck details updated")
        return redirect(url_for("trucks"))
    return render_template("updatedtrucks.html")


@app.route('/delete/<int:id>')
def deletebikes(id):
    if not session.get("loggedIn"):
        return redirect(url_for("login"))
    Bikes.delete().where(Bikes.id == id).execute()
    flash("Bike deleted successfully")
    return redirect(url_for("bikes"))


@app.route('/delete/<int:id>')
def deletecars(id):
    if not session.get("loggedIn"):
        return redirect(url_for("login"))
    Cars.delete().where(Cars.id == id).execute()
    flash("Car deleted successfully")
    return redirect(url_for("addcars"))


@app.route('/delete/<int:id>')
def deletetrucks(id):
    if not session.get("loggedIn"):
        return redirect(url_for("login"))
    Trucks.delete().where(Trucks.id == id).execute()
    flash("Truck deleted successfully")
    return redirect(url_for("addtrucks"))


@app.route('/bikes')
def bikes():
    if not session["loggedIn"]:
        return redirect(url_for("login"))

    bike = Bikes.select()
    return render_template("bikes.html", bikes=bikes)


@app.route('/cars')
def cars():
    if not session["loggedIn"]:
        return redirect(url_for("login"))

    car = Cars.select()
    return render_template("cars.html", cars=cars)


@app.route('/trucks')
def trucks():
    if not session["loggedIn"]:
        return redirect(url_for("login"))

    truck = Trucks.select()
    return render_template("trucks.html", trucks=trucks)


if __name__ == '__main__':
    app.run(debug=True)
