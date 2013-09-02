__author__ = 'Chris Bergh'

import boto
import os
import ConfigParser

boto_path = os.path.expandvars("${BOTO_PATH}")
boto_config = os.path.expandvars("${BOTO_CONFIG}")
print ('BOTO_PATH ' + boto_path )
print ('BOTO_CONFIG ' + boto_config )


config = ConfigParser.ConfigParser()
config.read(boto_config)

print config.sections()

access_key = config.get('Credentials','aws_access_key_id' )
secret_key = config.get('Credentials','aws_secret_access_key')
print access_key
print secret_key

from boto.s3.connection import S3Connection

conn = S3Connection(access_key, secret_key)

conn.create_bucket('testbotobucket2')

print ('all done \n')







