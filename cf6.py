import pandas as pd
import numpy as np
import datetime as dt

date = input("Enter a date in YYYY/MM/DD format: ") #enter date in exact format
year, month, day = map(int, date.split('/')) #maps variables based on the "/"
dtformat = dt.date(year, month, day) #set these variables into date format


#Enter inputs for principal, interest, coupon, and years(n)
prin = float(input("Enter your principal amount: ")) 
rate = float(input("Enter your interest amount: ")) 
coupon = float(input("Enter the coupon: " ))
n = int(input("Enter the amount of years: "))

date2 = np.arange(month, n  * 12 + 1)

#Formulas
months = np.arange(1, n * 12 + 1) #np.numpy([start], stop, [step], dtype = None) 
principal = np.ppmt(rate/12, months, n * 12, prin) #principal ( np.ppmt(rate, per, nper, pv, fv=0, when='end'))
interest = np.ipmt(rate/12, months, n * 12, prin) #interest
pmt = np.pmt(rate/12, n * 12, prin) #payment
wac = rate * 100 #constant throughout all periods 
#df['future date'] = plus_month_perod.astype("timedelta64[M]") 

def balance(pv, r, n, p):
    dfac = (1+r/12) ** n
    return pv * dfac - p * (dfac - 1) / (r / 12)


#Display Table Output (Excel CSV file)
table = pd.DataFrame({'Period': months, 
#                      'Date': dtformat + pd.offsets.MonthOffset(plus_month_period),
                      'Performing Balance' : balance(prin, rate, months - 1, -pmt),
                      'WAC': wac,
#                      'WAM': ,
                      'Principal' : -principal,
                      'Interest' : -interest,
                      'P&I' : -principal + -interest, 
                      'End Balance' : balance(prin, rate, months, -pmt)}, index=months)

assert np.allclose(table['End Balance'].tail(1), 0)

export_csv = table.to_csv(r'C:\Users\hdang\Documents\Export DataFrame\csvtest.csv',index=None, header=True) #exports to CSV file

print(table.round(2))

