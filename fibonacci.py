
#Fibonacci dizisi hangi terimine kadar yazdırılsın onu giriyoruz.
count_until = int(input("Enter term number: "))
#Burada ilk 2 değeri girdik.Yani 0 ve 1'i manuel ekledik.
value1 = 0
value2 = 1
count = 0

#Burada ilk girdiğimiz değeri kontrol ettiriyoruz.
#Eğer 0'dan küçük sayı girdiksek program hata verecektir.
#if count_until <= 0:
    #print("Enter pozitive number.")

#Yukarıdaki if kodunu çalıştırırsak aşağıdaki if kodu elif olmalı.

if count_until == 1:
    print("Fibonacci sequence to the","(",count_until,")","you entered: ")
    print(value1) # 1 istendiyse 1. değer, yani sıfır yazar.
else:
    print("Fibonacci sequence to the","(",count_until,")","you entered: ")
    while count < count_until:
        print(value1) # with end="" to beside
        new_value = value1 + value2

        #Burada değerleri yeniliyoruz.
        #Yani bir önceki sayıyı bir sonrakine ekledik ve yer değiştirdik.

        value1 = value2
        value2 = new_value
        count += 1
 
