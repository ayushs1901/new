def chatbot():
    """Simple chatbot that replies with 'hi'"""
    print("Chatbot: Hi! Type something or 'quit' to exit")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("Chatbot: Goodbye!")
            break
        elif user_input.lower() == 'bye':
            print("Chatbot: Bye!")
            break
        elif user_input:
            print("Chatbot: Hi")
        else:
            print("Chatbot: Hi")

if __name__ == "__main__":
    chatbot()
