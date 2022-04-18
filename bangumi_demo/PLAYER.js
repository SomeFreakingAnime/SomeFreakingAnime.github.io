console.log(document.body.clientWidth,document.body.clientHeight)

var url = document.location.toString();
if(url.indexOf("?")==-1)document.getElementById("Hontai").innerHTML="<h1 style=\"text-align:center;\">-WEB ERROR-</h1><p style=\"text-align:center;\">网页未传入参数</p>";
if(url.indexOf("&")==-1)document.getElementById("Hontai").innerHTML="<h1 style=\"text-align:center;\">-WEB ERROR-</h1><p style=\"text-align:center;\">网页传入参数格式错误</p>";
var urlParmStr = url.slice(url.indexOf('?')+1);
var arr = urlParmStr.split('&');
var JSONURL = arr[0].split("=")[1];
var EPCOUNT =arr[1].split("=")[1];
if(typeof(JSONURL)=="undefined"){
    document.getElementById("Hontai").innerHTML="<h1 style=\"text-align:center;\">-JSON ERROR-</h1><p style=\"text-align:center;\">json参数未指定或格式错误</p>";
}
if(JSONURL==""){
    document.getElementById("Hontai").innerHTML="<h1 style=\"text-align:center;\">-JSON ERROR-</h1><p style=\"text-align:center;\">json参数未指定或格式错误</p>";
}   
if(typeof(EPCOUNT)=="undefined")EPCOUNT=1;
if(EPCOUNT=="")EPCOUNT=1;
if(isNaN(EPCOUNT)==true)document.getElementById("Hontai").innerHTML="<h1 style=\"text-align:center;\">-WEB ERROR-</h1><p style=\"text-align:center;\">选集参数错误</p>";
const main_player = new DPlayer({
    container: document.getElementById('PLAYER'),
    video: {
        url: "",
    },
});
function VID_SWITCH(VURL,DURL,VCOUNT,VTITLE,VRES,VHTTPS,EPTOTAL){
    

    if(VHTTPS==false){NON_HTTPS_ALERT();}
    main_player.switchVideo(
        {
            url: VURL,
        },
    );
    //var DBUTTON=document.getElementById("VIDDOWN");
    //DBUTTON.setAttribute("onclick","location.href=\""+DURL+"\"");
    document.getElementById("VIDDOWN_BOX").href=DURL;
    //var P_DIV=document.getElementById("PLAYER_DIV");
    //P_DIV.title="RESOLUTION:"+VRES+"P";
    document.getElementById("VIDRES_BOX").innerText="当前视频分辨率："+VRES+"P";
    if(EPTOTAL==1){
        document.title=VTITLE+" - SFA";
    }
    else{
        var EPSTATUS=document.getElementById("EPW");
        EPSTATUS.innerText='EPISODE:('+VCOUNT+'/'+EPTOTAL+')';
        document.title=VTITLE+" EP"+VCOUNT+" - SFA";
    }

}
function NON_HTTPS_ALERT(){
    var PROTOCOL_CHECK=document.location.protocol;
    if(PROTOCOL_CHECK=="https:"){
        window.alert("当前资源使用无加密协议传输，请以http方式访问本页面，否则无法正常加载视频！");
    }
}
JSONURL = "/bangumi_demo/"+JSONURL+".json";
axios.get(JSONURL).then(function(response){
    if(Number(EPCOUNT)>response.data.EP_COUNT)document.getElementById("Hontai").innerHTML="<h1 style=\"text-align:center;\">-WEB ERROR-</h1><p style=\"text-align:center;\">选集参数错误</p>";
    if(Number(EPCOUNT)<=0)document.getElementById("Hontai").innerHTML="<h1 style=\"text-align:center;\">-WEB ERROR-</h1><p style=\"text-align:center;\">选集参数错误</p>";
    console.log("UPLOAD BY : "+response.data.PROVIDER);
    document.getElementById("PROVIDER").href="mailto:"+response.data.PROVIDER;
    document.getElementById("PROVIDER").innerText=response.data.PROVIDER_NAME;
    var MAIN_PIC = document.getElementById("MAIN_PIC");
    MAIN_PIC.src = response.data.PIC;
    var B_TITLE = document.getElementById("B_TITLE").innerText=response.data.BANGUMI_NAME;
    var B_REGION = document.getElementById("BANGUMI_REGION").innerText=response.data.REGION;
    var B_TYPE = document.getElementById("BANGUMI_TYPE");
    switch(response.data.TYPE){
        case 0:
            B_TYPE.innerText="TV动画";
            break;
        case 1:
            B_TYPE.innerText="动画电影";
            break;
        default:
            B_TYPE.innerText="未知";
    }
    var B_DATE = document.getElementById("BANGUMI_DATE").innerText=response.data.DATE;
    var B_STATUS = document.getElementById("BANGUMI_EP_STATUS");
    switch(response.data.IF_COMPLETE){
        case true:
            B_STATUS.innerText="已完结 全"+response.data.EP_COUNT+"话";
            break;
        case false:
            B_STATUS.innerText="连载中";
            break;
    }
    
    var VAR_INFO_COUNT=response.data.INFO_COUNT;
    var B_INTRO=document.getElementById("INTRO");
    for(INTRO_NUM=1;INTRO_NUM<=VAR_INFO_COUNT;INTRO_NUM++){
        var INTRO_LINE = document.createElement("div");
        INTRO_LINE.innerText=response.data.INFO[INTRO_NUM].LINE;
        B_INTRO.appendChild(INTRO_LINE);
    }
    var EPBUTTON_LIST=document.getElementById("EP_BUTTONS");
    if(response.data.EP_COUNT==1){
        var EPLD=document.getElementById("EPB");
        EPLD.style.display="none";
        VID_SWITCH(response.data.EP[1].VID,response.data.EP[1].DOWN,response.data.EP[1].NUM,response.data.BANGUMI_NAME,response.data.EP[1].RES,response.data.EP[1].HTTPS,response.data.EP_COUNT);
    }
    else{
        var IF_POP=false
        for(EPLOOP = 1;EPLOOP<=response.data.EP_COUNT;EPLOOP++){
            var BUTTONLOOP=document.createElement("button");
            BUTTONLOOP.innerText=EPLOOP;
            var FUNTEXT = "VID_SWITCH(\""+response.data.EP[EPLOOP].VID+"\",\""+response.data.EP[EPLOOP].DOWN+"\","+response.data.EP[EPLOOP].NUM+",\""+response.data.BANGUMI_NAME+"\","+response.data.EP[EPLOOP].RES+","+response.data.EP[EPLOOP].HTTPS+","+response.data.EP_COUNT+")";
            BUTTONLOOP.className="EP_BUTTON";
            BUTTONLOOP.title="RESOLUTION:"+response.data.EP[EPLOOP].RES+"P";
            BUTTONLOOP.setAttribute("onclick",FUNTEXT);
            EPBUTTON_LIST.appendChild(BUTTONLOOP);
            if(response.data.EP[EPLOOP].HTTPS==false)
            {
                if(IF_POP==false){
                    NON_HTTPS_ALERT();
                    IF_POP=true;
                }
                
            }
            
        }
        VID_SWITCH(response.data.EP[EPCOUNT].VID,response.data.EP[EPCOUNT].DOWN,response.data.EP[EPCOUNT].NUM,response.data.BANGUMI_NAME,response.data.EP[EPCOUNT].RES,response.data.EP[EPCOUNT].HTTPS,response.data.EP_COUNT);
    }
    
})
.catch(function (error) {
    document.getElementById("Hontai").innerHTML="<h1 style=\"text-align:center;\">-LOAD ERROR-</h1><p style=\"text-align:center;\">网路错误或资源不存在</p>";
})
