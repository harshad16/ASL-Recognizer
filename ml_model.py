import boto3
from boto3.session import Session
import csv

class ML_Model():
    def __init__(self,filename):
        self.filename=filename

    def run(self):
        session = Session(aws_access_key_id='', aws_secret_access_key='')
        machinelearning = session.client('', region_name='')
        model_id = ''
        try:

            model = machinelearning.get_ml_model(MLModelId=model_id)
            prediction_endpoint = model.get('EndpointInfo').get('EndpointUrl')

            a = []
            with open(self.filename,'r') as f:
                record_str = csv.reader(f)
                for r in record_str:
                    a.append(r)

            record={}
            for i in range(len(a[0])):
                record[a[0][i]]=a[1][i]
            print "record",record
            response = machinelearning.predict(MLModelId=model_id, Record=record, PredictEndpoint=prediction_endpoint)
            label = response.get('Prediction').get('predictedLabel')

            return label

        except Exception as e:
            print(e)