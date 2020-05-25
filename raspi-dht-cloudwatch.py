import boto3
import board
import adafruit_dht

# Especifico el PIN 15 (GPIO22)
dhtDevice = adafruit_dht.DHT22(board.D22)

# Obtengo los valores de temperatura y humedad
temperature = dhtDevice.temperature
humidity = dhtDevice.humidity

temperature = round(temperature,2)
humidity = round(humidity,2)

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
    Namespace='raspifran',
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
    Namespace='raspifran',
    MetricData=[
        {
            'MetricName': 'Humidity',
            'Value': humidity,
            'Unit': 'None'
        },
    ]
)
