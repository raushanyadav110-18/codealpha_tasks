import datetime


# Get the current time
def get_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%I:%M %p")


# Get today's date
def get_date():
    current_date = datetime.datetime.now()
    return current_date.strftime("%d-%m-%Y")


# Display available commands
def show_help():
    print("\n========== HELP ==========")
    print("You can ask me:")
    print("1. Hello / Hi")
    print("2. How are you?")
    print("3. What is your name?")
    print("4. What can you do?")
    print("5. What time is it?")
    print("6. What is today's date?")
    print("7. Help")
    print("8. Bye / Goodbye")
    print("==========================\n")


# Generate chatbot response
def get_response(user_input):

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! Nice to meet you. How can I help you?"

    elif user_input == "how are you":
        return "I'm doing great! Thanks for asking."

    elif user_input in ["what is your name", "your name"]:
        return "My name is CodeBot. I am a basic Python chatbot."

    elif user_input in ["what can you do", "your capabilities"]:
        return "I can have basic conversations, tell you the current time and date, and respond to common questions."

    elif user_input in ["time", "what time is it"]:
        return f"The current time is {get_time()}."

    elif user_input in ["date", "what is today's date", "today's date"]:
        return f"Today's date is {get_date()}."

    elif user_input == "help":
        show_help()
        return None

    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day. 👋"

    elif user_input == "":
        return "Please type something."

    else:
        return "Sorry, I don't understand that yet."


# Main chatbot function
def chatbot():

    print("=" * 45)
    print("           WELCOME TO CODEBOT")
    print("=" * 45)
    print("Bot: Hello! I am CodeBot 🤖")
    print("Bot: Type 'help' to see what I can do.")
    print("Bot: Type 'bye' to exit.")

    while True:

        try:
            user_input = input("\nYou: ").strip().lower()

            response = get_response(user_input)

            # Help function already prints its own output
            if response is not None:
                print("Bot:", response)

            # Stop the chatbot when user says goodbye
            if user_input in ["bye", "goodbye", "exit"]:
                break

        except KeyboardInterrupt:
            print("\nBot: Goodbye! 👋")
            break

        except Exception as error:
            print("Bot: Something went wrong.")
            print("Error:", error)


# Start the chatbot
if __name__ == "__main__":
    chatbot()