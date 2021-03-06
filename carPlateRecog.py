# %%
import time
import openalpr_api
from openalpr_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openalpr_api.DefaultApi()
# file | The image file that you wish to analyze
image = '/Users/benjamin/Downloads/rasptemp/aussie.jpg'
# str | The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/
secret_key = 'sk_5ea09962b11521cae432ecfe'
country = 'au'  # str | Defines the training data used by OpenALPR.  \"us\" analyzes  North-American style plates.  \"eu\" analyzes European-style plates.  This field is required if using the \"plate\" task  You may use multiple datasets by using commas between the country  codes.  For example, 'au,auwide' would analyze using both the  Australian plate styles.  A full list of supported country codes  can be found here https://github.com/openalpr/openalpr/tree/master/runtime_data/config
# int | If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request  (optional) (default to 0)
recognize_vehicle = 0
# str | Corresponds to a US state or EU country code used by OpenALPR pattern  recognition.  For example, using \"md\" matches US plates against the  Maryland plate patterns.  Using \"fr\" matches European plates against  the French plate patterns.  (optional) (default to )
state = ''
# int | If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response  (optional) (default to 0)
return_image = 0
# int | The number of results you would like to be returned for plate  candidates and vehicle classifications  (optional) (default to 10)
topn = 10
# str | Prewarp configuration is used to calibrate the analyses for the  angle of a particular camera.  More information is available here http://doc.openalpr.com/accuracy_improvements.html#calibration  (optional) (default to )
prewarp = ''

try:
    api_response = api_instance.recognize_file(
        image, secret_key, country, recognize_vehicle=recognize_vehicle, state=state, return_image=return_image, topn=topn, prewarp=prewarp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->recognize_file: %s\n" % e)

pprint(api_response.results)

# %%
unpacklist = api_response.results
result = []

for i in unpacklist:
    result.append(i.plate)

result[0]

resultdict = {'carNum': result[0],
              'parkingLotNum': '001'}

resultdict

import json
import requests
# %%

payload = resultdict
headers = {'content-type': 'application/json'}
url = 'api/parking/'

response = requests.post(url, data=json.dumps(payload), headers=headers)
