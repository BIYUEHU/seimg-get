from genericpath import exists
import requests

filePath = "E:\\桌面\\data\\"
fileName = "seimg.txt"
fileName2 = "seimgr18.txt"
nums = 10000
api = "https://api.lolicon.app/setu/v2?"
api2 = "https://api.lolicon.app/setu/v2?r18=1"
# api = "https://sex.nyan.xyz/api/v2/?r18=true"
tags = ["ツンデレ", "お姉さん"]
tag = None


# 初始化，标签检查，文件检查
def initial():
    if (tag == str):
        api = api + "&tag" + tag
        api1 = api1 + "&tag" + tag

    if (exists(filePath + fileName) != True):
        file = open(filePath + fileName, "w",)
        file.close()

    if (exists(filePath + fileName2) != True):
        file = open(filePath + fileName2, "w")
        file.close()


def climbData(i, b):
    resultJSON = requests.get(
        api + "&tag=" + tags[b], headers={}, params={})
    if type(resultJSON) == requests.models.Response:
        if type(resultJSON.text) == str:
            file = open(filePath + fileName, "a", encoding='utf-8')
            file.write(resultJSON.text + "\n")
            file.close()

            print("\033[0;32;40m第" + str(i) +
                "张" + str(b) + "图片:" + resultJSON.text + "\033[0m")
        else:
            print("\033[0;31;40m第" + str(i) +
                "张图片:" + resultJSON.text + "\003[0m")


def climbDataR18(i, b):
    resultJSON = requests.get(
        api2 + "&tag" + tags[b], headers={}, params={})
    if type(resultJSON) == requests.models.Response:
        if type(resultJSON.text) == str:
            file = open(filePath + fileName2, "a", encoding='utf-8')
            file.write(resultJSON.text + "\n")
            file.close()

            print("\033[0;33;40m第" + str(i) +
                "张" + str(b) + "图片R:" + resultJSON.text + "\033[0m")
        else:
            print("\033[0;31;40m第" + str(i) +
                "张图片R:" + resultJSON.text + "\003[0m")


initial()
# 循环
arrayLen = len(tags)
for a in range(arrayLen):
    for i in range(nums):
        climbData(i, a - 1)
        climbDataR18(i, a - 1)
