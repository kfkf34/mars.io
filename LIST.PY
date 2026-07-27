LIST=['']
r = int(input("Enter the range of animals you want to add: "))
for i in range(r):
    name_of_animal = input("Enter the name of an animal: ")
    LIST.append(name_of_animal)

for animal in LIST:
    print(animal + " is a farm animal.")
