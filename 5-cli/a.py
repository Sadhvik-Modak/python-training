# import requests
#
# url = "http://localhost:8000/employees/"
#
# payload={}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)

import requests
import json

url = "http://localhost:8000/employees/"

payload = json.dumps({
  "emp_id": 4,
  "name": "luffy",
  "salary": 1221818,
  "address": "ghi"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
