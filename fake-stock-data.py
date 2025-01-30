"""
fake_stock_prices ={
    {

    }
}

"""
 
import random
import time
import json
import boto3
from datetime import datetime

stream_name = 'stock-prices'

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

def get_data():
    data = {}
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    data['DATE_TIME'] = str(date_time)
    data['STOCK_PRICE'] = round(random.uniform(50.0, 100.0), 2)
    return data

def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey")
        time.sleep(1)
        
if __name__ == "__main__":
    generate(stream_name, kinesis_client)     




#another lab:



fake_data = {
    {
    "ticker": "AAPL",
    "price": "100.00",
    "date": "2020-01-01"
    },
}
    kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(fake_data),
        PartitionKey="partitionkey")  
          