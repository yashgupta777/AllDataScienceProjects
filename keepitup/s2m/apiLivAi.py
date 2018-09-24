import requests

# headers = {'Authorization' : 'db82955f1b490f1e821254c2839dde033ade2e3f'}
# data = {'device_id' : '5214' ,'platform' : 'python'}
# url = 'https://dev.liv.ai/liv_transcription_api/recordings/validate/'
# res = requests.post(url, headers = headers, data = data)
# print(requests.post(url, headers = headers, data = data))

headers = {'Authorization' : 'Token db82955f1b490f1e821254c2839dde033ade2e3f'}
data = {'user' : '5214' ,'language' : 'EN'}
files = {'audio_file' : open('C:/Users/Yash/Downloads/sample.m4a','rb')}
url = 'https://dev.liv.ai/liv_transcription_api/recordings/'
res = requests.post(url, headers = headers, data = data, files = files)
print(res)
