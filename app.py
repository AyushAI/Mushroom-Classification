from flask import Flask, render_template, request
import pickle
import numpy as np

def Mushroom_Predictor(result_data):
    prediction = np.array(result_data).reshape(1, 5)
    load_model = pickle.load(open('decision_tree_model.pkl', 'rb'))
    result = load_model.predict(prediction)
    return result[0]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    result_data = request.form.to_dict()
    result = Mushroom_Predictor(list(result_data.values()))
    if int(result) == 1:
        prediction = 'Edible'
    else:
        prediction = 'Poisonous'
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run()
