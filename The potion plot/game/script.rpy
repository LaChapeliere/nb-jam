# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define w = Character("Witch")

define a = Character("Andreas")

define m = Character("Maddie")


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

    w "Oh, hello Andreas, long time no see!"

    a "Yeah, busted my knee on my last hike, I've been stuck at home for the last few weeks..."

    a "But the docs have finally given me the okay to be out and about, I can't wait to get back to work!"

    w "I'm sorry to hear about your knee! I hope you're healing without after-effects?"

    a "Ah, you know me, a little pain isn't going to keep me down..."

    "*Witch react: Eye roll"

    w "Yes, well..."

    w "The usual then?"

    a "Actually, no. Or, I mean, yes, I'll take a crate of Share-A-Dream. But I have a custom order to make today, too."

    w "You are my best customer for those, you know..."

    "*Andreas react: Laughing/joking/chuckle"

    a "Not surprised. I mean, my creative process relies mostly on them."

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

    a "I'm not saying it wasn't worth it, I mean, I damned well loved each of them, I wouldn't have dealt with the homophobia otherwise!"

    a "But I'm still glad that the person I ended up marrying and building a life with is a woman because it makes things so much easier, socially speaking."

    a "I don't want that for my child! I want them to be happy and safe!"

    w "And your plan, to achieve that, is to change who he is, rather than support him and fight for his right to exist?"

    "*Witch react: Angry/furious"

    a "That's not... I'm supporting him!! I know how much easier my life would have been if I had been straight!"

    w "I can't even... Okay, I'll say this once and then you're leaving."

    "*Witch react: Angry/furious"

    w "Set your head straight and check your queerphobia before you set foot here again!"

    w "Now get the hell out of my shop..."

    "+Andreas react: Sad"

    "*The customer leaves"

    "*Door opens and closes"

    w "Asshole!"

    jump start

label first_monologue:

    scene bg room

    "This is the first monologue chapter"

    "*The witch is pacing in zir workshop."

    w "This is so infuriating!"

    w "You spend time and energy educating folks, making sure they understand other people's gender is none of their business..."

    w "...and you {i}think{/i} you've finally gotten the message accross, but then no!"

    w "They go and say some disgusting shit like 'Can you please make my son not trans cause being trans sucks'!"

    w "Want to bet Andreas's feeling self-righteous right now, telling his buddies that I'm an intolerant gender fanatic or something?"

    w "{i}aaaaargh{/i}"

    w "I just want to kick all those transphobic pricks in the guts!"

    w "Bust a few kneecaps..."

    w "Gouge a couple of eyeballs out..."

    "*Heavy sigh"

    w ""

    w "Like I'd ever do that... I'd probably sprain a wing or something..."

    w "Still, it'd feel good to teach them all a lesson!"

    w "Make them understand how confusing your own gender can be, and how gender feels can come from a lot of different things."

    w "..."

    w "Wait a sec..."

    w "I can do that!"

    w "A potion that changes the drinker's gender for a day or so shouldn't be too hard..."

    w "I can use that gender spell I developed when I was a teen, infuse a bunch of ingredients with intent, and then combine them into a potion..."

    w "Let's see... I can use taboo bags for pronouns, for example."

    w "Body parts are easy... Hum, might have to think a bit for things related to behaviours..."

    w "Yes, yes, this is a great idea!!"

    w "I can make a few different potions, build genders that'll confuse the heck out of transphobic bastards!"

    w "It shouldn't be too hard, most of them start panicking whenever someone's facial pilosity or preferred clothing isn't what they expected according to their first name..."

    w "Well, time to get to work, then!"

    jump start

label friendly_argument:

    scene bg room

    "This is the friendly argument chapter"

    "*The witch is in a shop, standing at the counter. Music is playing in the background."

    "*The door opens and close."

    "*The meerkat friend comes in."

    w "Oh hi! Give me a second, I'll turn off the music!"

    "*The music stops"

    "*Maddie react: Grateful"

    m "So, I'm here, what do you need my help with?"

    w "What, not even an 'How're you doing, darling'? I'm hurt, Maddie, really hurt!"

    "*Witch react: Laughing"

    "*Maddie react: Eye roll"

    m "Right, how have you been doing, 'darling', in the last hour since we chatted on the phone?"

    w "Just peachy, thank you! What about you?"

    m "Curious about that big secret project you need me for... Am I finally going to know what this is about?"

    w "Haha, the suspense must be killing you!"

    w "Not literally."

    m "I know, I understood."

    w "Okay, good! So the project..."

    w "I've got this big box of potions here, and I need your help to... distribute it..."

    m "I thought you had a deal with the couriers office next street over for deliveries?"

    w "Yeah, no, not that kind of distribution! For that one, we have to get a lot closer to our... marks..."

    "*Maddie react: Eye roll"

    m "Drop the mystery, W., you're not making any sense."

    w "And you're no fun!"

    "*Witch react: Angry"

    w "But okay, I guess I should explain properly!"

    m "Thank you!"

    w "I had yet another argument with a client couple of days ago, about their son."

    w "Kiddo's trans, but his father'd rather he wasn't, all for his son's happiness of course, so he asked me to make a potion to change their gender 'back'."

    "*Maddie react: Angry"

    w "Yeah, I was pretty furious myself..."

    w "But anyway, it got me thinking... How would all those pricks like it if their gender didn't correspond to their expectations or society's expectations anymore?"

    w "Those potions are my newest invention. They give the drinker another gender for a day, or so."

    w "Just the gender feels, it won't change your body or the clothes you are wearing or anything."

    w "I can't reproduce what it means to **grow up** misgendered, or how soul-draining figuring your gender can be, or any long-term stuff like that, but I can definitively get them to experience the dysphoria and disorientation!"

    w "So I made this bunch, they are all for genders that should confuse the heck out of those obsolete assholes who see people through a binary pink-and-blue lens!"

    w "Only thing that's left to do is for us to discreetly pour them into the drinks of a bunch of partying transphobes at a bar! I'm thinking the Green Monkey, it's close by and they are notoriously anti-trans..."

    m "..."

    m "I..."

    m "Are you serious right now?"

    w "Err, yes?"

    m "You want us to go and drug several dozen people against their consent, with a potion that could have disastrous consequences for their mental health, because it might teach them a lesson? Or is it just for revenge?"

    w "Hum, both?"

    m "And you didn't think I'd object to your plan?"

    w "Err, do you? Object to my plan, I mean?"

    m "Do I... Of course I object! There are so many things wrong with it, I don't even know where to start!"

    "*Maddie react: Angry"

    m "First, I'm not drugging people's drinks! Not matter how asshole-y they are! It's, like, super violent, and illegal, and, and, **not okay**!"

    m "Second, you don't even know that your 'marks', as you say, as transphobes. They could be random people who happen to live or work close by the Green Monkey and have no idea it's a famous anti-queer place."

    m "Like, being that oblivious is not good, sure, but it doesn't they deserve to be punished for it..."

    w "Okay, then let's find a way to target only verified transphobes, or whatever! It's not like we have a shortage of those..."

    m "Did you not hear my first point?"

    "*Witch react: Angry"

    w "Okay, okay, I won't involve you, I'll go take care of it on my own..."

    m "You really shouldn't... And that's my third point: are you doing this for revenge, or to make them empathise with us?"

    m "Because if you think this will be a learning experience for them, I'm going to be honest with you!"

    m "If I was convinced that being trans isn't normal, is maybe an illness or a sin, and a trans activist came and messed with my sense of self for a day, I'd be much more likely to hate and fear trans people as a result than anything else..."

    m "Think about it!"

    w "..."

    w "Okay... Okay, maybe you're right!"

    w "But I was so pissed off with that guy!"

    "*Maddie react: Eye roll"

    w "Well... Guess I should dump those potions down the drain, then..."

    w "It's probably best not to leave them lying around. Especially since they've got to be saturated in negative energies..."

    m "Hum..."

    m "Do you think your potion concept could be applied in a more... helpful way?"

    w "What do you have in mind?"

    m "Well, your process let's you 'build' a gender with various characteristics, right?"

    w "Yeah..."

    m "So, for example, you could create a potion for me to be a woman for a day, and one for me to be agender for a day, and I could compare with how I generally feel."

    m "It might help me figure things out once and for all..."

    m "I'm just sick of just permanently questionning if I'm not just cis and overly complicating things..."

    w "Oh, Maddie!"

    "*Maddie react: Crying"

    w "I can sure make you those potions if you think it could help. I can even make some with various degrees of 'woman-ness' At least that's the theory... And I can tie a lot of parameters to gender euphoria and dysphoria, if you want. Stuff like language and body parts and social perception."

    "*Maddie react: Happy"

    m "That'd be great! Can I come to the back with you so you can show me the options and everything?"

    "*Witch react: Happy"

    w "Sure, come on, let me just lock the front door and we can get brewing!"

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
