import time
import random
print("Welcome to MoodAI!")
time.sleep(2)
print("This noble and cutie helper is created to analyze your mood and give you a randomized advice afterwards.")
time.sleep(2)
print("(And to pass this year's class with an acceptable point, of course...)")
time.sleep(2)
print("This system doesn't exactly use Artificial Intelligence, but according to our conclusions, it is considered as AI since we use analyzing and randomized returns.")
time.sleep(2)
print("Which means, this is the base of AI's way of thinking without machine learning.")
time.sleep(2)
print("Please answer our questions with the numbers amongst 0-5.")


low_mood_advice = [
    "Listen to the best song you've ever heard to get some dopamine.",
    "Take a break from screens and go touch grass until you get bored.",
    "Meditate for at least 5 minutes. If you don't know how to, learn it.",
    "Let out anything you feel like you're keeping inside. I mean, crying is always okay..."
]

neutral_mood_advice = [
    "Go for a short walk without earphones.",
    "Text someone, ask how they are, maybe you can chit-chat a bit.",
    "Take a break from everything and take time for your hobbies.",
    "Try writing whatever comes to your mind until you get bored."
]

good_mood_advice = [
    "Use your energy for something creative.",
    "Exercise to keep your mood at this level.",
    "Chech your to-do list and find something you can complete and erase from there.",
    "Hang out with someone you've forgotten to talk to lately."
]



while True:
    try:
        stress = int(input("How stressed are you right now? (0-5): "))
        if 0 <= stress <= 5:
            break
        else:
            print("Please enter a number BETWEEN 0 AND 5...")

    except ValueError:
        print("Invalid input. Please ENTER a NUMBER.")

#  sacma sapan errorlar vermesin diye bi kacis yolu veriyoruz


while True:
    try:
        work = int(input("How much tiring was your work/whatever responsibility today? (0-5):"))
        if 0<= work <= 5:
            break
        else:
            print("Please enter a number BETWEEN 0 AND 5...")

    except ValueError:
        print("Invalid input. Please ENTER a NUMBER.")



while True:
    try:
        sleep = int(input("How 'poor quality' your sleep has been lately? (0-5):"))
        if 0<= sleep <= 5:
            break
        else:
            print("Please enter a number BETWEEN 0 AND 5...")

    except ValueError:
        print("Invalid input. Please ENTER a NUMBER.")



while True:
    try:
        alonetime = int(input("Last question: How much alone time do you want right now? (0-5):"))
        if 0<= alonetime <= 5:
            break
        else:
            print("Please enter a number BETWEEN 0 AND 5...")

    except ValueError:
        print("Invalid input. Please ENTER a NUMBER.")



average = (stress + work + sleep + alonetime) / 4

print("Okay. Well...")
time.sleep(2)
print("Hmm...")
time.sleep(2)
print("Calculating...")
time.sleep(2)
print("Preparing...")
time.sleep(2)
print("Your bad mood is:", average, "out of 5.")

if average <= 2:
    print("Yay!! Seems like you're in a good mood!")
    time.sleep(2)

    while True:
        print("Here is your advice:")
        time.sleep(2)
        print(random.choice(good_mood_advice))

        again = input("Do you want another advice? The result may repeat because we were too lazy to add another feature. (yes/no): ").lower()

        if again != "yes":
            break


elif average <= 3.5:
    print("Take your time. It happens to the best of us sometimes:(")
    time.sleep(2)
    while True:
        print("Here is your advice:")
        time.sleep(2)
        print(random.choice(neutral_mood_advice))

        again = input("Do you want another advice? The result may repeat because we were too lazy to add another feature. (yes/no): ").lower()

        if again != "yes":
            break

else:
    print("Are you sure you're okay, bro?")
    time.sleep(2)
    while True:
        print("Here is your advice:")
        time.sleep(2)
        print(random.choice(low_mood_advice))

        again = input("Do you want another advice? The result may repeat because we were too lazy to add another feature. (yes/no): ").lower()

        if again != "yes":
            break
