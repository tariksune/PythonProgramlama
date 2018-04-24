#Created by tariksune
#24.04.2018


number1 = input('Enter your first number: ') #Ilk değerimizi alıyoruz.
number2 = input('Enter your second number: ') #Ikinci değerimizi alıyoruz.

add = int(number1)+int(number2) #Bu kısımlar 4 işlemin yapıldığı yerler dilediğiniz gibi veri tipi değişikliği yapabilirsiniz.
sub = int(number1)-int(number2)
mul = int(number1)*int(number2)
div = float(number1)/float(number2)

#Seçim ekranı yazdırıyoruz.
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
choose = int(input('Please select your process: ')) #User'dan seçim yapmasını istiyoruz.

#Eğer yapılan seçim 1,2,3,4 ise aşağıda verilen yazdırma işlemleri yapılacaktır.
if choose == 1 :
    print('{0} + {1}: {2}'.format(number1,number2,add))
elif choose == 2:
    print('{0} - {1}: {2}'.format(number1,number2,sub))
elif choose == 3:
    print('{0} * {1}: {2}'.format(number1,number2,mul))
elif choose == 4:
    print('{0} / {1}: {2}'.format(number1,number2,div))

#Eğer yapılan seçim 1,2,3,4 dışında bir sayı ise hata mesajı yayınlanacaktır.
else:
    print('Error!')
