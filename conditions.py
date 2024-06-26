age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
    
elif 18 <= age <= 65:
    print("You are an adult.")
    
else:
    print("you are a senior citizen.")
    
    
    
    
    
    
    
    
    def condition(age):
     if age < 18:
        return"You are a minor."
     elif 8 <= age <= 65:
        return "You are an adult."
     else:    
         return"You are a senior citizen."

print(condition(15))
print(condition(35))  
print(condition(70))















