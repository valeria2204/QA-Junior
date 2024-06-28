import requests

url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default/0"

payload = {}
headers = {
  'Authorization': 'psz0zk8oqeetwpgt5i0x91a1jprqfgch',
  'Cookie': 'PHPSESSID=hptq27c9c3fum3b48p06vd1k4b'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)