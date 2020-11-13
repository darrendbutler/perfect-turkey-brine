import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    weight = req.params.get('weight')
    
    if not weight:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            weight = req_body.get('weight')


    if weight:
        #Create recipe dictionary
        recipe = {
        "brine time" : str( round(int (weight) * 2.4, 2)) + " hours",
        "salt" : str(round(int (weight) * 0.05, 2)) + " cups",
        "water" : str(round(int (weight) * 0.06, 2)) + " gallons",
        "brown sugar" : str( round(int (weight) * 0.13, 2) ) + " cups",
        "shallots" : str( round(int (weight) * 0.2, 2)),
        "garlic" : str( round(int (weight) * 0.4, 2)) + " cloves",
        "whole peppercorns" : str( round (int (weight) * 0.13, 2)) + " tablespoons",
        "dried juniper berries" : str( round(int (weight) * 0.13, 2)) + " tablespoons",
        "fresh rosemary" : str( round(int (weight) * 0.13, 2)) + " tablespoons",
        "thyme" : str( round(int (weight) * 0.06, 2)) + " tablespoons",
        "roast time" : str(round(int (weight) * 15, 2)) + " minutes",       
        }

        recipe_json = json.dumps(recipe)

        return func.HttpResponse(recipe_json, status_code=200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a weight in the query string or in the request body for a personalized response.",
             status_code=200
        )
