import boto3
import os
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()

# endpoint_http_url = os.environ['API_ENDPOINT'].replace("wss://","https://")

# client = boto3.client('apigatewaymanagementapi',endpoint_url=endpoint_http_url)

@logger.inject_lambda_context
def main(event:dict , context: LambdaContext):
    logger.info(event)
    connection_id = event.get('requestContext').get('connectionId')

    # client.post_to_connection(
    #     Data=b'barbarbarbarbarbar',
    #     ConnectionId=connection_id
    # )

    return {
        'statusCode': 200,
        'body': f'Hello from Lambda!, your connection id is {connection_id}'
    }