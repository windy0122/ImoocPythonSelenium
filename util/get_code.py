# coding=utf-8
from PIL import Image
# from util.ShowapiRequest import ShowapiRequest
import time
import urllib, urllib.request, sys, urllib.parse, json
import ssl, base64


class GetCode(object):
    # 获取图片
    def __init__(self, driver):
        self.driver = driver

    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(2)

    # 解析图片获取验证码
    # def code_online(self, file_name):
    #     r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
    #     r.addBodyPara("typeId", "35")
    #     r.addBodyPara("convert_to_jpg", "0")
    #     r.addFilePara("image", file_name)  # 文件上传时设置
    #     res = r.post()
    #     print(res.text)
    #     text = res.json()['showapi_res_body']['Result']
    #     time.sleep(2)
    #     return text

    def code_online(self, file_name):
        host = 'https://302307.market.alicloudapi.com'
        path = '/ocr/captcha'
        method = 'POST'
        appcode = '3229f8f5cf214751b8881e410f19e8d1'
        querys = ''
        bodys = {}
        url = host + path

        img_url = file_name
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









