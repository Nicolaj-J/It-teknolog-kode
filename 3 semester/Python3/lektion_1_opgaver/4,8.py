def my_input()-> int:
    while True:
        try: 
            x = int(input("Give a number: "))
            return x
        except ValueError:
            print("You didnt give a number")
            print("try again")
        except KeyboardInterrupt:
            print("Keyboardinterrupt")
            break
   
i = my_input()
if i is not None:
    print("My input was: %d" % i)
