import decimal #匯入decimal模組
f1,f2=10.0,3.0
d1=decimal.Decimal(10) #使用Decimal()發法宣告d1為decimal類型，值為10
d2=decimal.Decimal('3.0')
print(type(d1))
print(f1/f2)
print(d1/d2)
d3=decimal.Decimal('2.345')
d4=decimal.Decimal('6.78')
print(d3+d4) #有效位數為三位
print(d3*d4) #有效位數為五位