list = [0 for x in range(5)]
print('請依序輸入5個整數...')
for i in range(5):
    print(f'輸入第{i+1}個元素內容:',end = '')
    list[i] = eval(input())
max = list[0]
for item in list:
    if max < item :
       max = item 
       
print()
print(f'最大值為{max}')
