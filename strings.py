# -*- coding: utf-8 -*-
#Substring
message = "Merhaba Dünya"
print(message[7:11])
newmessage = message[12:13]
print(newmessage)

print(len(message))

#len
newmessage2 = message[len(message)-1:len(message)]
print(newmessage2)


#lower upper
print(message.upper())
print(message.lower())

#Replace

#print(message.replace("ü", "u"))
print(message.replace("a", "e"))


#split and strip
bilgi = "Mert Han;Sivas ".strip()
print(bilgi.split())
print("Adı =" + bilgi.split(";")[2])


#input

ad = input("adınız?")
sayi1 = input("sayı 1 =?")
sayi2 = input("sayı 2 =?")
print(int(sayi1) + int(sayi2))
