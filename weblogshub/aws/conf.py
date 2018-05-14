print('i am in conf')

AWS_ACCESS_KEY_ID = 'AKIAJZO7WOLUJCLCFQAA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'rpas3bucket2'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'myproject/static'),
# ]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'weblogshub.storage_backends.MediaStorage'
