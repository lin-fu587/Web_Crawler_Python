# 一般傳統的網頁運作流程(連線至網頁):
# 1.在瀏覽器(chrome)搜尋 網頁名稱.com
# 2.瀏覽器發出請求到那個網頁的遠端伺服器
# 3.網頁的遠端伺服器就將帶有資料(文章標題,文字等)的html網頁原始碼回傳給瀏覽器
# 4.瀏覽器將原始碼顯示成完整的網頁

#使用AJAX技術的網頁運作流程(連線至網頁):
# 1.在瀏覽器(chrome)搜尋 網頁名稱.com
# 2.瀏覽器發出請求到那個網頁的遠端伺服器
# 3.網頁的遠端伺服器就將不帶資料(可能只有html的標籤,沒有文字內容)的html網頁回傳給瀏覽器
# 4.瀏覽器根據取得的jsc的程式碼發送第二次請求到網頁的伺服器
# 5.伺服器才把真正的資料回傳給瀏覽器
# 6.瀏覽器將原始碼顯示成完整的網頁
# 還有可能發第三次,第四次的請求(從第二次之後的動作都叫做AJAX的技巧 *第二次也算 )

#在網路爬蟲時，要認清兩個問題:
# 1.要先找出網站運作模式(分辨方法:#1.一個網站按f5，如果在跑的過程中有停頓且出現一個殼(可能沒文字內容)=>那就是AJAX技術)
                                #2.複製文章標題，去網頁原始碼搜尋此標題會找不到(意旨文章資料不在HTML中)
# 2.找出真正能抓到資料的網址 (在request header中的general底下的request URL才是真正用XHR連線的網址)
# 3.模仿一般使用者的連線
# 4.知道資料格式為何 (基本都是html,JSON，可以在headers旁的review或response判讀格式)
# 5.解析資料並使用資料 (到開發人員選項的network中的XHR尋找要找的資料(有可能在很底層，要一個一個打開，裡面的名稱都是線索))

#抓取medium.com的資料
import urllib.request as request
url="https://medium.com/_/api/home-feed"
#建立一個實體物件，附加request headers的資訊
url_plus=request.Request(url,headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
})
with request.urlopen(url_plus) as url_ok:
    data=url_ok.read().decode("utf-8")
#print(data)

#解析json格式資料(json資料不是 字典{} ，就是 列表[] )
import json
data=data.replace("])}while(1);</x>","")    #將原始資料中的"])}while(1);</x>"替換成空字串"=>這樣才能讓所有資料成符合json格式去做解析
data=json.loads(data)    #把原始資料解析成字典/列表的表現形式
post=data["payload"]["references"]["Post"]  #此資料是一個字典
for i in post:    #假如用字典做迴圈，迴圈將會把字典中每一個鍵(key=>字串)一個一個放入i裡
    article=post[i] #獲取每一個鍵對應的值
    print(article["title"])
    
