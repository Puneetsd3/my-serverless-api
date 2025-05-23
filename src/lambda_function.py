import json
import boto3
import uuid
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def create_note(event, context):
    body = json.loads(event['body'])
    note_id = str(uuid.uuid4())
    title = body.get('title')
    content = body.get('content')

    item = {'id': note_id, 'title': title, 'content': content}
    table.put_item(Item=item)

    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Note created', 'note': item})
    }

def get_notes(event, context):
    result = table.scan()
    return {
        'statusCode': 200,
        'body': json.dumps(result['Items'])
    }

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        return create_note(event, context)
    elif event['httpMethod'] == 'GET':
        return get_notes(event, context)
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'message': 'Method Not Allowed'})
        }
