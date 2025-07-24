from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
from datetime import datetime
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField(label="Cafe location on Google map(URL)", validators=[DataRequired(), URL()])
    open_time = TimeField(label="Open Time eg(8AM)", validators=[DataRequired()])
    close_time = TimeField(label="Close Time eg(4:30pm)", validators=[DataRequired()])
    coffee = SelectField(label="Coffee Rating", choices=["✘", "☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️"], validators=[DataRequired()])
    wifi = SelectField(label="WIFI Strenght Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪"], validators=[DataRequired()])
    power = SelectField(label="Power Outlet Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌"])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        open_time = form.open_time.data.strftime("%I:%M %p")
        close_time = form.close_time.data.strftime("%I:%M %p")
        with open(file="100DOC/coffee/cafe-data.csv", mode="a", newline='') as csv_file:
            csv.writer(csv_file).writerow([form.cafe.data, form.location.data, open_time, close_time, form.coffee.data, form.wifi.data, form.power.data])
        return redirect(url_for('cafes'))
    else:
        return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('100DOC/coffee/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
