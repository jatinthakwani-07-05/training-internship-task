import requests

url = "https://custom-web-api.herokuapp.com/api/v1/users"

payload={'name': 'jatin thakwani',
'age': '22',
'college': 'cdgi',
'mobileNumber': '7990747589',
'githubLink': 'https://github.com/jatinthakwani-07-05'}
files=[
  ('documents',('Japanese_particles.pdf',open('/C:/Users/HP/Pictures/Japanese_particles.pdf','rb'),'application/pdf'))
]
headers = {
  'emailID': 'jatinthakwani123@gmail.com',
  'rollNO': '78'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
