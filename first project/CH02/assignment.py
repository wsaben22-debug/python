x=5 #指定x變數值為常值5
y=x #指定y變數值為x的值
print(id(x),id(y)) #顯示變數x,y的記憶體位置
x=3+y #指定x變數值為3+y的值
print(id(x),id(y)) 
a,b=2,3
print(id(a),id(b))
a,b=b,a #交換a,b的值
print(id(a),id(b))