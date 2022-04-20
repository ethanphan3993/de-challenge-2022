import json
import boto3
import logging
import os
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def lambda_handler(event, context):
    logger.info("here")
    client = boto3.client("glue")
    CRAWLER = os.environ.get('CRAWLER')
    try:
        logger.info("Start Crawler")
        client.start_crawler(Name=CRAWLER)
    except Exception as e:
        print(e)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
