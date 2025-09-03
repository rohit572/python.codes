print("WELCOME TO THE ROLLERCOASTER")

height = int(input("What is your height in cm? "))
bill = 0 

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("child tickets are $5.")

    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    else:
        bill = 12
        print("Adult tickets are $12.")

wants_photos = input("Do you wants a photo taken? Y OR N.")

if wants_photos == "Y":
    bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, You have to grow taller before you can ride")
