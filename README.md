# Accounting System with PostegreSQL

## Contents

- [簡介](#簡介)
- [軟體](#軟體)
- [clone 與安裝相依套件](#clone-與安裝相依套件)
- [執行步驟](#執行步驟)
- [網址](#網址)
- [API spec](#API-spec)
- [DB schema](#DB-schema)
- [執行圖](#執行圖)

## 簡介

從帳務資料取出所需統整資訊

## 軟體
- Visual Studio Code
- PostgreSQL 13
- Git

## clone 與安裝相依套件
- 請在 `Console` 輸入下方指令
  - 從 GitHub Clone 專案
  ```
  git clone https://github.com/yali860208/api.git
  ```
  - 切換路徑到專案資料夾
  ```
  cd ./api-main
  ``` 
  - 安裝相關套件
  ``` 
  pip install -r requirements.txt
  ``` 
  - 透過 Visual Studio Code 開啟專案
  ``` 
  code .
  ``` 
  
## 執行步驟
請在 `Console` 輸入下方指令
- 上傳資料到 PostgreSQL
  1. 到 PostgreSQL 創建一個資料庫
  2. 更改`api-main/app/database.ini`內的基本資料
  3. 
      ```
      cd ./api-main/app
      ```
      ```
      python connect.py
      ```
      若出現此 Error
      ![](https://i.imgur.com/MQYCr5J.png)
      - data.csv右鍵>內容>安全性>編輯>新增>Everyone>勾選完全控制>套用>確定 ([參考資料](https://blog.csdn.net/yufenghyc/article/details/58224641))
      ![](https://i.imgur.com/s9KRGbWm.png)
- 啟動專案
  ```
  cd ./api-main
  ```
  ```
  python run.py
  ```
## 網址

* 本地端啟動程式
  * http://localhost:8080/index.html

## API spec
[參考資料](https://dotblogs.com.tw/bda605/2020/02/26/170804)

- 參數
    |功能|input 參數名稱|output 參數名稱|函數|URL|
    |:-:|-|-|-|-|
    |0|pid_uid|resultid|list_uid|POST http://127.0.0.1:8080/uid |
    |1|uid_cost|resultcost|sum_unblendedcost|POST http://127.0.0.1:8080/cost |
    |2|uid_amount|resultamount|sum_usageamount|POST http://127.0.0.1:8080/amount |
    |3|uid_count|resultcount|sum_usagecount|POST http://127.0.0.1:8080/count |
    
 
- 功能說明
    |功能|說明|
    |:-:|-|
    |0|輸入 **PayerAccountID**，顯示使用的 **UsageAccountID**|
    |1|輸入 **UsageAccountID**，顯示其使用的 **Product Name** 及其 Product **總 Cost**|
    |2|輸入 **UsageAccountID**，顯示其使用的 **Product Name** 及其 Product **使用日期**和**總 Amount**|
    |3|輸入 **UsageAccountID**，顯示其使用的 **Product Name** 及其 Product **使用總次數**|
    
## DB schema
![](https://i.imgur.com/0bGDaVL.png)

## create with index
reduce the execution time

[參考資料](https://dataschool.com/sql-optimization/how-indexing-works/)
  - 功能 2 不使用 index
    - ![](https://i.imgur.com/AhabFon.png)
  - 功能 2 使用 index
    - ![](https://i.imgur.com/hcUppWG.png)
  - 功能 3 不使用 index
    - ![](https://i.imgur.com/vmgKN3Y.png)
  - 功能 3 使用 index
    - ![](https://i.imgur.com/HfUkoxh.png)


     
## 執行圖

![](https://i.imgur.com/HNmj30nl.png)

正常來說下面會顯示輸入的 ID 和輸出的結果
但重開機後要寫 README 時無法執行 http://localhost:8080/index.html
推測遇到的問題：
https://codertw.com/%E5%89%8D%E7%AB%AF%E9%96%8B%E7%99%BC/50603/

先拿 Postman 結果代替
- 功能 0
![](https://i.imgur.com/xn6DqRO.png)
- 功能 1
![](https://i.imgur.com/Ol6paWH.png)
- 功能 2
![](https://i.imgur.com/8zVAzhH.png)
- 功能 3
![](https://i.imgur.com/31rTGwN.png)
