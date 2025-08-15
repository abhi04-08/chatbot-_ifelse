

print("Chatbot: Hello I'm a simple chatbot.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hi chatbot"]:
        print("Chatbot: Hello there! How can I help you today?")

    elif user_input in ["how are you", 'how are you doing']:
        print("Chatbot: I'm a chatbot. but I'm fine. How about you?")
    
    elif user_input in ['i am doing good', 'i am fine']:
        print("Chatbot: That's nice! What will we do today?")

    elif "your name" in user_input:
        print("Chatbot: I'm your friendly Python chatbot!")
    
    elif "weather" in user_input:
        print("Chatbot: I'm not sure! But you can check in the weather app.")

    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day")

    else: 
        print("Chatbot: I didn't understand. Can you again rephrase that?")