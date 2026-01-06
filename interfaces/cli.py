from core.ai import ask_ai

def run_cli():
    print("AI Assistant CLI (type exit)")
    while True:
        text = input("You: ")
        if text.lower() == "exit":
            break
        answer = ask_ai(text)
        print("AI:", answer)