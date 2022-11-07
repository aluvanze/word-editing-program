sent=input("Enter your sentence\n")
print("*"*10)
sent=sent.lower()
vowels="aeiou"
count=0
while len(sent)>7:
    print("Length of sentence -->",len(sent))
    print("Seventh character:",sent[6])

    break
else:
    print("*"*28)
    print("The sentence is too short")
    print("*"*28)
print("Original ----------------------->",sent)
print("First and last letter removed:-->",sent[1:-1])

sentup=sent.title()
print("Capitalising first letters:----->",sentup)

print("Replacing a wit e:-------------->",sent.replace("a" ,"e"))
for ch in sent:
    if ch in vowels:
        count=1 + count
print("Number of vowels",count)


"coded by Jacob Aluvanze"