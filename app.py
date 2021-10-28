from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

model = pickle.load(open('regression_model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predictApi', methods=['POST'])
def predict():
    data1 = request.json['Months']
    data2 = request.json['Temp']
    data3 = request.json['RH']
    data4 = request.json['Protein']
    data5 = request.json['Oil']
    data6 = request.json['starch']
    data7 = request.json['Ash']
    data8 = request.json['DM']
    data9 = request.json['CrudeFib']
    data10 = request.json['IC']

    arr = np.array([[data1, data2, data3, data4, data5,
                     data6, data7, data8, data9,data10]])
    
    pred = model.predict(arr)
    pred = np.array(pred)

    pred_dict = {
        'MoistureContent': round(pred[0][0], 4),
        'BacterialCount': round(pred[0][1], 4),
        'FungalCount': round(pred[0][2], 4),
        'SeedViability': round(pred[0][3], 4)
        }

    return jsonify(pred_dict)


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']

    arr = np.array([[data1, data2, data3, data4, data5,
                     data6, data7, data8, data9,data10]])
    pred = model.predict(arr)
    pred = np.array(pred)

    pred_dict = {
        'Moisture content': round(pred[0][0], 4),
        'Bacterial count': round(pred[0][1], 4),
        'Fungal count': round(pred[0][2], 4),
        'Seed Viability': round(pred[0][3], 4)
        }

    return render_template('home.html', 
                               prediction_text='The seed quality variables : {}'.format(pred_dict))


if __name__ == "__main__":
    app.run(debug=True) 