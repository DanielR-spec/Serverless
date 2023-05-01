import json

def lambda_handler(event, context):
    message = "Hello, world!"
    messageb = "this is another message"
    return {
        'statusCode': 200,
        'body': json.dumps(message+messageb)
    }
