import random

def generate_quote():
    quotes = [
        "There are no more barriers to cross. All I have in common with the uncontrollable and the insane, the vicious and the evil, all the mayhem I have caused and my utter indifference toward it I have now surpassed.",
        "I have all the characteristics of a human being: flesh, blood, skin, hair; but not a single, clear, identifiable emotion, except for greed and disgust.",
        "I'm into, uh, suits. And, uh, the music of Huey Lewis and the News. I'm a pretty simple guy, really.",
        "There is an idea of a Patrick Bateman, some kind of abstraction, but there is no real me, only an entity, something illusory. And though I can hide my cold gaze, and you can shake my hand and feel flesh gripping yours and maybe you can even sense our lifestyles are probably comparable... I simply am not there.",
        "I'm not a moral person, I'm a barely functioning social climber.",
        "I like to dissect girls. Did you know I'm utterly insane?",
        "I'm into, uh, well, murders and executions, mostly.",
        "TRY GETTING A RESERVATION AT DORSIA NOW, YOU FUCKING STUPID BASTARD! YOU, FUCKING BASTARD!",
        "You're a fucking ugly bitch. I want to stab you to death, and then play around with your blood.",
        "I know that your friends are my friends and, uh... I've thought about that. You can have 'em.",
        " No... I'm in touch with humanity.",
        "My need to engage in homicidal behaviour on a massive scale cannot be corrected but, uh, I have no other way to fulfill my needs.",
        "When I see a pretty girl walking down the street, I think two things. One part wants me to take her out, talk to her, be real nice and sweet and treat her right.........and What her head would look like on a stick... (laughs) ",
        " Well, you can always be thinner... look better.",
        " Look at that subtle off-white coloring. The tasteful thickness of it. Oh my God, it even has a watermark!",
        " I have to return some videotapes",
        "There are no girls with good personalities."
    ]
    return random.choice(quotes)

print("Welcome to the Patrick Bateman quote generator!")
while True:
    print("\nHere is a quote from Patrick Bateman:")
    print(generate_quote())
    print("\nWould you like another quote? (y/n)")
    response = input()
    if response.lower() == "n":
        break
print("Goodbye!")
