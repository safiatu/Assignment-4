from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

def findinfo(cname):
    totalresult = []
    country = cname
    url = "https://www.worldometers.info/coronavirus/country/{countryname}/".format(countryname = country)

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.find_all('div',class_="maincounter-number")
        for i in result:
            totalresult.append(i.find("span").text)
    else:
        totalresult.append("No Result")
    return totalresult

app = Flask(__name__)

@app.route("/", methods =["GET"])
def cases():

    country = request.args.get("country")
    try:
        return jsonify({"Total cases ":findinfo(country)[0],
        "Total Death ":findinfo(country)[1],
        "Total Recovered ":findinfo(country)[2]})
    
    except:
        return jsonify({'No data found':" "})



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__': 
    app.run(debug=True)