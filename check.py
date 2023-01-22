import os

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

print ('u ' + str(EMAIL_HOST_USER))
print ('p ' + str(EMAIL_HOST_PASSWORD))