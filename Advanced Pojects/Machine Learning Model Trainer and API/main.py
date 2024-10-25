# This project trains machine learning models and serves them via an API.
# Implement the code here

from flask import Flask, request
import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Train and save the model
iris = load_iris()
model = LogisticRegression()
model.fit(iris.data, iris.target)
pickle.dump(model, open('model.pkl', 'wb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    model = pickle.load(open('model.pkl', 'rb'))
    prediction = model.predict([data])
    return {'prediction': int(prediction[0])}

# Run Flask app
if __name__ == '__main__':
    app.run()
