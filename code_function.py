import urllib, urllib.request, sys, urllib.parse, json
import ssl, base64

def code_func():

  host = 'https://302307.market.alicloudapi.com'
  path = '/ocr/captcha'
  method = 'POST'
  appcode = '3229f8f5cf214751b8881e410f19e8d1'
  querys = ''
  bodys = {}
  url = host + path

  img_url = '1.jpg'
  with open(img_url, 'rb') as fin:
    image_data = fin.read()
    # print(image_data)
    base64_data = base64.b64encode(image_data)
    # print(base64_data)

  bodys['image'] = base64_data
  bodys['length'] = '0'
  bodys['type'] = '1001'
  post_data = urllib.parse.urlencode(bodys).encode(encoding='UTF8')
  request = urllib.request.Request(url, post_data)
  request.add_header('Authorization', 'APPCODE ' + '3229f8f5cf214751b8881e410f19e8d1')
  # //根据API的要求，定义相对应的Content-Type
  request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
  ctx = ssl.create_default_context()
  ctx.check_hostname = False
  ctx.verify_mode = ssl.CERT_NONE
  response = urllib.request.urlopen(request, context=ctx)
  content = response.read()

  if (content):
      # print(data_res['data']['captcha'])
    data_res = json.loads(content)
    code_res = data_res['data']['captcha']
    # print(code_res)
    return code_res

if __name__ == '__main__':
  code_func()