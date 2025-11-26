from string import ascii_letters


def after(again = 2):

    for i in range(again):
        if again > 3:
            return
        def encript(data, step = 2):
            alfa = ascii_letters
            result = ''

            for character in data:
                if character not in alfa:
                    result += character
                
                else:
                    new_key = (alfa.index(character) + step) % len(alfa)
                    result += alfa[new_key]
                
            return result


        def decript(data, step = 2):
            step *= -1

            return encript(data, step)


        def choes():
            #en
            enter = input("encript/en or decript/de ? ")
            data1 = input('data ? ')
            step2 = int(input("step ? "))
            if enter == "en":
                print(f"This is encript data : {encript(data1 , step2)}")
            #de
            elif enter == "de":
                print(f"This is decript data : {decript(data1 , step2)}")
                

        choes()
after()