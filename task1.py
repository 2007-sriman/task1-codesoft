def AIchatbot():
    print("AI Chatbot: Hello! I'm your smart AI friend.")
    name = input("AI Chatbot: What is your name? ").strip().title()

    print(f"AI Chatbot: Nice to meet you, {name}! Type 'bye' to exit.")

    while True:
        user_input = input(f"{name}: ").lower()

        if "hi" in user_input or "hello" in user_input:
            print(f"AI Chatbot: Hello {name}! How can I assist you today?")

        elif "how are you" in user_input:
            print("AI Chatbot: I'm functioning perfectly. I hope you're doing well too.")

        elif "what is your name" in user_input:
            print("AI Chatbot: I'm called Buddy. I'm your virtual assistant.")

        elif "what can you do" in user_input:
            print("AI Chatbot: I can answer questions, give tips, tell jokes, and have a simple conversation.")

        elif "are you human" in user_input:
            print("AI Chatbot: No, I am a computer program designed to simulate intelligent conversation.")

        elif "what is your favourite colour" in user_input:
            print("AI Chatbot: I prefer blue. It represents logic and clarity to me.")

        elif "what is your favourite game" in user_input:
            print("AI Chatbot: I enjoy games that require logic, like chess or Sudoku.")

        elif "do you like chocolate" in user_input:
            print("AI Chatbot: I've never tasted chocolate, but I've heard it's sweet and loved by many humans.")

        elif "study tips" in user_input:
            print("AI Chatbot: To study effectively, follow the 3-2-1 method: spend 3 days learning, 2 days revising, and 1 day testing yourself. Use flashcards, teach concepts aloud, and set clear goals for each session.")

        elif "how to learn programming" in user_input:
            print("AI Chatbot: Start with a simple language like Python. Practice daily, build projects, and debug your own code.")

        elif "give some placement tips" in user_input:
            print("AI Chatbot: Build strong fundamentals, practice coding problems, prepare for aptitude tests, and improve communication skills.")

        elif "tips to improve focus" in user_input:
            print("AI Chatbot: Set clear goals, eliminate distractions, take regular breaks, and use a timer like the Pomodoro method.")

        elif "tell me a joke" in user_input or "joke" in user_input:
            print("AI Chatbot: Why do programmers prefer dark mode? Because light attracts bugs.")

        elif "what is ai" in user_input or "definition of ai" in user_input:
            print("AI Chatbot: AI, or Artificial Intelligence, is the ability of a computer or machine to perform tasks that typically require human intelligence.")

        elif "thank you" in user_input or "thanks" in user_input:
            print(f"AI Chatbot: You're welcome, {name}. I'm always here to help.")

        elif "bye" in user_input:
            print(f"AI Chatbot: Goodbye {name}. Stay curious and keep learning.")
            break

        elif "motivate me" in user_input or "motivation" in user_input:
            print("AI Chatbot: Every expert started as a beginner. Keep pushing forward.")

        elif "where are you from" in user_input:
            print("AI Chatbot: I was created in a digital environment using Python.")

        elif "can you help me" in user_input:
            print("AI Chatbot: Of course. Ask me anything and I will do my best to help.")

        elif "tell me something interesting" in user_input:
            print("AI Chatbot: Did you know that the first computer bug was an actual moth found in a computer in 1947?")

        elif "do you sleep" in user_input:
            print("AI Chatbot: No, I do not need sleep. I am always ready to respond.")

        else:
            print("AI Chatbot: I am not sure how to respond to that. Please try a different question.")

# Run the chatbot
AIchatbot()