import pyrebase
from colorama import Style, Fore, Back
import colorama
from datetime import datetime
colorama.init(autoreset=True)



# initiliging connection to firebase database

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


# function here
def display_logo():
    logo = """
                                                                                                                       
                                                                                                                   
FFFFFFFFFFFFFFFFFFFFFF                       tttt                                               kkkkkkkk           
F::::::::::::::::::::F                    ttt:::t                                               k::::::k           
F::::::::::::::::::::F                    t:::::t                                               k::::::k           
FF::::::FFFFFFFFF::::F                    t:::::t                                               k::::::k           
  F:::::F       FFFFFF ssssssssss   ttttttt:::::ttttttt       ooooooooooo       cccccccccccccccc k:::::k    kkkkkkk
  F:::::F            ss::::::::::s  t:::::::::::::::::t     oo:::::::::::oo   cc:::::::::::::::c k:::::k   k:::::k 
  F::::::FFFFFFFFFFss:::::::::::::s t:::::::::::::::::t    o:::::::::::::::o c:::::::::::::::::c k:::::k  k:::::k  
  F:::::::::::::::Fs::::::ssss:::::stttttt:::::::tttttt    o:::::ooooo:::::oc:::::::cccccc:::::c k:::::k k:::::k   
  F:::::::::::::::F s:::::s  ssssss       t:::::t          o::::o     o::::oc::::::c     ccccccc k::::::k:::::k    
  F::::::FFFFFFFFFF   s::::::s            t:::::t          o::::o     o::::oc:::::c              k:::::::::::k     
  F:::::F                s::::::s         t:::::t          o::::o     o::::oc:::::c              k:::::::::::k     
  F:::::F          ssssss   s:::::s       t:::::t    tttttto::::o     o::::oc::::::c     ccccccc k::::::k:::::k    
FF:::::::FF        s:::::ssss::::::s      t::::::tttt:::::to:::::ooooo:::::oc:::::::cccccc:::::ck::::::k k:::::k   
F::::::::FF        s::::::::::::::s       tt::::::::::::::to:::::::::::::::o c:::::::::::::::::ck::::::k  k:::::k  
F::::::::FF         s:::::::::::ss          tt:::::::::::tt oo:::::::::::oo   cc:::::::::::::::ck::::::k   k:::::k 
FFFFFFFFFFF          sssssssssss              ttttttttttt     ooooooooooo       cccccccccccccccckkkkkkkk    kkkkkkk
        
    
    """
    print(logo)

#live_stock loop function get data
def get_liveStock(stock):
    date = str(datetime.now().date())
    datadict = db.child("stocks").child(stock).child(date).get().val()
    return datadict



def option(id, name):
    print(f"{Fore.RED}[{Fore.GREEN}{id}{Fore.RED}] {Fore.BLUE}{Back.WHITE}{name}")

# function over here






display_logo()
while True:

    print(f"{Fore.GREEN}enter key {Fore.RED}[for quit press q] {Fore.BLUE}or {Fore.GREEN}[for proceed press other key]")
    x = input()
    if x == "q":
        break
    else:
        while True:
            print(f"{Fore.BLUE}{Back.WHITE} [1] stock live")
            x = int(input(f"{Fore.GREEN}{Back.RED}enter the number to get"))
            if x == 0:
                break
            elif(x == 1):
                #live stock loop function 
                stocknameli = list()
                stockli ={
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
                    "tata_steel_limited":"https://in.finance.yahoo.com/quote/TATASTEEL.NS?p=TATASTEEL.NS&.tsrc=fin-srch",}
                n = 1
                for i in stockli:
                    option(n,i)
                    n += 1
                    stocknameli.append(i)
                op = int(input("enter the option"))
                while True:
                    data =  get_liveStock(stocknameli[op-1])
                    min =data['min']
                    max = data['max']
                    current = data['current']
                    print(f"{stockli[op-1]} min:{min} max:{max} current:{current}")