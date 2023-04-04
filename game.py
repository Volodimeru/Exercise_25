import random
def main():
    while True:
        try:
            l = int(input("Level: "))
            if l > 0:
                break
        except:
            pass
    r=random.randint(1,l)
    while True:
        try:
            guess=int(input("Guess: "))
            if guess > 0:
                if r>guess:
                    print("Too small!")
                elif r<guess:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        except:
            pass
main()