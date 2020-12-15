import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import json
import os
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python updateAdvertisement trigger function processed a request.')

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            url =  os.environ['MongoDbUdacityExam2'] 
            client = pymongo.MongoClient(url)
            database = client['udacity-exam-2-db']
            collection = database['advertisements']
            
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            logging.info('----------result--------')

            return func.HttpResponse(status_code=200)
        except:
            logging.info('----------Failed--------')
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

