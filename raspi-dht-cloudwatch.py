import boto3
import board
import adafruit_dht
import socket

# DHT22 using PIN 15 (GPIO22)
dhtDevice = adafruit_dht.DHT22(board.D22)

# Obtaining temperature and humidity
temperature = dhtDevice.temperature
humidity = dhtDevice.humidity

temperature = round(temperature,2)
humidity = round(humidity,2)

# Obtaining hostname
hostname = socket.gethostname()

# If I want to print the output
# print ('Temperature: ',temperature,', Humidity: ',humidity)

# AWS credentials and region needs to be added
# Credentials: ~/.aws/credentials
# Region: ~/.aws/config
# Guide: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#guide-configuration

# CloudWatch
cloudwatch = boto3.client('cloudwatch')

# Add temperature metric
cloudwatch.put_metric_data(
    Namespace=hostname,
    MetricData=[
        {
            'MetricName': 'Temperature',
            'Value': temperature,
            'Unit': 'None'
        },
    ]
)

# Add humidity metric
cloudwatch.put_metric_data(
    Namespace=hostname,
    MetricData=[
        {
            'MetricName': 'Humidity',
            'Value': humidity,
            'Unit': 'None'
        },
    ]
)
