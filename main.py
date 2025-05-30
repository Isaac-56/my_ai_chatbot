# chatbot.py

def get_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi there! 👋 How can I help you today?",
        "hi": "Hello! 😊 What would you like to talk about?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm GenBot, your first AI chatbot. 🤖",
        "bye": "Goodbye! 👋 Hope to chat with you again soon.",
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "I'm not sure how to respond to that yet. Can you ask something else?"

def main():
    print("Welcome to GenBot! Type something to begin (type 'bye' to exit).")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("GenBot: Goodbye! 👋")
            break
        response = get_response(user_input)
        print("GenBot:", response)

if __name__ == "__main__":
    main()
