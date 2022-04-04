from fastapi import FastAPI
from predict.prediction import predictor
from preprocessing.cleaning_data import preprocess
import os

app = FastAPI()

@app.get('/')
async def home():
    msg = 'alive'
    return(msg)

@app.get('/house')
async def predict(): 
    msg = 'Working'
    return(msg)


@app.post('/house')
async def house_api(): 
    house_json = request.json
    df = preprocess(house_json)
    return str(predictor(df))
    
 
'''If running a FlaskAPI, the script bellow is neccesary 
    if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host="0.0.0.0", threaded=True, port=port)'''