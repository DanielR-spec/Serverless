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

        http_method = event["requestContext"]["http"]["method"]

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

            body = json.loads(event['body'])
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

        # print(responseObject)
        return responseObject
    except Exception as e:
        ErrorLine = str(e)
        # ev = str(event)
        # print(ev)
        return 'Exited with status code 401: service not found' + ErrorLine

#event = {
#    "requestContext":{
#      "http":{
#         "method":"SAD",
#      }
#   },
#   "body":"{\n   \"httpMethod\":\"POST\",\n   \"body\":{\n\t\"transactionId\":1,\n\t\"type\":\"HTTP/1\",\n    \"amount\":128\n}\n}"
#}
#lambda_handler(event,None)
