import json
import boto3

##CHANGE THIS BY YOUR ENDPOINT, OR MAKE A VAR ENVIRONMENT
ENDPOIT=''


runtime=boto3.client('runtime.sagemaker')

def lambda_handler(event ,context):

    print("'####:'##::::'##::::'###::::'########:::'######::'##:::'##:")
    print(". ##:: ###::'###:::'## ##::: ##.... ##:'##... ##: ##::'##::")
    print(": ##:: ####'####::'##:. ##:: ##:::: ##: ##:::..:: ##:'##:::")
    print(": ##:: ## ### ##:'##:::. ##: ########:: ##::::::: #####::::")
    print(": ##:: ##. #: ##: #########: ##.. ##::: ##::::::: ##. ##:::")
    print(": ##:: ##:.:: ##: ##.... ##: ##::. ##:: ##::: ##: ##:. ##::")
    print("'####: ##:::: ##: ##:::: ##: ##:::. ##:. ######:: ##::. ##:")
    print("....::..:::::..::..:::::..::..:::::..:::......:::..::::..::")
    print("")

    query_params=event['queryStringParameters']
    
    query=query_params.get('query') ##could be a custom parameter
    payload={
        'inputs': query,
        'parameters':{
            'do_simple':True,
            'top_p':0.7,
            'temperature':0.3,
            'top_k':50,
            'max_new_tokens':512,
            'repetition_penalty':1.03} }
    response=runtime.invoke_endpoint(EndpointName=ENDPOIT, ContentType='application/json', Body=json.dumps(payload))
    prediction=json.loads(response['Body'].read().decode('utf-8'))
    final_result=prediction[0]['generated_text']

    return {
        'satatusCode': 200,
        'body': json.dumps(final_result)
    }
        

