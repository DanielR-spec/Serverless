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

        #data = json.loads(event)
        data = event
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

        # Create connection with RDS Cluster
            conn = get_redshift_con()

        # Set up the cursor and excecute query
            cursor: redshift_connector.Cursor = conn.cursor()
            table = "execution_time_logs_dev"

        # Get unique id 
            get_id = f"SELECT MAX(id) from {table}"
            cursor.execute(get_id)
            max_id = cursor.fetchone()[0]
            conn.commit()
            if max_id is None:
            	max_id = 1
            else:
            	max_id = max_id + 1

        # Construct the json instert object
            insert = {
                "id":max_id,
                "user_id":body["user_id"],
                "user_email":body["user_email"],
                "first_name":body["user_name"],
                "last_name":body["user_last"],
                "organization_id":body["org_id"],
                "organization_name":body["org_name"],
                "request_type":body["request_type"],
                "request_path":body["request_path"],
                "request_timestamp":body["request_timestamp"],
                "response_timestamp":body["response_timestamp"],
                "duration":body["duration"],
                "response_status":body["response_status"],
                "device_type":body["device_type"],
                "country_id":body["user_country_id"],
                "time_zone":body["user_time_zone"],
                "error":body["error"]
            }

        # Convert the JSON data to a list of values
            json_list = list(insert.values())
            

        # Construct the SQL statement to insert data into the Redshift table
            insert_sql = f"INSERT INTO {table} (id,user_id,user_email,first_name,last_name,organization_id,organization_name,request_type,request_path,request_timestamp,response_timestamp,duration,response_status,device_type,country_id,time_zone,error) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        # Execute the insert statement to load data into the Redshift table
            cursor.execute(insert_sql, json_list)
            conn.commit()

        # Close cursor index & connection
            cursor.close()
            conn.close()

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
        # print(ErrorLine)
        return 'Exited with status code 401: service not found' + ErrorLine
'''
event = {
  'requestContext': {
    'http': {
      'method': 'POST'
    }
  },
  'body': {
    'user_id': 34,
    'user_email': 'juan@motivy.co',
    'user_name': 'Juan avalatina',
    'user_last': 'Brown',
    'org_id': 2,
    'org_name': 'PBD',
    'request_type': 'POST',
    'request_path': '/login',
    'request_timestamp': '2023-05-16T06:45:37.141Z',
    'response_timestamp': '2023-05-16T06:45:37.332Z',
    'duration': 101,
    'response_status': True,
    'device_type': 'Mobil',
    'user_country_id': 2,
    'user_time_zone': 'America/Los_Angeles',
    'error': 'Exited with status code 200'
  }
}
lambda_handler(event,None)
'''
