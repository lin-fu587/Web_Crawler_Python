#抓取PTT電影版的網頁原始碼(HTML)=>要讓我們的連線看起來像是一般使用者，否則會被網頁拒絕
#1.所以必須先去要抓取資料的網頁選擇開發人員工具，點選network，其中位於最上方的index.html點開按header
#2.我們必須像裡面的request header一樣給予類似一般使用者的連線許可(裡面的user-agent)

import urllib.request as request
url="https://www.ptt.cc/bbs/movie/index9187.html"
#使用request模組中的Request函式在網址連線時附加Request Header資訊，將此回傳的物件放入re1物件(變數)中
re1=request.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"})

with request.urlopen(re1) as ptt:
    data=ptt.read().decode("utf-8")
#print(data)

#解析原始碼(這邊必須安裝beautifulsoup4=>下方指令打 pip install beautifulsoup4)
import bs4
root=bs4.BeautifulSoup(data,"html.parser")  #讓第三方套件幫我們解析data資料(html格式=>"html.parser")
print(root.title)   #解析完畢後，要使用的方法=>操作物件(變數).標籤名稱(<>角括弧中的字)
print(root.title.string)    #上面一行程式可抓到=> <title>看板 movie 文章列表 - 批踢踢實業坊</title>
                            #，這行程式可抓到=> 看板 movie 文章列表 - 批踢踢實業坊

titles=root.find("div",class_="title")  #尋找class="title"的div標籤，find()工具只找一個
print(titles.a.string+"\n")  #titles代表抓到class="title"的div標籤
                        #titles.a代表抓到class="title"的div標籤中的a標籤

titles=root.find_all("div",class_="title")  #尋找class="title"的div標籤，find_all()工具會找所有的，並給我們一個列表(list)
for i in titles:
    if i.a !=None:
        print(i.a.string)  #i代表抓到class="title"的div標籤
                        #i.a代表抓到class="title"的div標籤中的a標籤