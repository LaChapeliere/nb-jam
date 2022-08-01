﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define w = Character("Witch")

image witch front:
    "images/witch front.png"
    zoom 0.43

transform witch_shop_react:
    xalign 0.87
    yalign 0.06
    xzoom -1.0


define a = Character("Andreas")

image andreas back:
    "images/andreas back.png"
    zoom 0.52

transform andreas_react:
    xalign 0.27
    yalign 0.17


define m = Character("Maddie")

image maddie back:
    "images/maddie back.png"
    zoom 0.37

transform maddie_react:
    xalign 0.39
    yalign 0.16


define f = Character("Farah")

image farah back:
    "images/farah back.png"
    zoom 0.4

transform farah_react:
    xalign 0.37
    yalign 0.20


image react angry:
    "angry/angry1.png"
    0.1 #this part defines how long to wait before next frame
    "angry/angry2.png"
    0.1
    repeat

image react eyeroll:
    "eyeroll/eyeroll1.png"
    0.1 #this part defines how long to wait before next frame
    "eyeroll/eyeroll2.png"
    0.1
    "eyeroll/eyeroll3.png"
    0.1
    "eyeroll/eyeroll4.png"
    0.1
    repeat

image react happy:
    "gratefulA/grateful1.png"
    0.1 #this part defines how long to wait before next frame
    "gratefulA/grateful2.png"
    0.1
    repeat

image react flower:
    "gratefulB/grateful1.png"
    0.1 #this part defines how long to wait before next frame
    "gratefulB/grateful2.png"
    0.1
    repeat

image react laugh:
    "hahaha/laugh1.png"
    0.1 #this part defines how long to wait before next frame
    "hahaha/laugh2.png"
    0.1
    repeat

image react sad:
    "sad/sad1.png"
    0.1 #this part defines how long to wait before next frame
    "sad/sad2.png"
    0.1
    repeat

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg intro small

    pause

    "Content warning: transphobia, mention of drugging drinks."

    jump intro


label intro:

    play music poisonloop fadein 5.0

    scene bg shop small
    show witch front:
        xalign 0.70
        yalign 0.22
    show counter small
    with fade

    play sound "/audio/SFX_DoorOpen.wav"
    queue sound "/audio/SFX_DoorClose_Light.wav"
    pause 0.6

    show andreas back:
        xalign 0.4
        yalign 0.41
    with moveinright

    w "Oh, hello Andreas, long time no see!"

    a "Yeah, busted my knee on my last hike, I've been stuck at home for the last few weeks..."

    a "But the docs have finally given me the okay to be out and about, I can't wait to get back to work!"

    w "I'm sorry to hear about your knee! I hope you're healing without after-effects?"

    a "Ah, you know me, a little pain isn't going to keep me down..."

    show react eyeroll at witch_shop_react

    w "Yes, well..."

    hide react

    w "The usual then?"

    a "Actually, no. Or, I mean, yes, I'll take a crate of Share-A-Dream. But I have a custom order to make today, too."

    w "You are my best customer for those, you know..."

    show react laugh at andreas_react

    a "Not surprised. I mean, my creative process relies mostly on them."

    hide react

    w "Here you are, one crate of Share-A-Dream. What else can I do for you today, then?"

    a "It's a bit... private."

    show react eyeroll at witch_shop_react

    w "Honestly, Andreas, I'm pretty sure I've heard it all before. I mean, some people even come in there trying to trade their firstborn..."

    hide react

    a "Right, right, I guess my request isn't that weird. It's definitively not illegal, at least."

    w "Lucky that!"

    a "..."

    a "You remember me telling you about Bruno, right? How he used to be a girl, and I was a bit lost when he transitioned two years ago?"

    w "Yes...?"

    a "Yes, well, I was wondering if you could make a spell, or an amulet or something, to turn him back into a girl."

    show react angry at witch_shop_react

    w "..."

    hide react

    a "No, no, don't look at me like that, I know he's a boy, it's not about me not accepting that!"

    a "But hear me out!"

    w "I honestly don't see how you could justify what you've just asked me for."

    w "But we've known each other for a long time, so I'll give you one chance to convince me not to throw you out of my shop..."

    a "Okay, so he's a boy, but he'll always be a {b}trans{/b} boy."

    a "And people, they aren't nice. He comes home crying at least once a week because he got bullied at school."

    a "And it's not going to get better, I would know..."

    a "I'm bi. People usually assume I'm straight, because of my wife, but I've been in relationships with guys, too."

    a "I don't know what hit me the hardest, the street harassment or the constant reminders that I was {b}different{/b} by well-meaning friends and family..."

    show react sad at andreas_react

    a "I'm not saying it wasn't worth it, I mean, I damned well loved each of them, I wouldn't have dealt with the homophobia otherwise!"

    hide react

    a "But I'm still glad that the person I ended up marrying and building a life with is a woman because it makes things so much easier, socially speaking."

    a "I don't want that for my child! I want them to be happy and safe!"

    w "And your plan, to achieve that, is to change who he is, rather than support him and fight for his right to exist?"

    show react angry at witch_shop_react

    a "That's not... I'm supporting him!! I know how much easier my life would have been if I had been straight!"

    w "I can't even... Okay, I'll say this once and then you're leaving."

    w "Set your head straight and check your queerphobia before you set foot here again!"

    w "Now get the hell out of my shop..."

    hide react

    show react sad at andreas_react

    pause 1

    hide react

    hide andreas
    with moveoutright

    play sound "/audio/SFX_DoorOpen.wav"
    queue sound "/audio/SFX_DoorClose_Hard.wav"
    pause 0.6

    w "Asshole!"

    jump first_monologue

label first_monologue:

    scene bg workshop small
    hide witch
    hide counter
    with fade

    show witch front:
        xalign 0.5
        yalign 0.75
    with moveinright

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

    w "..."

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

    jump potion_placeholder


label potion_placeholder:

    stop music fadeout 1.0

    hide witch
    scene bg intro small
    with fade

    "{b}This was supposed to be a minigame to make Build-A-Gender potions, but Life happened...{/b}"

    jump friendly_argument


label friendly_argument:

    play music poisonloop fadein 0.5

    scene bg shop small
    show witch front:
        xalign 0.70
        yalign 0.22
    show counter small
    with fade

    play sound "/audio/SFX_DoorOpen.wav"
    queue sound "/audio/SFX_DoorClose_Light.wav"
    pause 0.6

    show maddie back:
        xalign 0.53
        yalign 0.53
    with moveinright

    w "Oh hi! Give me a second, I'll turn off the music!"

    stop music

    show react happy at maddie_react

    m "So, I'm here, what do you need my help with?"

    hide react

    w "What, not even an 'How're you doing, darling'? I'm hurt, Maddie, really hurt!"

    show react laugh at witch_shop_react

    pause 1

    show react eyeroll at maddie_react

    m "Right, how have you been doing, {i}darling{/i}, in the last hour since we chatted on the phone?"

    hide react

    w "Just peachy, thank you! What about you?"

    m "Curious about that big secret project you need me for... Am I finally going to know what this is about?"

    w "Haha, the suspense must be killing you!"

    w "Not literally."

    m "I know, I understood."

    w "Okay, good! So the project..."

    w "I've got this big box of potions here, and I need your help to... distribute it..."

    m "I thought you had a deal with the couriers office next street over for deliveries?"

    w "Yeah, no, not that kind of distribution! For that one, we have to get a lot closer to our... marks..."

    show react eyeroll at maddie_react

    m "Drop the mystery, W., you're not making any sense."

    hide react

    w "And you're no fun!"

    show react angry at witch_shop_react

    w "But okay, I guess I should explain properly!"

    hide react

    m "Thank you!"

    w "I had yet another argument with a client couple of days ago, about their son."

    w "Kiddo's trans, but his father'd rather he wasn't, all for his son's happiness of course, so he asked me to make a potion to change their gender {i}back{/i}."

    show react angry at maddie_react

    w "Yeah, I was pretty furious myself..."

    hide react

    w "But anyway, it got me thinking... How would all those pricks like it if their gender didn't correspond to their expectations or society's expectations anymore?"

    w "Those potions are my newest invention. They give the drinker another gender for a day, or so."

    w "Just the gender feels, it won't change your body or the clothes you are wearing or anything."

    w "I can't reproduce what it means to {b}grow up{/b} misgendered, or how soul-draining figuring your gender can be, or any long-term stuff like that, but I can definitively get them to experience the dysphoria and disorientation!"

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

    show react angry at maddie_react

    m "First, I'm not drugging people's drinks! Not matter how asshole-y they are! It's, like, super violent, and illegal, and, and, {b}not okay{/b}!"

    m "Second, you don't even know that your 'marks', as you say, as transphobes. They could be random people who happen to live or work close by the Green Monkey and have no idea it's a famous anti-queer place."

    hide react

    m "Like, being that oblivious is not good, sure, but it doesn't they deserve to be punished for it..."

    w "Okay, then let's find a way to target only verified transphobes, or whatever! It's not like we have a shortage of those..."

    m "Did you not hear my first point?"

    show react angry at witch_shop_react

    w "Okay, okay, I won't involve you, I'll go take care of it on my own..."

    hide react

    m "You really shouldn't... And that's my third point: are you doing this for revenge, or to make them empathise with us?"

    m "Because if you think this will be a learning experience for them, I'm going to be honest with you!"

    m "If I was convinced that being trans isn't normal, is maybe an illness or a sin, and a trans activist came and messed with my sense of self for a day, I'd be much more likely to hate and fear trans people as a result than anything else..."

    m "Think about it!"

    w "..."

    w "Okay... Okay, maybe you're right!"

    w "But I was so pissed off with that guy!"

    show react eyeroll at maddie_react

    w "Well... Guess I should dump those potions down the drain, then..."

    hide react

    w "It's probably best not to leave them lying around. Especially since they've got to be saturated in negative energies..."

    m "Hum..."

    m "Do you think your potion concept could be applied in a more... helpful way?"

    w "What do you have in mind?"

    m "Well, your process let's you {i}build{/i} a gender with various characteristics, right?"

    w "Yeah..."

    m "So, for example, you could create a potion for me to be a woman for a day, and one for me to be agender for a day, and I could compare with how I generally feel."

    m "It might help me figure things out once and for all..."

    m "I'm just sick of just permanently questionning if I'm not just cis and overly complicating things..."

    show react sad at maddie_react

    w "Oh, Maddie!"

    hide react

    w "I can sure make you those potions if you think it could help. I can even make some with various degrees of {i}woman-ness{/i} At least that's the theory... And I can tie a lot of parameters to gender euphoria and dysphoria, if you want. Stuff like language and body parts and social perception."

    show react happy at maddie_react

    m "That'd be great! Can I come to the back with you so you can show me the options and everything?"

    show react happy at witch_shop_react

    w "Sure, come on, let me just lock the front door and we can get brewing!"

    hide react

    jump epilogue



label epilogue:

    play music funpotionmaking fadein 1.0

    scene bg shop small
    show witch front:
        xalign 0.70
        yalign 0.22
    show counter small
    with fade

    w "{i}sigh{/i} Slow day..."

    play sound "/audio/SFX_DoorOpen.wav"
    queue sound "/audio/SFX_DoorClose_Light.wav"
    pause 0.6

    w "Oh, a customer, welcome!"

    show farah back:
        xalign 0.53
        yalign 0.53
    with moveinright

    show react happy at witch_shop_react

    f "Hi, err, good afternoon."

    hide react

    f "Hum, I hope I'm not interupting anything?"

    w "Seriously? I was so bored I was considering breaking out the duster..."

    show react eyeroll at witch_shop_react

    w "So I'm all yours!! What can I do for you, friend?"

    hide react

    f "Ah, that's nice... I'm Farah."

    f "I use they/them pronouns. I think..."

    w "Welcome to my humble shop Farah! I'm the resident witch, ze/zir. You can actually call me 'witch' or 'the witch', since I foolishly offered my first name to demons to seal a deal when I was a kid..."

    f "Err, that's... I'm sorry?"

    w "Don't sweat it, I'm used to it now... Plus, I could easily pick a new name, but the mystery works well with the shop and everything..."

    w "And I doubt you came in here to hear my origin story, anyway! Probably more interested in the spells and amulets... Anything specific in mind?"

    f "Well... I'm not sure my information was correct... It seemed a bit... too good to be true?"

    f "So please don't mind me if I'm actually asking for the moon!"

    f "I've heard you can brew custom potions to change someone's gender for a few hours?"

    w "Oh, yeah, sure, the Build-A-Gender potions!"

    f "So it's true?"

    w "Sure is!"

    w "I don't openly advertise for it because I'm afraid people might misuse it, but I've been spreading the word about them for a couple of month through our community's gravepine. Makes me really happy to see new people coming in to ask for it!"

    show react happy at farah_react

    f "Oh this is great!!"

    hide react

    f "And I can ask for anything?"

    w "Well, not anything anything. I can't recreate genders that are totally outside of my cultural experience, for example. And I won't make it last more than a day, for safety reasons."

    f "That still sounds great!"

    show react flower at farah_react

    f "So... How do I... Do I need to fill in an order form?"

    hide react

    f "Or maybe you already have a waiting list, I don't wait to sound impatient!"

    show react laugh at witch_shop_react

    w "Nothing like that, love. No order form, no waiting list..."

    hide react

    w "Just a chat around a cup of tea, so I can explain how it works and what options you have, and you can pick what would help you the most."

    w "We can do it now, since nothing else seems to be happening. Or we can make an appointment outside of opening hours if you'd rather be sure no one interrupts."

    w "Whatever you prefer!"

    f "Oh, this is, I didn't expect..."

    w "I'm not going to pry, honest. I know how difficult it can be to put that stuff into words, especially when talking to a stranger."

    w "You can just tell me yes or no for the various variants if you're more comfortable with that. I'll offer advice if you want it, but those potions are to help {b}you{/b} figure {b}you{/b} out, so you don't have to explain your choices to me!"

    f "Ah, okay. This... It sounds easier. Thank you!"

    w "You're welcome! Do you want me to put the keetle on, or would you rather come back later?"

    f "I... Now? If it's not too much trouble?"

    w "Sure isn't! Give me a sec, I'll grab the tea set and a couple of ottomans."

    show react happy at farah_react

    pause 1


    hide witch
    hide farah
    scene bg credits small
    with fade

    pause
