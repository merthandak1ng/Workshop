
# FOR LOOP


citys = ['Ankara',"İstanbul",'İzmir']
print(citys[0])
print(citys[1])
print(citys[2])

for city in citys:
  
        print(city + " for code = " + city[0:3])
        
        
        
# WHİLE LOOP


connector = 1
result = 0

while connector<=10:
    result = result + connector
    connector = connector + 1
    
print(result)


#%% FOR RANGE

#  1 DEN 9 A KADAR OLAN SAYILAR

for x in range(1,10):
    print(x)
    
# 1 DEN 99 A KADAR OLAN TEK SAYILAR

for x in range(1,100,2):
      print(x)
# 0 DAN 100 E KADAR OLAN ÇİFT SAYILAR

for x in range(0,102,2):
    print(x)