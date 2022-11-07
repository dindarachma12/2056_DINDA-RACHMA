import random 
print("===== Hello! Welcome to Number Guessing Game =====") #judul/pembuka permainan
print("Enjoy The Game\n") #pembuka permainan
number_of_trials = 0
number = random.randint(1, 100)
opportunity = 10 #kesempatan yang dapat dilakukan pemain dalam permainan
print("Enter the guess number between 1-100\n")
while number_of_trials< 10: #nomor lebih besar daripada 0
    data = int(input("Enter Guess Numbers: "))
    number_of_trials += 1 #nomor percobaan akan bertamabah
    if data == number :
        print(f"congrats, your guess is true after { number_of_trials} trial")
        break
    if  number_of_trials== 10 and data != number :  #jika kesempatan yang pemain punya telah habis
        print("Your chance is over, you are lost")
        # print(f"The number is {opportunity}")
        # print("Play again")
        break
    elif data > number:
        print("The guess number is bigger")
        print(f"{opportunity - number_of_trials} chance left\n")
        continue
    elif data < number:
        print("The guess number is smaller")
        print(f"{opportunity - number_of_trials}  chance left\n")
        continue