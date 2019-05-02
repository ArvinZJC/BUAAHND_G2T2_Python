# 第2章.pptx, P96 - 111, program that uses dictionaries

dictionary1 = {"Name" : "Tim", "Sex" : "Male", "Age" : "18", "Score" : "80"}
print(dictionary1)
print(len(dictionary1))
print(dictionary1["Name"], end = "\n\n")

dictionary1["Score"] = "59"
print(dictionary1, end = "\n\n")

dictionary2 = {"Pass (Y/N)" : "N"}
dictionary1.update(dictionary2)
print(dictionary1, end = "\n\n")

dictionary1.pop("Sex")
print(dictionary1, end = "\n\n")

if "name" in dictionary1: 
    print(dictionary1["name"], end = "\n\n")
else:
    print("No such key.", end = "\n\n")

for key in dictionary1.keys():
    print('The value of the key "' + key + '": ' + dictionary1[key])

print("\r")

for value in dictionary1.values():
    print(value)

print("\r")

for (key, value) in dictionary1.items():
    print("dictionary1[%s] =" %key, value)

print("\r")

dictionary1.clear()
print(dictionary1, end = "\n\n")

dictionary1 = {"Name" : {"First" : "Johney", "Last" : "Lee"}, "Age" : "40"}
print(dictionary1["Name"]["First"])