from urllib2_file import Request
import urlopen

headers = {
  'Authorization': '08e15c0a-4119-4ed5-8852-bf512a3cd434'
}
request = Request('https://api.wizenoze.com/v1/customSearchEngines?reading=reading%20english&english=&grade%201=', headers=headers)

response_body = urlopen(request).read()
print (response_body)