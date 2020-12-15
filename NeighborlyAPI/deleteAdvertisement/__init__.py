import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import os
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python deleteAdvertisement trigger function processed a request.')


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
            logging.info(event_id)  
            result = collection.delete_one({"_id": ObjectId(event_id)})

            logging.info('----------Delete Record--------')

            return func.HttpResponse("")

        except:
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
