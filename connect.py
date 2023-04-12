from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()
@logger.inject_lambda_context
def main(event, context):
    logger.info(event)
    return {
    'statusCode': 200,
    'body': f"Hello WebSockets",
  }
