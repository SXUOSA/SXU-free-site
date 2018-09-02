import requests
import hashlib
import imgcodeidentify
from PIL import Image
from aip import AipOcr
import re
import optparse

def get_class(username,password,year,term,flag,path):

    header = {
	"Host":"bkjw.sxu.edu.cn",
	"Origin":"http://bkjw.sxu.edu.cn",
	"Content-Type":"application/x-www-form-urlencoded",
	"Referer":"http://bkjw.sxu.edu.cn/_data/login.aspx",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"

	}
    host = "http://bkjw.sxu.edu.cn/sys/ValidateCode.aspx"

    login_url = "http://bkjw.sxu.edu.cn/_data/login.aspx"

    score_url = "http://bkjw.sxu.edu.cn/xscj/Stu_MyScore.aspx"

    while True:

        s = requests.Session()

        r = s.get(host,headers=header)

        with open("imgCode.jpg",'wb+') as w:

            w.write(r.content)

        print("[*]:已经获取验证码")

        yzm = get_code()

        h1 = hashlib.md5()

        h1.update(password.encode(encoding='utf-8'))

        hex_password = h1.hexdigest()

        temp_pwd = username+hex_password[:30].upper()+"10108"

        h2 = hashlib.md5()

        h2.update(temp_pwd.encode(encoding='utf-8'))

        hex_temp = h2.hexdigest()

        dsdsdsdsdxcxdfgfg = hex_temp[:30].upper()   #密码

        txt_asmcdefsddsd = username                 #用户名

        h3 = hashlib.md5()

        h3.update(yzm.upper().encode(encoding='utf-8'))

        hex_temp_yzm = h3.hexdigest()[:30].upper()+'10108'

        h4 = hashlib.md5()

        h4.update(hex_temp_yzm.encode(encoding='utf-8'))

        fgfggfdgtyuuyyuuckjg = h4.hexdigest()[:30].upper()  #验证码

        __VIEWSTATE = "/wEPDwULLTE4ODAwNjU4NjBkZA=="

        __EVENTVALIDATION = "/wEWAgLnybi8BAKZwe+vBg=="

        pcInfo = "Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64;+rv:61.0)+Gecko/20100101+Firefox/61.0Windows+NT+10.0;+Win64;+x645.0+(Windows)+SN:NULL"

        Sel_Type = "STU"
        typeName = "学生"
        values = {}
        values["__VIEWSTATE"] = __VIEWSTATE
        values["__EVENTVALIDATION"] = __EVENTVALIDATION
        values["dsdsdsdsdxcxdfgfg"] = dsdsdsdsdxcxdfgfg
        values["fgfggfdgtyuuyyuuckjg"] = fgfggfdgtyuuyyuuckjg
        values["pcInfo"] = pcInfo
        values["Sel_Type"] = Sel_Type
        values["txt_asmcdefsddsd"] = txt_asmcdefsddsd
        values["txt_pewerwedsdfsdff"] = ""
        values["txt_sdertfgsadscxcadsads"] = ""
        values["typeName"] = typeName

        print("[*]:正在尝试登录")

        t = s.post(login_url,data=values,headers=header)

        if "登录失败" in t.text:

            print("[*]:登录失败，马上重新尝试")

            continue

        else:

            print("[*]:登录成功")

            break



    r = s.get("http://bkjw.sxu.edu.cn/xscj/Stu_MyScore_Drawimg.aspx?x=1&h=2&w=782&xnxq="+str(year)+str(term)+"&xn="+str(year)+"&xq="+str(term)+"&rpt=1&rad=2&zfx="+str(flag),headers=header)

    with open(path,"wb") as jpg:
        jpg.write(r.content)
        print("[*]:成绩图像保存成功")

def get_code():

    APP_ID = '11519354'
    API_KEY = 'tLlZhgC4kwx8ArqEhBXzCvRw'
    SECRET_KEY = 'GnpZ0XXBFgZXz8v0aYTGIMhHRMmlRKSd'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    print("[*]:正在处理验证码图片")
    code = ""
    for j in range(30):
    	imgcodeidentify.deal_img("imgCode.jpg")
    	imgcodeidentify.interference_line(imgcodeidentify.deal_img("imgCode.jpg"),"imgCode.jpg")
    	imgcodeidentify.interference_point(imgcodeidentify.interference_line(imgcodeidentify.deal_img("imgCode.jpg"),"imgCode.jpg"),"imgCode.jpg")
    try:
        print("[*]:正在识别验证码")
        code = client.basicGeneral(get_img_content("imgCode.jpg"))["words_result"][0]["words"]
        code = re.findall('[a-zA-Z0-9]*',code)[0]
        print("[*]:已经得到验证码" + code)
    except:
        pass
    return code


def get_img_content(path):
    with open(path,'rb') as a:
        img_content = a.read()
    return img_content


opt = optparse.OptionParser()
opt.add_option('-u',dest='username',type='string')
opt.add_option('-p',dest='password',type='string')
opt.add_option('-y',dest='year',type='string')
opt.add_option('-t',dest='term',type='string')
opt.add_option('-f',dest='format',type='string')
opt.add_option('-P',dest='jpg_path',type='string')
(options,args) = opt.parse_args()

username = options.username
password = options.password
year = options.year
term = options.term
format = options.format
path = options.jpg_path


get_class(username,password,year,term,format,path)
