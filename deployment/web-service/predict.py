import pickle
from flask import Flask, jsonify, request
app=Flask('duration_prediction')

with open('lin_reg.bin', 'rb') as f_out:
    (model,dv)= pickle.load(f_out)



def predict(data):
    data=dv.transform(data)
    prediction=model.predict(data)
    return prediction[0]


@app.route('/predict', methods=['POST'])
def pred_endpoint():
    ride=request.get_json()
    pred=predict(ride)
    result={
        'duration': pred
    }
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True, host= '0.0.0.0', port=9696)