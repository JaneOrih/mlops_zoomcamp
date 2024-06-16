load pickle

with open('lin_reg.bin', 'rb') as f_out:
    (model,dv)= pickle.load(f_out)



def predict(data):
    data['duration']= data['tpep_dropoff_datetime']-data['tpep_pickup_datetime']
    data['duration']=data['duration'].apply(lambda x: x.total_seconds()/60)
    new_data=data[(data['duration']>= 1) & (data['duration']<= 60)]
    variables=new_data[['PULocationID' ,'DOLocationID']].astype(str)
    data_dict=variables.to_dictconda(orient='records')
    return model.predict(dv.transform(data_dict))