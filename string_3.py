letter='''Dear<|Name|>,
You are selected!
   <|Date|>'''
print(letter.replace("<|Name|>","Harry").replace("<|Date|>","12/12/2027"))
#replace chaining
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes