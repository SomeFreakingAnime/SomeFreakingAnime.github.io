import json
import pinyin
f_L=open('//192.168.1.5/web/CONFIGTOOL/bangumilist_prototype.json',encoding="UTF8").read()
print(f_L)
dic=json.loads(f_L)
def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False
def data_search(inputstr):
    inputstr=pinyin.get(inputstr,format='strip')
    inputstr=inputstr.upper()
    result=[]
    cou=len(dic['list'])
    i=0
    while(i<cou):
        cc1=pinyin.get(dic['list'][i]['name'],format='strip')
        cc1=cc1.upper()
        if(cc1.find(inputstr)!=-1):
            print(str(i)+' '+dic['list'][i]['name']+' '+dic['list'][i]['JSON'])
        i=i+1


while 1:
    i=input()
    data_search(i)
