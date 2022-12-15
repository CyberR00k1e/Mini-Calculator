import json

#a=input("enter your answer")
with open("Questions.json", "r") as file:
    content = file.read()

data =  json.loads(content)
score=0
for i in data:
    print(i["text"])
    for a,b in enumerate(i["options"]):
        print(f"{a+1}.{b}")
    ans=input("your answer")
    if ans==i["correct_answer"]:
        score=score+1
        print("correct answers!!")

print("-------"+"\n")
print(f"your total score is {score}")




