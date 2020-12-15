import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python getAdvertisement trigger function processed a request.')

    db_id = req.params.get('id')

    if not db_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            db_id = req_body.get('id')
    
    if db_id:

        logging.info(db_id)   
        
        try:
            url =  os.environ['MongoDbUdacityExam2'] 
            client = pymongo.MongoClient(url)
            database = client['udacity-exam-2-db']
            collection = database['advertisements']

            event_id = db_id
            result = collection.find_one({"_id": ObjectId(event_id)})
            result = dumps(result)
            logging.info('----------result--------')

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=400)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)