#Created by tariksune
#24.04.2018

number1 = input('A = ')
number2 = input('B = ')

#swap öncesi
print('A = {0} ve B = {1}'.format(number1,number2))
print('A ve B sayılarına vermiş olduğunuz değerler değiştiriliyor...')

#Burada bir adet tanım belirlemeliyiz.
#Belirlemiş olduğumuz tanım ile swap olayını gerçekleştireceğiz.

tarik = number1
number1 = number2
number2 = tarik

#tarik tanımına number1 değerini atadık.
#number1 değerine number2 değerini atadık.
#number2 değerine tarik değerini atadık.

#swap sonrası
print('A = {0} ve B = {1}'.format(number1,number2))
