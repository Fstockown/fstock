import requests
from bs4 import BeautifulSoup

# import pyrebase

# config ={
#     "apiKey": "AIzaSyCY1CKDsoF4frwE9hDv0Cvybc559hUrb70",
#     "authDomain": "fstock-9ced2.firebaseapp.com",
#     "projectId": "fstock-9ced2",
#     "databaseURL": "https://fstock-9ced2-default-rtdb.asia-southeast1.firebasedatabase.app",
#     "storageBucket": "fstock-9ced2.appspot.com",
#     "messagingSenderId": "956197289236",
#     "appId": "1:956197289236:web:a96a757386b39788435601",
#     "measurementId": "G-HKY3F089QX"
# }

# firebase = pyrebase.initialize_app(config)

# def makeStock_data(current,date,stock):
#     min = 0 
#     max = current
#     try:
#         min = firebase.child("stock_data").child(stock).child(date).get().value()["min"]
#         max = firebase.child("stock_data").child(stock).child(date).get().value()["max"]
#     except Exception as e :
#         print(e)
#     if min > current :
#         min = current
#     elif max < current:
#         max = current
#     data_map = {"date":date, "min":min, "max":max, "current":current}
#     return data_map


# def pull_data(api):
# r = requests.get(api)
# web_c = BeautifulSoup(r.text,'lxml')
# web_c = web_c.find('div',{"class":"D(ib) Mend(20px)" })
# web_c = web_c.find('span').text
# if web_c ==[]:
        # web_c = "9999"
    


# if __name__=="__main__":
# def data(api):
#     r = requests.get(api)
#     web = BeautifulSoup(r.text,"lxml")
#     web = web.find('div',{"class":"D(ib) Mend(20px)" })
#     web = web.find('span').text

#     return str(web)
# print(data("https://in.finance.yahoo.com/quote/%5EBSESN?p=%5EBSESN&.tsrc=fin-srch"))


# de = {"aman":"79","suman":"120"}
# for i in de:
#         print(i,de[i])





# #function to convert string into int or float 
# def con(data):
#         inte=str()
#         datali = list(data)
#         for i in datali:
#                 if i != ",":
#                         inte = inte+i
#         result = float(inte)
#         return result
# print(type(con("52,23,45.09")))



# import pyrebase               
                        

# config ={
#   "apiKey": "AIzaSyCY1CKDsoF4frwE9hDv0Cvybc559hUrb70",
#   "authDomain": "fstock-9ced2.firebaseapp.com",
#   "databaseURL": "https://fstock-9ced2-default-rtdb.asia-southeast1.firebasedatabase.app",
#   "projectId": "fstock-9ced2",
#   "storageBucket": "fstock-9ced2.appspot.com",
#   "messagingSenderId": "956197289236",
#   "appId": "1:956197289236:web:649d4a76569d3341435601",
#   "measurementId": "G-HZ7Z7R2HLG"
# }


# firebase = pyrebase.initialize_app(config)
# db = firebase.database()
# data = {"name": "Mortimer 'Morty' Smith"}

# db.child("users").push(data)









import pyrebase
from datetime import datetime


config ={
  "apiKey": "AIzaSyCY1CKDsoF4frwE9hDv0Cvybc559hUrb70",
  "authDomain": "fstock-9ced2.firebaseapp.com",
  "databaseURL": "https://fstock-9ced2-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "fstock-9ced2",
  "storageBucket": "fstock-9ced2.appspot.com",
  "messagingSenderId": "956197289236",
  "appId": "1:956197289236:web:649d4a76569d3341435601",
  "measurementId": "G-HZ7Z7R2HLG"
}
# initilizing pyrebase
firebase = pyrebase.initialize_app(config)

db = firebase.database()

db.child("stock").child("nifty50").child(str(datetime.now().date())).set({"min":"23.67567","max":"23.089"})
x = db.child("stock").child("nifty50").child(str(datetime.now().date())).get().val()["min"]
print(float(x))

print(datetime.now().date())