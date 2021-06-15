from datetime import datetime
import pyrebase

#config data for firebase 

config ={
    "apiKey": "AIzaSyCY1CKDsoF4frwE9hDv0Cvybc559hUrb70",
    "authDomain": "fstock-9ced2.firebaseapp.com",
    "projectId": "fstock-9ced2",
    "databaseURL": "https://fstock-9ced2-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "fstock-9ced2.appspot.com",
    "messagingSenderId": "956197289236",
    "appId": "1:956197289236:web:a96a757386b39788435601",
    "measurementId": "G-HKY3F089QX"
}

# initilizing pyrebase
firebase = pyrebase.initialize_app(config)

#function to make stock datalist 
def makeStock_data(current,date,stock):
    min = 0 
    max = current
    try:
        min = firebase.child("stock_data").child(stock).child(date).get().value()["min"]
        max = firebase.child("stock_data").child(stock).child(date).get().value()["max"]
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
    

api_list = {"stock":"api"}

while True:
    date = datetime.date(datetime.now())
    day =  date.weekday()
    time = datetime.now().hour
    if day != 5 and day != 6:
        if time >=9 and time <= 15:

            # main database edit here 


            print('aman')
        else:
            #tempory break the sript runs forever
            break



        
# if __name__=="__main__":
    # print(time)


