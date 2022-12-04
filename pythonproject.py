currency={"USD":81,"EUR":83.75,"INR":1,'CAD':60.89,'AUD':54.14,'SGD':59.29,'JPY':0.579,'CNY':11.41,'PKR':0.361,'NPR':0.62,'XOF':0.128,'MXN':4.18795,'ARS':0.5,'SEK':7.63,'DKK':11.26,'VND':0.00329}
def convert(c1,a,c2):
    if(c2=="INR"):
        print("The Currency After Converting into %s is"%c2,(amount*currency[c1]))
    elif(c1=="INR"):
        print("The Currency After Converting into %s is"%c2,(amount/currency[c2]))
    else:
        print("The Currency After Converting into %s is"%c2,(amount/currency[c1])*currency[c2])



print(" ---------------------- ")
print("|  Currency Converter  |")
print(" ---------------------- ")
for i in currency.keys():
    print(i)
c1=input("Enter The Currency: ")
amount=eval(input("Enter The Amount: "))
c2=input("Enter The Currency you want to convert to: ")
convert(c1,amount,c2)
