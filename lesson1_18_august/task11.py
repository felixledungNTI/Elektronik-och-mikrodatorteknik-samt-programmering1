age = int(input("How old are you? "))

if(age < 18):
    print(f"Du är {age} år gammal, och därför omyndig.")
elif(age < 67):
    print(f"Du är {age} år gammal och därför tillräcklig gammal för att jobba.")
else:
    print(f"Du är {age} år gammal, och därför en pensionär. Du bör inte jobba längre.")