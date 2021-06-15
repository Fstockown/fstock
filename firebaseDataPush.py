from datetime import datetime
import json
import pyrebase
import requests
from bs4 import BeautifulSoup
#config data for firebase 

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
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("admin@fstock.com","fstockadmin7987")

#function to convert string into float
def convertType(data):
        inte=str()
        datali = list(data)
        for i in datali:
                if i != ",":
                        inte = inte+i
        result = float(inte)
        return result



def upload_data(data,stock,date):
    db = firebase.database()
    db.child("stocks").child(stock).child(date).set(data)


#function to make stock datalist 
def makeStock_data(current,date,stock):
    min = 0 
    max = current
    try:
        min = int(firebase.child("stock_data").child(stock).child(date).get().value()["min"])
        max = int(firebase.child("stock_data").child(stock).child(date).get().value()["max"])
    except Exception as e :
        print(e)
    if min > current :
        min = current
    elif max < current:
        max = current
    data_map = {"date":date, "min":min, "max":max, "current":current}
    return data_map

def get_dataLive(api):
    # function to get data from api
    r = requests.get(api)
    web = BeautifulSoup(r.text,"lxml")
    web = web.find('div',{"class":"D(ib) Mend(20px)" })
    web = web.find('span').text

    return str(web)
    

api_list = {
    "sensex":"https://in.finance.yahoo.com/quote/%5EBSESN?p=%5EBSESN",
    "nifty50":"https://in.finance.yahoo.com/quote/%5ENSEI?p=%5ENSEI",
    "bitcoin":"https://in.finance.yahoo.com/quote/BTC-INR?p=BTC-INR",
    "dogecoin":"https://in.finance.yahoo.com/quote/DOGE-INR?p=DOGE-INR",
    "SBI":"https://in.finance.yahoo.com/quote/SBIN.NS?p=SBIN.NS&.tsrc=fin-srch",
    "HDFC":"https://in.finance.yahoo.com/quote/HDFCBANK.NS?p=HDFCBANK.NS&.tsrc=fin-srch",
    "relience":"https://in.finance.yahoo.com/quote/RELIANCE.NS?p=RELIANCE.NS&.tsrc=fin-srch",
    "tesla,inc":"https://in.finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch",
    "facebook,inc":"https://in.finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch",
    "amazon,inc":"https://in.finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch",
    "tata_motors":"https://in.finance.yahoo.com/quote/TTM?p=TTM&.tsrc=fin-srch",
    "tata_steel_limited":"https://in.finance.yahoo.com/quote/TATASTEEL.NS?p=TATASTEEL.NS&.tsrc=fin-srch",
}

while True:
    date_forDay = datetime.date(datetime.now())
    day =  date_forDay.weekday()
    date = str(date_forDay)
    time = datetime.now().hour
    if day != 5 and day != 6:
        if time >=9 and time <= 15:
            for i in api_list:
                stock = i 
                api = api_list[i]
                data_str = get_dataLive(api)
                data = convertType(data_str)
                data_map = makeStock_data(data, date ,stock)
                upload_data(data_map, stock,date)

            # main database edit here 


            print('aman')
        else:
            #tempory break the sript runs forever
            break



        
# if __name__=="__main__":
    # print(time)


