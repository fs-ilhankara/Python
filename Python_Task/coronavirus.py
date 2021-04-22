deger = {"No": False, "Yes": True}

age = deger[input("Are you a cigarette addict older than 75 years old? Yes or No\n").capitalize()]
chronic = deger[input("Do you have a severe chronic disease? Yes or No\n").capitalize()]
immune = deger[input("Is your immune system too weak? Yes or No\n").capitalize()]

if (age or chronic or immune) == True:
    print("You are in risky group")
else:
    print("You are not in risky group")