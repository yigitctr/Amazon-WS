import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def lambda_handler(event, context):
    item_id = str(uuid.uuid4())
    item_data = json.loads(event['body'])
    item_data['itemId'] = item_id

    table.put_item(Item=item_data)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item created', 'itemId': item_id})
    }
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def lambda_handler(event, context):
    item_id = event['pathParameters']['id']

    response = table.get_item(Key={'itemId': item_id})
    item = response.get('Item')

    if not item:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Item not found'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def lambda_handler(event, context):
    item_id = event['pathParameters']['id']
    update_data = json.loads(event['body'])

    update_expression = "SET " + ", ".join(f"{k}= :{k}" for k in update_data.keys())
    expression_attribute_values = {f":{k}": v for k, v in update_data.items()}

    table.update_item(
        Key={'itemId': item_id},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item updated'})
    }
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def lambda_handler(event, context):
    item_id = event['pathParameters']['id']

    table.delete_item(Key={'itemId': item_id})

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item deleted'})
    }
import json
import psycopg2

def lambda_handler(event, context):
    conn = psycopg2.connect(
        host="your-rds-endpoint",
        database="mydatabase",
        user="your-username",
        password="your-password"
    )
    cur = conn.cursor()

    item_data = json.loads(event['body'])
    name = item_data['name']
    description = item_data['description']
    price = item_data['price']

    cur.execute("INSERT INTO Items (name, description, price) VALUES (%s, %s, %s) RETURNING itemId", (name, description, price))
    item_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item created', 'itemId': item_id})
    }
import json
import psycopg2

def lambda_handler(event, context):
    conn = psycopg2.connect(
        host="your-rds-endpoint",
        database="mydatabase",
        user="your-username",
        password="your-password"
    )
    cur = conn.cursor()

    item_id = event['pathParameters']['id']
    cur.execute("SELECT * FROM Items WHERE itemId = %s", (item_id,))
    item = cur.fetchone()

    if not item:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Item not found'})
        }

    item_data = {
        'itemId': item[0],
        'name': item[1],
        'description': item[2],
        'price': item[3],
        'created_at': str(item[4])
    }

    cur.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps(item_data)
    }
import json
import psycopg2

def lambda_handler(event, context):
    conn = psycopg2.connect(
        host="your-rds-endpoint",
        database="mydatabase",
        user="your-username",
        password="your-password"
    )
    cur = conn.cursor()

    item_id = event['pathParameters']['id']
    update_data = json.loads(event['body'])
    name = update_data['name']
    description = update_data['description']
    price = update_data['price']

    cur.execute("UPDATE Items SET name = %s, description = %s, price = %s WHERE itemId = %s", (name, description, price, item_id))

    conn.commit()
    cur.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item updated'})
    }
import json
import psycopg2

def lambda_handler(event, context):
    conn = psycopg2.connect(
        host="your-rds-endpoint",
        database="mydatabase",
        user="your-username",
        password="your-password"
    )
    cur = conn.cursor()

    item_id = event['pathParameters']['id']
    cur.execute("DELETE FROM Items WHERE itemId = %s", (item_id,))

    conn.commit()
    cur.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item deleted'})
    }
