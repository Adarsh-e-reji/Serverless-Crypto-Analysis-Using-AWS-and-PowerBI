import json
import boto3
import urllib.request
from datetime import datetime

BUCKET = "adarsh-aws-project-bucket"
FOLDER = "c_data/"

def lambda_handler(event, context):

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    timestamp = datetime.utcnow()

    csv_content = f"timestamp,bitcoin_usd,ethereum_usd\n{timestamp},{data['bitcoin']['usd']},{data['ethereum']['usd']}"

    filename = f"{FOLDER}crypto_{timestamp.strftime('%Y%m%d_%H%M%S')}.csv"

    s3 = boto3.client("s3")

    s3.put_object(
        Bucket=BUCKET,
        Key=filename,
        Body=csv_content
    )

    return {
        "statusCode": 200,
        "message": "File uploaded to S3"
    }




    