# Import library
import redshift_connector
import json
import os

HOST = os.environ['DBHost']
USERNAME = os.environ['DBUser']
PASSWORD = os.environ['DBPassword']
PORT = int(os.environ['DBPort'])
DBNAME = os.environ['DBName']

def get_redshift_con(password=PASSWORD,
                     user=USERNAME,
                     host=HOST,
                     port=PORT,
                     dbname=DBNAME):
    return redshift_connector.connect(database=dbname,host=host,port=port,user=user,password=password)


def lambda_handler(event, context):

    # TODO implement

    try:

    # Caputer request event

        data = json.loads(event)
        http_method = data["requestContext"]["http"]["method"]
        

    # Construct Object & the body of the response

        transactionResponse = {}
        responseObject = {}

    # Review request type and return acording response

        if http_method == 'GET':

        # Construct http response object

            transactionResponse['message'] = 'Hello from HTTP GET!'

            responseObject['statusCode'] = 200
            responseObject['headers'] = {}
            responseObject['headers']['Content-Type'] = \
                'application/json'
            responseObject['body'] = json.dumps(transactionResponse)
        
        elif http_method == 'POST':

        # Construct http response object
            body = data['body']

            transactionResponse['message'] = 'Hello from HTTP POST!'

            responseObject['statusCode'] = 200
            responseObject['headers'] = {}
            responseObject['headers']['Content-Type'] = \
                'application/json'
            responseObject['body'] = json.dumps(transactionResponse)
            responseObject['data'] = body
        
        else:

        # Error Handling

            transactionResponse['message'] = \
                'Bad Request, Invalid Lambda Invocation!'

            responseObject['statusCode'] = 400
            responseObject['headers'] = {}
            responseObject['headers']['Content-Type'] = \
                'application/json'
            responseObject['body'] = json.dumps(transactionResponse)

        return responseObject
    except Exception as e:
        ErrorLine = str(e)
        return 'Exited with status code 401: service not found' + ErrorLine

# event = "{\"requestContext\":{\"http\":{\"method\":\"POST\"}},\"body\":{\"request_timestamp\":\"2023-05-15T05:45:37.141Z\",\"response_timestamp\":\"2023-05-15T05:45:37.232Z\",\"duration\":91,\"request_type\":\"POST\",\"request_path\":\"/login\",\"user_id\":32,\"user_email\":\"aprego-local@motivy.co\",\"user_name\":\"Alberto Anitalavalatina\",\"user_last\":\"lorem itsum dolor sit amet\",\"user_country_id\":1,\"user_time_zone\":\"America/Los_Angeles\",\"org_id\":1,\"org_name\":\"Test Org 1\",\"response_status\":true,\"error\":\"Exited with status code 200\"}}"
# lambda_handler(event,None)
