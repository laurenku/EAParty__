# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Emily", color="#27aa92")
define a = Character("Angie", color="#edb0d7")
define d = Character("Mysterious Eggdog", color = "#737373")

define audio.bird = "audio/bird.wav"

define audio.convention = "audio/convention.mp3"
define audio.dorm = "audio/dorm.mp3"
define audio.danger = "audio/danger.mp3"

define epath = False

image a angry = "aangry.png"
image a deep = "adeep.png"
image a happy = "ahappy.png"
image a laughing = "alaughing.png"
image a sad = "asad.png"
image a thinking = "athinking.png"

image e angry = "eangry.png"
image e deep = "edeep.png"
image e happy = "ehappy.png"
image e laughing = "elaughing.png"
image e sad = "esad.png"
image e thinking = "ethinking.png"

#image edog = "dyingdog.png"
#image edog movie = Movie(play="idle.webm")
image idle:
    "output-onlineimagetools.png"
    0.1
    "output-onlineimagetools (1).png"
    0.1
    "output-onlineimagetools (2).png"
    0.1
    "output-onlineimagetools (3).png"
    0.1
    "output-onlineimagetools (4).png"
    0.1
    "output-onlineimagetools (5).png"
    0.1
    "output-onlineimagetools (6).png"
    0.1
    "output-onlineimagetools (7).png"
    0.1
    "output-onlineimagetools (8).png"
    0.1
    "output-onlineimagetools (9).png"
    0.1
    "output-onlineimagetools (10).png"
    0.1
    "output-onlineimagetools (11).png"
    0.1
    "output-onlineimagetools (12).png"
    0.1
    "output-onlineimagetools (13).png"
    0.1
    "output-onlineimagetools (14).png"
    0.1
    "output-onlineimagetools (15).png"
    0.1
    "output-onlineimagetools (16).png"
    0.1
    "output-onlineimagetools (17).png"
    0.1
    "output-onlineimagetools (18).png"
    0.1
    "output-onlineimagetools (19).png"
    0.1
    "output-onlineimagetools (20).png"
    0.1
    "output-onlineimagetools (21).png"
    0.1
    "output-onlineimagetools (22).png"
    0.1
    "output-onlineimagetools (23).png"
    0.1
    "output-onlineimagetools (24).png"
    0.1
    "output-onlineimagetools (25).png"
    0.1
    "output-onlineimagetools (26).png"
    0.1
    "output-onlineimagetools (27).png"
    0.1
    "output-onlineimagetools (28).png"
    0.1
    "output-onlineimagetools (29).png"
    0.1
    "output-onlineimagetools (30).png"
    0.1
    "output-onlineimagetools (31).png"
    0.1
    "output-onlineimagetools (32).png"
    0.1
    "output-onlineimagetools (33).png"
    0.1
    "output-onlineimagetools (34).png"
    0.1
    "output-onlineimagetools (35).png"
    0.1
    "output-onlineimagetools (36).png"
    0.1
    "output-onlineimagetools (37).png"
    0.1
    "output-onlineimagetools (38).png"
    0.1
    "output-onlineimagetools (39).png"
    0.1
    "output-onlineimagetools (40).png"
    0.1
    repeat

image bg convention = "bg convention.jpg"
image bg deepfake = "deepfake.png"
image bg fantasy = "bg fantasy.jpg"
image bg fuku = "bg fuku.png"
image bg stever double = "dorm.png"
image conv transition= "conv transition.png"
image poke transition= "poke transition.png"

image ticket = "ticket.png"

# The game starts here.

label start:

    play music dorm

    "You're sleeping... man sleeping is great."
    "Being a CMU student and everything, sleeping isn't something you get to do very often."
    "Man, it would really suck if something or someone were come along right now and wake you up."
    "Anyways..."

    "What's your name?"
menu name_menu:

        "Angie, because you're an angel :)":
            $ epath = True
            "Outstanding! Fantastic decision!"
            jump morning

        "Emily, because you're a boss bitch!":
            "Absolutely radical! Great choice!"
            jump morning

        "Fuck it, I dont know.":
            "Try again bro!"
            jump name_menu

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

label morning:

    "Ah... now that you have your identity sorted out, you can go back to slumbering peacefully..."

if epath:

    play sound "audio/disturbance.wav"

    "...Eh-?!"

    scene bg stever double

    e "Wake the fuck up bitch!"

    show e happy at left

    e "Today's the eggdog convention! How dare you be late!"

    "She's holding a pair of deconstructed shoeboxes... that must be the source of the loud noise."

    e "Angie you're always really on top of things! It's funny, usually you're the one dragging me out of bed!"
    e "You're such a boss... like you wake up at 8 am everyday! It's too powerful..."

    a "Well, you know me too well aha..."
    a "I thought the convention started at 1?"

    e "Yeah me too, but I was just looking at the ticket and it actually starts at 11!"

    show ticket

    e "See how the 1 looks scratched out? That must be how we missed it!"

    a "Ohhhh... yeah that makes sense. I wonder why the print job is so bad..."

    e "Who cares? Let's go!"

    hide e happy

    jump con

else:

    scene bg stever double

    a "Hey, you overslept. Let's go to the convention!"

    play sound "audio/bird.wav"

    show a happy at left

    a "Come on, the eggdogs wait for noone! ʕ•́ᴥ•̀ʔっ"

    "Ughhh... Angie I love you but just five more minutes please..."

    e "Urbffghh... amgy m lumf oo buh just five more minutes please..."

    a "I already gave you five! っ-̶●̃益●̶̃)っ That's it, you're getting up!≧◉ᴥ◉≦"

    "You still don't understand how she does those emoticons out loud..."

    e "Okay okay I'm up... have mercy, please..."
    e "I thought the convention started at 1?"

    a "Ah, me too, but it's actually at 11."
    a "It looks like you accidentally spilled whiteout on the ticket earlier, and that's why you thought that."

    show ticket

    a "Here, you can take a look at it if you want!"

    e "Huh.. shit, you're right!"

    a "Okay! I've already showered and changed, so I'll go ahead and call an uber.️"

    e "Wait, but then won't the driver be here in like, only 10 minutes?!"

    a "Yup! So you better get a move on! (ง︡'-'︠)ง"

    e "Holy shit girl - "
    hide a happy
    jump con

label con:

    scene black

    show conv transition

    if epath:
        e "We're here!"

        scene bg convention
        play music convention

        show e thinking at left
        e "Wow, this place looks like shit. Damn, what the hell happened here? This is even worse than Dashcon."

        a "Oof yeah... geez I can really see what you mean."

        show e angry
        e "Is this gonna turn out like Fyre Festival? I hope they give us a refund... like I'm not rich enough"
        e "to afford being scammed like this!"

        a "Yeahhh... me neither :/"

        e "Imagine being rich... like I could evade taxes... probably be able to play water polo all day..."
        e "Like how nice is that?"

        a "Ooooh yeah... be able to pay off your student debt, too."

        e "Goddamn. My broke ass could never."
        e "*cries in broke*"

        a "There, there."

        e "*continues to cry in broke*"

        a "At least you'll get to do awesome art?"

        show e happy
        e "You're right! Goddamn... I'm already doing the least amount of art for my major LMAO"
        e "Everytime I'm doing homework for 112 I look around and I'm like..."
        e "I'm too much of an art student for this, are you kidding me?"
        e "And then everytime I'm in a crit, I'm like, 'I'm a CS student, I can't do this shit!'"

        d "Help... help me, please... I am in massive pain..."

        show idle



        e "Woah! Angie, there's an egg next to you! But I think it's a ... dog?"

        a "Like an eggdog?"

        e "Yeah!"

        d "I have mere minutes left to live... please help..."

        e "Hang on little guy, I think there's gotta be a first aid kit around here somewhere..."

        a "Maybe check near the entrance?"

        e "Good idea. I'll go run to get the kit - Angie, stay with the Eggdog while I'm gone!"
        hide e happy

        d "Euuuuughhhhh..."
        d "*extreme noises of pain*"
        d "I must... tell you... what happened here..."

        a "What happened? You... this place... everything looks terrible!"

        d "Yes... a monster came... a monster so horrifying it is undescribable..."

        a "What did this monster look like?!"

        d "Horrifying...and indescribable..."

        "I had that one coming to me, didn't I?"

        d "Please... find the Eggdogs this monster scared off... they are hiding..."

        a "Where?!"

        d "Let me finish... around here... in the convention center... they hide in fear..."

        show e angry at left
        e "Okay I'm back, not to worry Eggdog dude! I got the first aid kit!"
        e "Alright let's take a look in here... and for some reason it's filled with cheeto puffs. Huh."

        a "Oh dear..."

        d "... I thought it would be funny when I filled it with puffs..."

        show e thinking
        e "You did this?!"

        a "Yeah I think that's what they're saying..."

        e "Man, what the fuck? Okay. Okay. Okay okay okay okay."
        e "I don't want to be mean, but you kinda deserve it at this point."

        a "How could you say that? This little guy is in extreme pain!"

        e "You're right, ack! I'm sorry, I just... I don't know how to feel about any of this-!"
        e "I thought we were gonna have a fun afternoon with some eggdogs, but instead it's, it's this!"

        a "I know how you feel... but we gotta keep it together."
        a "For our buddy here... er... what was your name again?"

        d "Call me... Begg..."

        e "Like. Egg, but with a B?"

        d "As I was saying... please find my comrades... you'll find an Eggdogdex in my pocket..."
        d "This dex has the names of all the conventiongoers registered... with it you'll be able to find everyone..."
        d "...I will... now be... passing.... away..."

        e "SHIT WHAT THE FUCK NO DON'T DO THAT -"

        d "Eurghhh....."

        "..."
        "..."
        "..."

        hide idle

        a "...I think... they're gone... oh my gosh..."

        show e sad

        e "Oh my fucking god..."

        "There's only one thing to do from here, then."
        "Eggdogdex... huh? That must be the thing in Begg's pocket..."

        a "Here, help me read this Dex."

        e "Yeah... sure."

        a "Let's go."

        hide e sad
        jump eggdogdex

    else:
        a "We made it!"

        scene bg convention
        play music convention

        show a thinking at left

        a "It's... a little deserted."
        a "Are we late after all?"

        e "No hold on... there's all those chairs and tables that are turned over..."

        a "And there gouges in the walls... I think something horrible happened. ʘ ʘ"
        a "Maybe... all the Eggdogs decided to add a post apocalyptic theme?"
        a "It IS 2020 after all... something like that could spread awareness about proper mask procedures...?"

        e "Goddamn."

        a "Like, they're gonna hop out any minute and tell us it was all a prank?"
        a "Any minute now. Aaaany minute."

        e "Um..."

        a "Yeah. You're right. That's... probably not it."
        a "Man, this is... not very cash money."
        a "Guess I'll just go stupid go crazy."

        show a happy
        a "*absolutely shreds it on the makeshift dancefloor that is a clearing between some overturned tables*"

        e "Angie holy fuck how are you this good at dancing."

        a "Y'know. Well, y'know."

        e "You are so right. I do know."

        a "Yes."

        e "Well it looks like there isn't really anything to do here... could you show me some moves?"

        a "Sure. What do you wanna know?"

        e "Hm. What's that ballet move where you do the spin with your arms like a circle?"

        a "Do you mean a pirouette?"

        e "Yeah that!"

        a "Okay... well let me show you."
        a "*does it perfectly, but trips on a strange white blob at the very end*"
        a "Huh?"

        show idle



        d "Help... help me, please... I am in massive pain..."

        a "Woah... is that an egg... dog? Oh wow, it's an Eggdog!"

        e "Woah you found one?"

        a "Yeah!"

        d "I have mere minutes left to live... please help..."

        a "Hang on little buddy, I think there's gotta be a first aid kit around here somewhere..."

        e "Maybe check near the entrance?"

        a "Good idea. I'll go run to get the kit. Emily, can you stay with the Eggdog while I'm gone?"

        e "You got it."

        hide a happy

        d "Euuuuughhhhh..."
        d "*extreme noises of pain*"
        d "I must... tell you... what happened here..."

        e "Holy shit, what happened? This place looks absolutely fucked!"

        d "Yes... a monster came... a monster so horrifying it is undescribable..."

        e "What did this monster look like?!"

        d "Horrifying...and indescribable..."

        "I had that one coming to me, didn't I?"

        d "Please... find the Eggdogs this monster scared off... they are hiding..."

        e "Where are they?! Motherfucker tell me!"

        d "Let me finish... around here... in the convention center... they hide in fear..."

        show a happy at left

        a "I found the kit! We'll save you little guy. Just hang in a little longer!"
        a "Let's take a look in here...for some reason it's filled with cheeto puffs. Hm. Don't like that."

        e "Jesus Fucking Christ."

        d "... I thought it would be funny when I filled it with puffs..."

        show a angry
        a "Why would you do that?! You're saying that you're the one who filled this with cheese puffs?"

        e "Yeah I think that's what they're saying..."

        a ".... I - hm. No. I'm. I'm... angry?"
        a "I can't... I mean i just can't - like why would you do that?"

        e "Hey, they said they thought it'd be funny."

        a "Wh- but. It's... You're dying! You're actually dying! Do you... still think this is funny?"

        d "...a little bit...."

        a "Pardon my language but... screw you!"

        e "... Angie, are you ok?"

        a "I thought we were gonna have a fun afternoon with some eggdogs, but instead it's, it's this!"

        e "Angie..."
        e "Girl, you're right. Fuck this shit. Today has been total garbage."

        a "Absolute garbage! The worst!"

        e "Fuck it. When all this is over, we're going to Fuku tea together, on me. Anything you want."

        a "No, I can't make you pay that...!"

        e "Fuck you. You're my friend, bitch, and I wanna cheer you up. I'm goddamn paying."

        a "Alright..."

        e "Okay. Boba later. Got it. Now back to this punk. What's your name again?"

        d "Call me... Begg..."

        a "... as in Egg, but with a B?"

        d "As I was saying... please find my comrades... you'll find an Eggdogdex in my pocket..."
        d "This dex has the names of all the conventiongoers registered... with it you'll be able to find everyone..."
        d "...I will... now be... passing.... away..."

        e "BEGG WHAT THE FUCK STOP THAT RIGHT NOW -"

        d "Eurghhh....."

        "..."
        "..."
        "..."


        hide idle

        e "Fuck. I think. I think Begg's fucking dead."

        show a sad

        a "Oh... oh my gosh..."

        "There's only one thing to do from here, then."
        "Eggdogdex... huh? That must be the thing in Begg's pocket..."

        e "Here, help me read this Dex."

        a "Yeah... sure."

        e "Alright girl. Let's go and save some fucking eggdogs."

        hide a sad
        jump eggdogdex

label eggdogdex:

    scene black
    show poke transition

    "eggdogs and shit"

if epath:

    scene bg convention
    play music dorm

    show e happy at left
    e "We got all the eggdogs!"
    e "Man... if only Begg were here to see it. They would've been proud."

    a "Yeah... they sure would have. Thank you for helping me do this."

    e "No problem! This was actually kinda fun. Minus the 'saw a conscious being die in front of me part'. Like an epic quest!"

    a "It was pretty thrilling... especially the part where that one doggy boi refused to go into into her Eggdoggball..."

    e "And we both had to sit on it so the Eggdollball wouldn't reopen! Man, that was so fun."

    a "Maybe they should just do this for Eggdogcon every year!"

    e "You are so big brain. I absolutely agree. It'll be like Easter except non religious and the eggs are alive!"
    e "Hmmmmmm... advanced hide and seek.... my adventure brain likes this idea."
    e "That aside, I wonder what happened to the big monster who caused all this in the first place? Where did it go?"

    a "Maybe... it just left?"

    e "Hm. I sure hope so. Anyways, that probably won't be plot relevant later."

    a "For sure."

    e "Great! Let's head home!"

    a "Yeah, I'm beat. All in all, a pretty on point and fun Eggdogcon!"

    e "Yup! Let's just walk out those doors and leave. Easy as pie."

    a "Mm-hmm! I'll follow you!"

    "I sure hope nothing interrupts us while we walk towards the exit."

    show a deep at center

    "Ah. Nevermind."

    e "Woah what the fuck is that? Oh shit- it's attacking me; quick, Angie, we gotta fight back!"
    hide a deep
    hide e happy
    jump ending

else:
    scene bg convention
    play music dorm

    show a happy at left
    a "We got all the eggdogs :D"
    a "I wish Begg were here to see it. Even if they were kind of a jerk, they would've been proud."

    e "Heck yeah they sure would have. Thanks for helping me find all the Eggdogs!"

    a "You're welcome~! This was fun. The part where I saw an Eggdog die in front of me aside, it felt like an epic quest!"

    e "Right? Awesome as heck... remember when that one doggy boi was too scared to go into into her Eggdoggball,"
    e "so you showed her a shiny thing and she felt better?"

    a "My wallet? That she took? Oh yeah... well I'm just glad she's feeling better now. Though I'm REALLY not gonna be able to pay for boba later."
    a "Eh... It's alright. There were only like, 2 dollars in there anyways. I think I can get it back later."
    a "It WAS so much fun though... we should do this again!"
    a "Maybe they should just do this for Eggdogcon every year!"

    e "You're right... god that's so big brain."

    a "It'll be like Easter! Except... hm... non religious and the eggs are alive!"

    e "Hmmmmmm... advanced hide and seek.... my adventure brain likes this idea."

    a "Ooooh... a d v a n c e d  h i d e  a n d  s e e k .... v e r y  n i c e ,  v e r y  n i c e . . . "
    a "Speaking of...I wonder what happened to the big monster who caused all this in the first place? Hm...Where did it go?"
    a "Maybe... it just left?"

    e "Hm. I sure hope so."

    a "True. That probably won't be plot relevant later."

    e "Oh yeah, For sure."

    a "... Cool~! ( ◑‿◑)ɔ┏🍟--🍔┑٩(^◡^ ) Let's head to Fuku!"

    e "Dude, yes! All in all, a pretty on point and fun Eggdogcon!"

    a "Yup! Let's just walk out those doors and leave. I'm really excited to get out of here."

    e "Me too, it's been a long day. I'll follow you!"

    "I sure hope nothing interrupts us while we walk towards the exit."

    show e deep at center
    play music danger

    "Ah. Nevermind."

    a "Oop - ah, darnit. This is - okay. It's attacking me. Hey Emily, can you help me fight the monster please?"

    e "Oh yeah, of course, totally -!"

    hide e deep
    hide a happy
    jump ending

label ending:

scene bg deepfake
"So imagine this is where the deepfake battle happens."

if epath:
    scene bg stever double
    play music dorm

    a "We made it back home! Hurray!"

    show e laughing at left
    e "You were so cool back there Angie. The way you took no shit -"
    e "Like you were a cool knight fighting a dragon or something."
    e "Hold on - lemme draw a dragon real quick - "

    scene bg fantasy

    e "Yeah like this is the kind of mean motherfucker I can see you destroying."

    a "Wow, thank you Emily. That's really flattering."

    e "Except I guess the dragon was like... deepfake you...?"
    e "Hm. Kinda creepy lol."

    a "Yeah, it kinda was... I wonder where that came from?"
    a "Who made it, and why? What does it all mean?"

    "Is it somehow significant that it was a deepfake of me, and that I had to fight it?"
    "Is there some sort of greater symbolism going on here?"

    scene bg stever double

    a "I'm sure whatever it is, it doesn't really matter."

    show e happy at left
    e "That's true! I'm sure it doesnt really mean anything lol."

    a "Yeah it's not that deep."

    show e laughing
    e "I'm just glad to be your friend Angie! You're really cool and a total sweetheart!"

    a "Awww I'm glad to be your friend too!"

    show e happy
    show a happy at right

    "The person reading this text is a legend."

    hide e happy
    hide a happy
    jump credits

else:
    scene black
    scene bg fuku
    play music dorm

    e "Oh HECK yes fuku tea. Finally!"

    show a happy at left
    a "Looks like there are already three people inside and the max capacity is 4..."
    show a laughing
    a "Do you wanna go in first or shall I?"

    e "You go ahead, drinks are on ME after all."
    e "Wait wait, I'm so dumb, I have a better idea. Can you order for the both of us?"

    a "Sure. What do you want?"

    e "Anything's good. Surprise me!"

    a "Alright...That gives me a lot to work off of. I'll do my best?"
    show a happy

    e "Okay, even if I hate it, I'll still like it! Don't worry man."

    a "Okay okay..."
    hide a happy

    "Good thing I'm not a picky eater... this way we both get our drinks sooner AND we social distance..."
    "God that was such a pro gamer move... Emily you're so smart, goddamn."

    show a happy at left

    a "Alright, here you go! Hope you like it ( ͡~ ͜ʖ ͡°)!"

    e "Yo thanks!"
    "Okay... this is kind of terrible.... but I won't tell her that..."

    show a laughing
    a "By the way, thank you so much for stepping up back there..."
    a "I don't know if I could have gotten through fighting that deepfake version of you without you."

    e "Yeah that was kind of fucked up wasn't it? Like why was there a giant me?"

    show a sad
    a "Hm. Good question... I really don't know."
    a "... I wonder where that came from?"
    a "Who made it, and why? What does it all mean?"
    a "Is it somehow significant that it was a deepfake of you, and that we both had to fight it?"
    a "Alone, we wouldn't have made it, but with our combined strength we overcame it?"
    a "That a false image of you was the one responsible for ruining your day,"
    a "as well as mine... perhaps there's some allegory to be found about personal responsibility..."
    a "and our hand in controlling our own destiny and responses to difficult events..."
    a "Is there some sort of greater symbolism going on here?"

    e "I'm sure whatever it is, it doesn't really matter."

    show a thinking
    a "True, it's not that deep."
    show a laughing
    a "I'm really glad that I got to hang out with you today! It was so much fun <3"

    e "Awwwwwwwwwwww I'm happy you're my friend too!"

    show e happy at right
    show a happy
    "The person reading this text is a legend."

    hide e happy
    hide a happy
    jump credits

label credits:

if epath:
    play music acredits

    $ credits_speed = 40
    scene black
    show credits at Move((0.5, 1.0), (0.5, -3.65), credits_speed,
                  xanchor=0.5, yanchor=0)
    with Pause(credits_speed+10)

else:
    play music ecredits

    $ credits_speed = 40
    scene black
    show credits at Move((0.5, 1.0), (0.5, -3.65), credits_speed,
                xanchor=0.5, yanchor=0)
    with Pause(credits_speed+10)







    # This ends the game.

return
