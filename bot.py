import random


first_questions = {
    "neo": [
        {"When was neolithic man in Britian?": "5000BC"},
        {"Where can I find the most standing stones?": "Orkney"},
        {"What were neolithic beds like?": "Stone bunks"},
    ]
}


print("Hello, what's your name?")
myname = input("Write your name: ")
print(f"Hello {myname}")
q_and_a = None
if myname == "Special":
    q_and_a = random.choice(first_questions.get("neo"))
    question = list(q_and_a.keys())[0]
answer = q_and_a.get(question)

print(f"{myname},{question}")
input_answer = input("type your answer")
if input_answer == answer:
    print("WoW! I never knew that!")
else:
    print("Really?! Are you sure?")
