import boto3
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()
endpoint_url = "https://0gmpnpncdl.execute-api.ap-southeast-1.amazonaws.com/dev"
client = boto3.client('apigatewaymanagementapi',endpoint_url=endpoint_url)

@logger.inject_lambda_context
def main(event:dict , context: LambdaContext):
    logger.info(event)
    connection_id = event.get('requestContext').get('connectionId')
    logger.info(connection_id)

    client.post_to_connection(
        Data=b'barbarbarbarbarbar',
        ConnectionId=connection_id
    )

    return {
        'statusCode': 200
    }