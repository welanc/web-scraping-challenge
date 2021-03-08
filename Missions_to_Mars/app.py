from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

   # Page title 
    title = "Mission to Mars"

    # Return template and data
    return render_template("index.html", title=title)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)  

    # Find one record of data from the mongo database
    retrieved_data = mongo.db.collection.find_one()

    # Redirect back to home page
    return render_template("data.html", mars_info=retrieved_data)


if __name__ == "__main__":
    app.run(debug=True)
