#!/usr/bin/python
# -*-coding:utf-8-*-

import httplib
import urllib

# Define parameters need to post
params = urllib.urlencode({'./sling:resourceType': 'foundation/components/parsys/colctrl',
                           './jcr:lastModified': '',
                           './jcr:lastModifiedBy': '',
                           '_charset_': 'utf-8',
                           ':status': 'carchanging',
                           './layout': '2;cq-colctrl-lt0'})
# Define headers
headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Connection": "Keep-Alive",
           "Cookie": "login-token=e583e9d8-93d8-46c4-9729-9bf13fae2235%3ab3d9c18b-e7e3-435f-8d72-b222bb8818d9_75d16b34d54fcd3f%3acrx.default"}

# Create connection
conn = httplib.HTTPConnection("localhost:4502")

# Send request
conn.request(method="POST", url="/content/geometrixx/en/products/jcr:content/par/5_1219676772646",
             body=params, headers=headers)

# Get response
response = conn.getresponse()

# Check result
if response.status == 200:
    print "Success!"
else:
    print "Status: " + response.status

# Close connection
conn.close()
