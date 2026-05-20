score = 0
answer = input("1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct Answer")
    score = score + 1
else:
    print("Wrong Answer")

answer = input("2. Who is known as the Father of Computers? ")

if answer.lower() == "charles babbage":
    print("Correct Answer")
    score = score + 1
else:
    print("Wrong Answer")

answer = input("3. Which planet is known as the Red Planet? ")

if answer.lower() == "mars":
    print("Correct Answer")
    score = score + 1
else:
    print("Wrong Answer")

print("\nYour Final Score is:", score)