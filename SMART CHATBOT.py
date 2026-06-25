from datetime import datetime

print("===== SMART CHATBOT =====")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How can I help you?")
        
    elif user == "how are you":
        print("Bot: I am doing great!")
        
    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current Time is", current_time)

    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date is", current_date)

    elif user == "internship":
        print("Bot: CodeAlpha offers internships in Python, AI, Web Development and Data Science.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")