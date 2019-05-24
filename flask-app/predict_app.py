
import base64
import numpy as np
import io
import keras
from keras import backend as K
from keras.models import Sequential
from keras.models import load_model
from flask import request
from flask import jsonify
from flask import Flask
import pickle




pickle_in = open("X_train.pickle","rb")
X_train = pickle.load(pickle_in)




from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train  = sc.fit_transform(X_train)
print(sc)

app=Flask(__name__)

def get_model():
	global model
	model= load_model('model1_99.keras')
	print("Model Loaded")
print("Loading Model")
get_model()

@app.route("/predict",methods["POST"])


def predict():
	message = request.get_json(force = True)
	encoded = message['symp']
	decoded = base64.b64decode(encoded)

	x = np.array(decoded)
	x = x.reshape(len(x),-1)
	x = sc.transform(x)

	pred = model.predict(x).astype(int)

	if(pred>=0.5):
		result ={	"prediction" : "Malignant" }

	else :
		result ={	"prediction" : "Benign" }

	return jasonify(result)

		

print("Loading Keras Model...")



