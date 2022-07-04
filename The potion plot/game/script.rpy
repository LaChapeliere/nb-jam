# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define w = Character("Witch")

define m = Character("Andreas")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    w "Things are in debug mode for now, so we don't have to play through everything to access a given chapter"

    w "Just select the chapter you want to access"

    menu:

        "Intro":
            jump intro

        "First monologue":
            jump first_monologue

        "Friendly argument":
            jump friendly_argument

        "Enthusiastic friend":
            jump enthusiastic_friend

        "Shy costumer":
            jump shy_costumer

        "Epilogue":
            jump epilogue

        "Potion minigame":
            jump potions

        "None":
            return


    return

label intro:

    scene bg room

    "This is the intro chapter"

    "*The witch is in a shop, standing at the counter."

    "*The door opens and close."

    "*The first customer, the moose transphobic parent, stand in front of the counter."

    w "Oh, hello Andreas, long time not see!"

    a "Yay, busted my knee on my last hike, I've been stuck at home for the last few weeks..."

    a "But the docs have finally given me the okay to be out and about, I can't wait to get back to work!"

    w "I'm sorry to hear about your knee! I hope you're healing without SEQUELLES?"

    a "Ah, you know me, a little pain isn't going to keep me down..."

    "*Witch react: Eye roll"

    w "Yes, well..."

    w "The usual then?"

    a "Actually, no. Or, I mean, yes, I'll take a crate of Share-A-Dream. But I have a custom order to make today, too."

    w "You are my best customer for those, you know..."

    "*Andreas react: Laughing/joking/chuckle"

    a "Not surprised. I mean, my INPIRATION process relies mostly on them."

    "*A small crate labeled 'Share-A-Dream' with a colourful logo appears on the counter."

    w "Here you are, one crate of Share-A-Dream. What else can I do for you today, then?"

    a "It's a bit... private."

    "*Witch react: Eye roll"

    w "Honestly, Andreas, I'm pretty sure I've heard it all before. I mean, some people even come in there trying to trade their firstborn..."

    a "Right, right, I guess my request isn't that weird. It's definitively not illegal, at least."

    w "Lucky that!"

    a "..."

    a "You remember me telling you about Bruno, right? How he used to be a girl, and I was a bit lost when he transitioned two years ago?"

    w "Yes...?"

    a "Yes, well, I was wondering if you could make a spell, or an amulet or something, to turn him back into a girl."

    "*Witch react: Angry/furious"

    w "..."

    a "No, no, don't look at me like that, I know he's a boy, it's not about me not accepting that!"

    a "But hear me out!"

    w "I honestly don't see how you could justify what you've just asked me for."

    w "But we've known each other for a long time, so I'll give you one chance to convince me not to throw you out of my shop..."

    a "Okay, so he's a boy, but he'll always be a **trans** boy."

    a "And people, they aren't nice. He comes home crying at least once a week because he got bullied at school."

    a "And it's not going to get better, I would know..."

    a "I'm bi. People usually assume I'm straight, because of my wife, but I've been in relationships with guys, too."

    a "I don't know what hit me the hardest, the street harassment or the constant reminders that I was **different** by well-meaning friends and family..."

    "*Andreas react: Sad"

    a "I'm not saying it wasn't worth it, I mean, I loved each of them pretty damn much, I wouldn't have dealt with the homophobia otherwise!"

    a "But I'm still glad that the person I ended up marrying and building a life with is a woman because it makes things so much easier, socially speaking."

    a "I don't want to for my child! I want them to be happy and safe!"

    w "And your plan, to achieve that, is to change who he is, rather than support him and fight for his right to exist?"

    "*Witch reach: Angry/furious"

    a "That's not... I'm supporting him!! I know how much easier my life would have been if I had been straight!"

    w "I can't even...!"

    "*Witch reach: Angry/furious"

    w "Get the hell out of my shop..."

    "*The customer leaves"

    w "And you better set your head straight and check your queerphobia before you set foot here again!"

    "*Door opens and closes"

    w "Asshole!"

    jump start

label first_monologue:

    scene bg room

    "This is the first monologue chapter"

    jump start

label friendly_argument:

    scene bg room

    "This is the friendly argument chapter"

    jump start

label enthusiastic_friend:

    scene bg room

    "This is the enthusiastic friend chapter"

    jump start

label shy_costumer:

    scene bg room

    "This is the shy costumer chapter"

    jump start

label epilogue:

    scene bg room

    "This is the epilogue chapter"

    jump start

label potions:

    "This is the potion minigame"

    jump start
