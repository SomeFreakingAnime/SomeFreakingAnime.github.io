import sys,os,base64,time,json
Twidth = os.get_terminal_size().columns
Thight = os.get_terminal_size().lines
pver="0.1"
pdate="2021/12/7"

mainmenu_errmessage=""

def new_file_menu():
    global pver
    os.system("cls")
    
    print((" "*int(((Twidth-18)/2)))+"-----您选择了: 新建文件-----\n")
    jsondict={}
    name=input("请输入资源名:")
    jsondict['BANGUMI_NAME']=name
    btype=input("请输入资源类型(0=TV动画 1=动画电影 2=WEB动画/动画短片):")
    while(btype!="0" and btype!="1" and btype!="2"):btype=input("参数错误\n请输入资源类型(0=TV动画 1=动画电影 2=WEB动画/动画短片):")
    jsondict["TYPE"]=int(btype)
    binfo=input("请输入资源简介(换行用\\n表示):")
    binfo="LINE0_NULL Generate by S.B.J.C.T.t v"+pver+"\\n"+binfo
    binfo_split=binfo.split("\\n")
    print(len(binfo_split))
    jsondict["INFO_COUNT"]=len(binfo_split)-1
    jsondict["INFO"]=[]
    binfocount=0
    while(binfocount<=(len(binfo_split)-1)):
        jsondict["INFO"].append({'LINE':binfo_split[binfocount]})
        print(str(jsondict["INFO"][binfocount]))
        binfocount+=1
    i=input()

    jsonfinal=json.dumps(jsondict)

    file_test=open("testout.json","w",encoding="utf8")
    file_test.write(jsonfinal)
    file_test.close()

    global mainmenu_errmessage
    mainmenu_errmessage=""
    
def help_menu():
    global mainmenu_errmessage
    mainmenu_errmessage=""
    
def load_file_menu():
    global mainmenu_errmessage
    mainmenu_errmessage=""
    
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
    print((" "*int(((Twidth-39)/2)))+"1.打开文件 2.新建文件 3.说明/帮助 4.退出")
    print("\n"*int((Thight-15)))


if (Twidth < 58):
    print("ERROR01：命令行界面宽度不足")
    os._exit(0)

while 1:
    os.system("cls")
    main_menu_draw()
    uinput1=input(mainmenu_errmessage+"键入您的选择:")
    if(uinput1=="4"):
        os._exit(0)
    elif(uinput1=="3"):
        help_menu()
    elif(uinput1=="2"):
        new_file_menu()
    elif(uinput1=="1"):
        load_file_menu()
    else:mainmenu_errmessage="(参数错误)"




