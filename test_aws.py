import boto3

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
data = open('results/api_test.png','rb')
s3.Bucket('style-transfer-output-test').download_file('test.png', 'test.png')
