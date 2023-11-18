from random import choice

def generate(r:list):
    ask = input("QUESTION: ")
    if ask.strip() == "": generate(r)
    elif ask in ['`', 'exit', 'e', 'x']: quit()

    res = choice(r)
    print("RESPONSE: " + res+"\n")
    
    generate(r)

if __name__ == "__main__":
    print("\n8 Ball Program by Len.icon\nFor Vod")
    print("\nAsk me an advisory question...")
    responses = [
        "Yes, definitely.",
        "Without a doubt.",
        "Most likely.",
        "Yes, but ask again later.",
        "Ask again later.",
        "Cannot predict now.",
        "Don't count on it.",
        "Very doubtful."
    ]

    generate(responses)