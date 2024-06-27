import requests

url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/1"

payload = {}
headers = {
  'Authorization': 'Bearer psz0zk8oqeetwpgt5i0x91a1jprqfgch',
  'Cookie': 'PHPSESSID=jjrsfh4densrjqi23e0l4rkm8o'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
