from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017/mars_db'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
db = client.mars_db

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    info_dict = db.info.find_one()
    return render_template("index.html", info_dict=info_dict)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a dictionary
    mars_dict = scrape_mars.scrape()
    
    # Update the Mongo database with scraped info
    db.info.update_one({}, {"$set":mars_dict}, upsert=True)
    
    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
