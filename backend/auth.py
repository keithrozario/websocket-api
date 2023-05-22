from aws_lambda_powertools import Logger

logger = Logger()


@logger.inject_lambda_context
def main(event, context):
    logger.info(event)
    logger.info(context)
    
    # new! -- create a policy that can be used by APIGW to make API calls
    principalId = "user|a1b2c3d4"
    statement = {
            'Action': 'execute-api:Invoke',
            'Effect': 'Allow',
            'Resource': "arn:aws:execute-api:*"
    }
    policy = {
            'principalId' : principalId,
            'policyDocument' : {
                'Version' : "2012-10-17",
                'Statement' : [statement],

            }
    }
    authResponse = policy

    # new! -- add additional key-value pairs associated with the authenticated principal
    # these are made available by APIGW like so: $context.authorizer.<key>
    # additional context is cached
    context = {
        'key': event['headers']['Auth'], # $context.authorizer.key -> value
        'number' : 1,
        'bool' : True
    }
    # context['arr'] = ['foo'] <- this is invalid, APIGW will not accept it
    # context['obj'] = {'foo':'bar'} <- also invalid
 
    authResponse['context'] = context
    logger.info(authResponse)
    
    return authResponse

