aws apigatewayv2 update-integration \
    --integration-id n3mtghr \
    --api-id 0gmpnpncdl \ 
    --request-parameters 'integration.request.header.connectionId'='context.connectionId'


    aws apigatewayv2 update-route --route-id 0abcdef \
    --api-id 0gmpnpncdl \
    --request-parameters '{"route.request.header.test" : {"Required": false}}'