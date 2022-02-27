import sys,os,base64,time,json

#配置文件检查及用户名修改代码块 保存至S_B_J_C_T_config.json JSON参数："USERNAME" "USEREMAIL"
def userchange():
    name=input("请输入用户名:")
    email=input("请输入联系方式(eMail):")
    global configdict
    configdict["USERNAME"]=name
    configdict["USEREMAIL"]=email
    fil=open("S_B_J_C_T_config.json","w",encoding="utf-8")
    fil.write(json.dumps(configdict))
    fil.close()
    print("操作成功")
    global mainmenu_errmessage
    mainmenu_errmessage=""
configfile=open("S_B_J_C_T_config.json","r",encoding="utf-8")
configdict={}
cff=configfile.read()
if(cff==""):
    print("warning".upper()+"01:未检测到配置文件 将自动初始化配置")
    userchange()
else:configdict=json.loads(cff)
configfile.close()

#ISO3166地区码检查函数（未完成
def iso3166cn(input):
    if(input=="JPN"):return "日本"
    else:return "ERROR"

#获取窗口宽高及定义版本信息
Twidth = os.get_terminal_size().columns
Thight = os.get_terminal_size().lines
pver="0.1"
pdate="2021/12/7"
#主菜单错误信息变量
mainmenu_errmessage=""

#新增文件菜单及json生成测试代码块（未完成
def new_file_menu():
    global pver
    os.system("cls")
    print((" "*int(((Twidth-22)/2)))+"-----您选择了: 新建文件-----\n")
    jsondict={}
    name=input("请输入资源名:")
    jsondict['BANGUMI_NAME']=name
    btype=input("请输入资源类型(0=TV动画 1=动画电影):")
    while(btype!="0" and btype!="1"):btype=input("参数错误\n请输入资源类型(0=TV动画 1=动画电影):")
    jsondict["TYPE"]=int(btype)
    binfo=input("请输入资源简介(换行用\\n表示):")
    binfo="LINE0_NULL Generate by S.B.J.C.T.t v"+pver+"\\n"+binfo
    binfo_split=binfo.split("\\n")
    jsondict["INFO_COUNT"]=len(binfo_split)-1
    jsondict["INFO"]=[]
    binfocount=0
    while(binfocount<=(len(binfo_split)-1)):
        jsondict["INFO"].append({'LINE':binfo_split[binfocount]})
        binfocount+=1
    date_year=input("请输入作品年份(20xx):")
    if(date_year.isdigit()==False or int(date_year)<=1000 or int(date_year)>=9999):
        trflag=False
        while(trflag==False):
            date_year=input("参数错误\n请输入作品年份(20xx):")
            if(date_year.isdigit()==True):
                if(int(date_year)>=1000):
                    if(int(date_year)<=9999):
                        trflag=True
    date_season=input("请输入作品季度(Q1 Q2 Q3 Q4):")
    date_season=date_season.upper()
    while(date_season!="Q1" and date_season!="Q2" and date_season!="Q3" and date_season!="Q4"):
        date_season=input("参数错误\n请输入作品季度(Q1 Q2 Q3 Q4):")
        date_season=date_season.upper()
    date=date_year+date_season
    jsondict["DATE"]=date
    region=input("[实验性功能 按Enter可跳过](默认为JPN)请输入作品地区的ISO3166码(例:JP/JPN/392代表日本):")
    if(region!=""):
        region=iso3166cn(region)
        while(region=="ERROR"):
            region=input("参数错误\n[实验性功能 按Enter可跳过](默认为JPN)请输入作品地区的ISO3166码(例:JP/JPN/392代表日本):")
            if(region==""):region="JPN"
            region=iso3166cn(region)
    else:
        region="日本"
    jsondict["REGION"]=region
    picadd=input("请输入资源主视觉图片地址(必须为https链接):")
    while(picadd[7]!="/"):
        picadd=input("参数错误\n请输入资源主视觉图片地址(必须为https链接):")
    jsondict["PIC"]=picadd
    if_complete=input("请选择资源更新状态(1.连载中 2.已完结):")
    while(if_complete!="1" and if_complete!="2"):
        if_complete=input("参数错误\n请选择资源更新状态(1.连载中 2.已完结):")
    if(if_complete=="1"):jsondict["IF_COMPLETE"]=False
    else:jsondict["IF_COMPLETE"]=True
    jsondict["PROVIDER_NAME"]=configdict["USERNAME"]
    jsondict["PROVIDER"]=configdict["USEREMAIL"]
    jsondict["EP_COUNT"]=0
    jsondict["EP"]=[{"NUM":0,"VID":"EP0_NULL Generate by S.B.J.C.T.t v"+pver,"DOWN":"EP0_NULL","RES":0,"HTTPS":False}]
    
    jsonfinal=json.dumps(jsondict,ensure_ascii=False)
    
    #↑已完成部分 ↓未完成部分 临时将json输出至testout.json 最终文件名及目录生成方式未确定
    file_test=open("testout.json","w",encoding="utf-8")
    file_test.write(jsonfinal)
    file_test.close()
    #清空主菜单错误信息
    global mainmenu_errmessage
    mainmenu_errmessage=""

#帮助菜单代码块（未完成    
def help_menu():
    #清空主菜单错误信息
    global mainmenu_errmessage
    mainmenu_errmessage=""

#加载文件菜单代码块（未完成    
def load_file_menu():
    #清空主菜单错误信息
    global mainmenu_errmessage
    mainmenu_errmessage=""

#主菜单界面绘制代码块   
def main_menu_draw():
    BAR1_spnum=int((Twidth-58)/2)
    bar1space=" "*BAR1_spnum
    print(bar1space+"╔========================================================╗")
    print(bar1space+"║                                                        ║")
    print(bar1space+"║           SFA-S.B.J.C.T Terminal Version "+pver+"           ║")
    print(bar1space+"║               Written by Xuu   "+pdate+"               ║")
    print(bar1space+"║                                                        ║")
    print(bar1space+"╚========================================================╝")
    print("\n\n\n\n")
    print((" "*int(((Twidth-23)/2)))+"欢迎！请选择一项想要的操作")
    print((" "*int(((Twidth-50)/2)))+"1.打开文件 2.新建文件 3.说明/帮助 4.更改用户 5.退出")
    print("\n"*int((Thight-15)))

#文件编辑界面逻辑（未完成
def edit_file_menu(address):
    pass

#启动前置检查
if (Twidth < 58):
    print("ERROR01：命令行界面宽度不足")
    os._exit(0)
#主界面循环
while 1:
    os.system("cls")
    main_menu_draw()
    uinput1=input(mainmenu_errmessage+"键入您的选择:")
    if(uinput1=="5"):
        os._exit(0)
    elif(uinput1=="4"):
        os.system("cls")
        userchange()
    elif(uinput1=="3"):
        help_menu()
    elif(uinput1=="2"):
        new_file_menu()
    elif(uinput1=="1"):
        load_file_menu()
    else:mainmenu_errmessage="(参数错误)"




