# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, render_template, request, jsonify
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, StandardScaler
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('./model/model.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
       
        print(request.form)
       
        print(request.form["mileage"])
        print(request.form["my"])
        
        
       # data = np.reshape(data, (1,-1))
        
        stats1 = {
                "1999":0,
                "2000":1,
                "2001":2,
                "2002":3,
                "2003":4,
                "2004":5,
                "2005":6,
                "2006":7,
                "2007":8,
                "2008":9,"2009":10,"2010":11,"2011":12,"2012":13,"2013":14,"2014":15,"2015":16,"2016":17, "2017":18
        }

        stats4 = {
               

               0: "1999",
               1: "2000",
               2: "2001",
                3:"2002",
                4:"2003",
                5:"2004",
               6: "2005",
                7:"2006",
               8: "2007",
                9:"2008",10:"2009",11:"2010",12:"2011",13:"2012",14:"2013",15:"2014",16:"2015",17:"2016", 18:"2017"
        }
        year = stats1[request.form["my"]]


       # stats5 = {

         #       "LE":1,
         #       "EX":2,
         #       "S":3,
          #      "EX-L":4,
           #     "LX":5,
           #     "Sedan":6,
            #    "L":7,
            #    "New Listing":8,
             #   "CE":9,
             #   "SES":10,
            #    "SEL":11,
             #   "ST":12,
              #  "XLE":13,
            #    "XRS":14

       # }

        #stats6 = {

           #     1:"LE",
           #     2:"EX",
             #   3:"S",
             #   4:"EX-L",
             #   5:"LX",
               # 6:"Sedan",
              #  7:"L",
              #  8:"New Listing",
             #   9:"CE",
               # 10:"SES",
             #   11:"SEL",
               # 12:"ST",
              #  13:"XLE",
             #   14:"XRS"

       # }

        #brand = stats5[request.form["origin"]]

        stats2 = {
                "Ford":1,
                "Honda CRV":2,
                "Toyota Corolla":3
        }
        stats3 = {
                1:"Ford",
                2:"Honda CRV",
                3:"Toyota Corolla"
        }
        brand = stats2[request.form["origin"]]
        print('origin',request.form["origin"])

        # data = [[float(request.form['R&D']), float(request.form['admin']),float(request.form["marketing"]),request.form["location"]]]
        data = [[int(request.form['mileage']),year,brand]]
    


        print("DAtA :      ")
        print(data)
        
      
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict(data)
        print(prediction)

        # Take the first value of prediction
        output = prediction[0]

        return render_template("results.html", output=output, exp=data)

if __name__ == '__main__':
    app.run(debug=False)
