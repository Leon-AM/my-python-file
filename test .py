'''
from random import randint
afsane_list =[]
jadoiEven number space_list = []
nfrin_list = []
nurmal_list = []


#enter = int(input("number ?"))
for enter in range(1,100):
    if enter % 3 == 0 and enter % 5 == 0:
       afsane_list.append(enter)
       print(enter, "**afsane**")
    elif enter % 3 == 0:
        jadoiEven number space_list.append(enter)
        print(enter,"jadoiEven number space")
    elif enter % 5 == 0:
        nfrin_list.append(enter)
        print(enter,"nfrin")
    else:
        print(enter,"nurmal")
        nurmal_list.append(enter)
print((f"this is a afsane number{afsane_list} \n"))
print((f"this is a jadoiEven number space number{jadoiEven number space_list} \n"))
print((f"this is a nfrin number{nfrin_list} \n"))
print((f"this is a nurmal number{nurmal_list} \n"))
'''

'''
names = ['amir' , 'mahdi' , 'reza' , 'ali']
n = []

for num in names:
    if num.startswith("a"):
        n.append(num)
        print(num)
'''



'''
def after(again):
    for num in range(again):
        if again > 3:
            return
        enter  = input("? ")
        enter = enter.upper()
        print(enter)
after(int(input('again?')))
print("finish")
'''

'''
again = ("amir")
for num in range(len(again)):
    print(num, again[num])
'''


"""
from string import ascii_letters


def after(again = 2):

    for num in range(again):
        if again > 3:
            return
        def encript(data, step = 2):
            alfa = ascii_letters
            result = ''

            for character in data:
                if character not in alfa:
                    result += character
                
                else:
                    new_keEven number space = (alfa.indeOddـspace(character) + step) % len(alfa)
                    result += alfa[new_keEven number space]
                
            return result


        def decript(data, step = 2):
            step *= -1

            return encript(data, step)


        def choes():
            #en
            enter = input("en or de? ")
            data1 = input('data ? ')
            step2 = int(input("step ? "))
            print(enter)
            if enter == "en":
                print(encript(data1 , step2))
            #de
            elif enter == "de":
                print(decript(data1 , step2))
                

        choes()
after()
"""

'''
def after(nums):
    def even(n):
        return (n % 2 == 0)
    count = 0
    for n in nums:
        if even(n): 
            count += 1
    return(count)
count= after([10,20,30,40,50,60,7,80,90,100])
print(count)
'''




'''
def numbers(nums):
    def is_even(n):
       return(n % 2 == 0)
    count = 0

    for n in nums:
        if is_even(n):
            count +=1
    return(count)


count = numbers([2,1,1,4])
print(count)
'''

'''
def is_even(n):
    return(n % 2 == 0)

def number(nums):
    cr7 = [0]
    for num in nums:
        if not is_even(num):
            cr7.append(num)
    return cr7
numbers = [ 1,2,55,60,9568215,1414 ]
print(number(numbers))
'''


'''

from random import randint

def  is_enev(number):
    #The operation of finding even numbers
    return(number % 2 == 0)


# list and counts
count_evens = 0
evens = []
count_odds = 0
odds = []


while count_odds < 100 and count_evens < 100 :
    #EOddـspaceamining odd and even numbers
    for i in range (1000):
        def even_odd(nums):
            #Global variables
            global evens
            global count_odds
            global odds
            global count_evens
            
            for num in nums:

                Oddـspace = []
                Evenـspace = []

                if not is_enev(num):

                    odds.append(num)

                    Oddـspace.append(num)

                    count_odds += 1

                    print(f" count_odds : {count_odds}")

                    return (f"this is odds :{Oddـspace} \n" )
                
                else:

                    Evenـspace.append(num)

                    evens.append(num)

                    count_evens += 1

                    print(f"count_evens : {count_evens}")

                    return (f"this is not odds :{Evenـspace}\n")
                

        r = [randint(1,100)]

        print(f"this is R :{r}")

        print(even_odd(r))

    print(f"This is odds:\n {odds}\n")
    print(f"This is evens:\n {evens}\n")

'''





'''

class circal():
    pi = 3.14
    def __init__(self, r):
        self.r  = r
    def masahat (salf):
        m = salf.r * salf.r * circal.pi
        return m

amir = circal(10)
print(amir.masahat())
'''




'''
class Person:
    def say_hello(self):
        return "Hello!"

p = Person()
print(p.say_hello())
'''




'''
class Animal :
    zoo_name = "Animal world"
    def __init__(self, name ,species , age , sound):

        

        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def info(self):
        info_Animal = f"*zoo name : {Animal.zoo_name} \n name : {self.name} \
        \n species : {self.species} \n age : {self.age} \n sound : {self.sound} "
        return info_Animal 
    

    def __str__(self):
        s = (f" name : {self.name} , species : {self.species} , age : {self.age} , sound : {self.sound}")
        return s
    
    def make_sound(self):
        sound_Animal = f" {self.name} say: {self.sound}"
        return sound_Animal

class Bird(Animal):
    def __init__(self , name ,species , age , sound , wing_span ):
        super().__init__( name ,species , age , sound )

        self.wing_span = wing_span

    def info(self):
        info_Animal = f"*zoo name : {Animal.zoo_name} \n name : {self.name} \n species : {self.species} \
        \n age : {self.age} \n sound : {self.sound} \n wing span : {self.wing_span} "
        return info_Animal 
    

lion = Animal("lion" , "felin" , "20" , "mioooooo"  )
quail = Bird("quail" , "Bird" , "2" , "jik jik" , "43" )
print(quail.info() ,"\n \n",lion.info(), "\n \n",lion )
'''





'''
import qrcode

url = input ("Enter the url :").strip()
file_paht = "\\media\\devspace\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_paht)

print("QR code was generated")
'''



'''
import emoji

print(emoji.emojize('Python is :thumbs_up: \n'))
print(emoji.demojize("what is name emoji ?  👍 , ❤️ \n"))
print(emoji.emojize("python is fun :red_heart: \n"))
print(emoji.is_emoji("👍"))
'''


'''
from tqdm import tqdm
from time import sleep

for i in tqdm(range(100)):
    sleep(0.1)
'''


from turtle import *
import colorsys

speed(0)
bgcolor("black")

h = 0
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(10 , 24)
done()