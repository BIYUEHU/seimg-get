#coding: utf8
import requests
import json
import os
# 导入相关库

# 基础配置:filePath保存路径、times调用次数(即下载的图片,不建议过大,否则可能会像刚才那样运行一会就报错,因为API请求超时
# 当然,你也可以设置个一定时间内循环执行一次)、api即图片信息获取接口(下面的接口是UP主自己的,有条件可以用其他接口分担下服务器
# 压力，如果接口调用次数过多可能会做一些调用限制)
filePath = "F:\\imgs\\"
times = 5000
api = "http://imlolicon.tk/api/seimg/v2/?r18=true"


# 接着是主要部分
def climbImgs(i):
    resultJSON = requests.get(api, headers={}, params={})
    if type(resultJSON) == requests.models.Response:
        if type(resultJSON.text) == str:
            # 对接口发送get请求
            temp = json.loads(resultJSON.text)
            print(temp);
            data = temp['data'][0]
            title = data['pid']
            url = data['url']
            imgArray = url.split('.')
            imgType = imgArray[len(imgArray) - 1]
            # 对返回的JSON信息进行简单的解析，解析出URL图片链接、图片类型(jpg or png)、以及标题(这里以图片的pid为图片名字)

            if os.path.exists(filePath + title + "." + imgType) == False:
                # IF判断，以防止下到重复的图片

                # 图片下载函数
                def download_img(img_url, api_token):
                    header = {"Authorization": "Bearer " + api_token}

                    refuse = requests.get(img_url, headers=header, stream=True)
                    if refuse.status_code == 200:
                        open(filePath + title + "." + imgType,
                             "wb").write(refuse.content)
                    # 写入到文件
                    del refuse

                if __name__ == '__main__':
                    api_token = "fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"
                    download_img(url, api_token)

                # 打印信息到控制台
                print("第" + str(i) + "张图片:" + title + "." + imgType)


# 最后是循环
for i in range(times):
    climbImgs(i)
