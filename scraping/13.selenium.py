from selenium import webdriver

# Chrome version : 93.0.4577.63
broswer = webdriver.Chrome("./chromedriver.exe") # 
    # () 안에 chromedriver의 경로를 써주면 된다.
broswer.get("http://www.google.com/")

