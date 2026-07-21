import decimal #匯入decimal模組
d1=decimal.Decimal.from_float(123.4567) 
#從資料是浮點數123.4567，使用from_float()方法宣告d1為decimal類型
d2=decimal.Decimal.from_float(34.5678) 
#從資料是浮點數34.5678，使用from_float()方法宣告d2為decimal類型
print(decimal.getcontext()) 
print(decimal.getcontext().prec)
print(decimal.getcontext().rounding)
print(d1+d2) #有效位數為28位
decimal.getcontext().prec=8
print(d1+d2)