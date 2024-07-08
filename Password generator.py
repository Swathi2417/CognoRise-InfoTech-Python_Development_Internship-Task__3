import random as rd
letter="abcdefghijklmnopqrstuvwxyz"
number="0123456789"
complex_characters="#@$&%-_"

k=[]
def generate_password():
    def user_input():
        a=int(input("Enter the Password Length:\n"))

        for i in range(0,a):
            r=rd.randint(0,len(letter)-1)
            k.append(letter[r])

        for j in range(0,3):
            x1=rd.randint(0,len(number)-1)
            k.append(number[x1])
        print(k)

    user_input()

def generate_complex_password():
    for i in k:
        #print(f"{i},{x.index(i)}")
        index1=rd.randint(0,len(k)-1)
        if k.index(i)<= index1:
            #print(f"{i},{index1}")
            k.remove(i)
            k.insert(index1,i)
        break

    for i in complex_characters:
        r=rd.randint(0,1)
        k.append(complex_characters[r])
        break
    print("Your Strong Password\n",k)

generate_password()
complex=str(input("Do you want to make it more Complex ? Y/N\n"))
for i in range(0,3):
    if isinstance(complex,str) and complex.lower() == "y":
        generate_complex_password()
        #print("Y")
    elif isinstance(complex,str) and complex.lower() == "n":
        #print("N")
        print("Your Generated Password\n",k)
    else:
        print("Incorrect Input..\nTRY AGAIN")
        complex=str(input("Do you want to make it more Complex ?\nY/N\n"))
        continue
    break
