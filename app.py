# -*- coding: utf-8 -*-
"""
Created on Fri Mai 06 21:51:19 2022
@author: win10
"""

import uvicorn
from fastapi import FastAPI
from CropData import CropData
from fastapi.middleware.cors import CORSMiddleware
import pickle
import json
# 2. Create the app object
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000/",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
pickle_in = open("model_pickle.pickle","rb")
classifier=pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Crop pediction app'}

@app.get('/home')
def index():
    return {'message': 'this is home'}


@app.post('/predict/')
def predict_cropnote(data:CropData):
    data_object = data.dict()
    nitrogen = data_object['nitrogen']
    phosphorius = data_object['phosphorius']
    potassium = data_object['potassium']
    temperature = data_object['temperature']
    humidity =data_object['humidity']
    ph =data_object['ph']
    rainfall =data_object['rainfall']
    
   # print(classifier.predict([[nitrogen,phosphorius,potassium,temperature,humidity,ph,rainfall]]))
    prediction = classifier.predict([[nitrogen,phosphorius,potassium,temperature,humidity,ph,rainfall]])
    return {
        'prediction': prediction[0]
    }
      
      

#    Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload
