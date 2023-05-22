aws apigatewayv2 update-integration \
    --integration-id abc12345 \
    --api-id abc12345 \ 
    --request-parameters 'integration.request.header.connectionId'='context.connectionId'

aws apigatewayv2 update-route --route-id abc12345 \
--api-id abc12345\
--request-parameters '{"route.request.header.test" : {"Required": false}}'