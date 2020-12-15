import azure.functions as func
import pymongo
import json
import os
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python createAdvertisement trigger function processed a request.')
    
    request = req.get_json()
    
    if request:

        try:

            url =  os.environ['MongoDbUdacityExam2'] 
            client = pymongo.MongoClient(url)
            database = client['udacity-exam-2-db']
            collection = database['advertisements']
            
            logging.info(request) 

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except:

            logging.info('----------Failed--------')
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )