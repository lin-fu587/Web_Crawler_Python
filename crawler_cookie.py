#cookie=>網站存放在瀏覽器的一小段內容(可以在開發者選項中的application中的cookie知道網站存取在瀏覽器的cookie)
#八卦板跟電影版差別在前面有18歲限制=>因為我們程式沒將cookie(over18)帶上，所以搜尋到的頁面原始碼都是18歲的點選頁面
#一樣要盡可能模仿一般使用者
#cookie也是request headers裡的一項
import urllib.request as request
def getdata(url):

    url_plus=request.Request(url,headers={
        "cookie":"over18=1",    #伺服器存在瀏覽器的cookie在連線時將此cookie告訴伺服器，代表我已經點選過18歲的頁面了
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    })    #建立實體物件Request(參數,指定參數)並放入url_plus中=>讓此實體物件帶有網址跟使用者資訊

    with request.urlopen(url_plus) as res1:
        data=res1.read().decode("utf-8")
    #print(data) 

    import bs4
    data_used=bs4.BeautifulSoup(data,"html.parser") #一樣是實體物件
    data_choose=data_used.find_all("div",class_="title")    #回傳列表
    for i in data_choose:
        if i.a!=None:
            print(i.a.string)
    #找到下一個網址
    nextlink=data_used.find("a",string="‹ 上頁")    #找到內文是 ‹ 上頁 的a標籤=>回傳一個標籤
    return nextlink["href"] #標籤名[屬姓名]=>要標籤的屬性就這樣寫

#主程式:抓取多個頁面的標題
pageurl="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
    pageurl="http://www.ptt.cc"+getdata(pageurl)    #幫原來回傳的字串連接成完整網址
    count=count+1