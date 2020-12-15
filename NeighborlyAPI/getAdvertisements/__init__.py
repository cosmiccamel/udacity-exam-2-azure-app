import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python getAdvertisements trigger function processed a request.')

    try:
        url =  os.environ['MongoDbUdacityExam2'] 
        client = pymongo.MongoClient(url)
        database = client['udacity-exam-2-db']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

