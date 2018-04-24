#Created by tariksune
#24.04.2018

number = int(input('Enter your number: ')) 

#Girilen sayının çift veya tek olduğunu if-else içerisinde, o sayının modunu alarak bulabiliriz.

if number%2 == 0: #Dilerseniz 0 değerini 1 ile değiştirip, print kısmını tektir olarak güncelleyebilirsiniz.
    print('Number is even.')
else: #Ilk durum dışında kalan tüm durumlar tek sayıyı belirteceğinden tanımlamamıza gerek yoktur.
    print('Number is odd.')

