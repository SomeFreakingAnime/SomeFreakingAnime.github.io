#!/usr/bin/python 
# -*- coding: utf-8 -*-
import datetime

current_address = 'c:/Users/HP/SFA/SomeFreakingAnime.github.io/'

htmlname = input("Input HTMLname:")
anmtype = input("Input Type:")
title = input("Input Title:")
res = input("Input Res:")
vidurl = input("Input Video:")
viddown = input("Input Download Link:")
htflink = current_address+'bangumi/'+htmlname+'.html'
htf = open(htflink,'w',encoding='utf-8')
viddown = "'"+viddown+"'"
htftext = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>'''+title+'''</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <!--meta content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no" name="viewport"-->
        <!-- 引用 liveplayer-element.min.js -->
        
    </head>
    <body>
        <h1 style="text-align:center">'''+title+'''</h1>
        <hr>
        <div style="text-align:center">
            <video controls="" autoplay="" name="media" height="480px" width="800px"><source src="'''+vidurl+'''" type="video/mp4"></video>
        </div>
        <hr>
        <div style="text-align:center">
            <button onclick="location.href='''+viddown+'''" type="button">视频下载</button>
            <button onclick="location.href='https://somefreakinganime.github.io'" type="button">回到主页</button>
        </div>
        
    </body>
'''
htf.write(htftext)
htf.close()
bgmlist = open(current_address+'bangumilist.html','r',encoding='utf-8')
bgmlist_prev = bgmlist.read()
bgmlist.close()
bgmlist = open(current_address+'bangumilist.html','w',encoding='utf-8')
to_day = datetime.date.today()
to_day_strft = to_day.strftime('%y.%m.%d')
bgmlist_add = '''<p style="text-align:center;font-size: large">
    <a href="https://some.freakinganime.online/bangumi/'''+htmlname+'''.html" target="_blank">['''+anmtype+''']'''+title+''' ('''+res+''')<a>         20'''+to_day_strft+'''上传
</p>'''+'\n'
bgmlist_now = bgmlist_add+bgmlist_prev
bgmlist.write(bgmlist_now)
bgmlist.close()
