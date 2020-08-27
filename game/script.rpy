﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Emily", color="#27aa92")
define a = Character("Angie", color="#edb0d7")
define d = Character("Mysterious Eggdog", color = "#737373")
define A = Character("Deepfake Angie", color="#edb0d7")
define E = Character("Deepfake Emily", color="#27aa92")

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

image conventionStill = "ConventionBackgroundStill.jpg"

image idle:
    "output-onlineimagetools.png"
    size(1280,720)
    0.1
    "output-onlineimagetools (1).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (2).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (3).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (4).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (5).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (6).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (7).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (8).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (9).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (10).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (11).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (12).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (13).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (14).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (15).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (16).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (17).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (18).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (19).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (20).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (21).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (22).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (23).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (24).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (25).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (26).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (27).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (28).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (29).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (30).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (31).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (32).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (33).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (34).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (35).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (36).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (37).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (38).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (39).png"
    size(1280,720)
    0.1
    "output-onlineimagetools (40).png"
    size(1280,720)
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

image emDeepfake movie = Movie(size=(1280,720), play="EmilyDeepFakeConversation.webm")

image angDeepfake movie = Movie(size=(1280,720), play="AngieDeepFakeConversation.webm")

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

    a "Huh? What time is it?"

    e "It's 11! We're late for the eggdog convention!"

    a "Wait what? I thought I set my alarm to wake me up at 10."

    e "ER MAH GERD, you set your alarm to 10 *PM*"

    e "Angie you're always really on top of things! It's funny, usually you're the one dragging me out of bed! You're such a boss... like you wake up at 8 am everyday! It's too powerful..."

    #a "Well, you know me too well aha..."

    e "Let's go!"

    hide e happy

    jump con

else:

    scene bg stever double

    a "Hey, you overslept. Let's go to the convention!"

    play sound "audio/bird.wav"

    show a happy at left

    a "Come on, the eggdogs wait for no one! ʕ•́ᴥ•̀ʔっ"

    "Ughhh... Angie I love you but just five more minutes please..."

    a "..."

    e "Urbffghh... amgy m lumf oo buh just five more minutes please..."

    a "I already gave you five! っ-̶●̃益●̶̃)っ That's it, you're getting up! ≧◉ᴥ◉≦"

    "You still don't understand how she does those emoticons out loud..."

    e "Okay okay I'm up... have mercy, please..."

    e "What time does the convention start?"

    a "11."

    e "..."

    a "..."

    e "I thought the convention started at 1?"

    a "It be at 11."

    e "..."

    a "..."

    e "Huh.."

    a "Don't worry, I'm sure we won't miss anything in the first 30 minutes."

    a "You better get a move on! (ง︡'-'︠)ง"

    hide a happy
    jump con

label con:

    #scene black

    show conv transition

    show conventionStill

    if epath:
        e "We're here!"

        scene bg convention
        play music convention
        show idle

        show e thinking at left
        e "Wow, this place looks like shit. Damn, what the hell happened here? This is even worse than Dashcon."

        a "Oof yeah... geez I can really see what you mean."

        show e angry
        e "I'm never trusting Google reviews again! I hope they give us a refund... in this economy?"

        a "Yeahhh... can't afford to get scammed right now :/"

        e "Goddamn. My broke ass could never."
        e "*cries in broke*"

        a "*also cries in broke*"

        d "...help..."

        a "What was that? Was that a ghost?"

        e "It's the sound of my sadness... *continues to cry in broke*"

        d "Help..."

        show e thinking
        #REPLACE WITH E SURPRISED/STARTLED
        e "Oh my god! Is that a monster??"

        a "No, I think that's an eggdog??"

        d "Help... help me, please..."

        #show e thinking

        d "Euuuuughhhhh..."

        a "What happened? You... this place... everything looks terrible!"

        d "Yes, a horrid beast, so grotesque, it makes my spine shiver even thinking about it right now... if I had a spine."

        a "Where is everyone?"

        d "Gone."

        e "Gone how?"

        d "Just gone... That pixelated creature whisked them away... You gotta help me!"

        e "How can we help you?"

        d "...find them..."

        a "Where?!"

        d "*exhales*"

        hide idle

        e "*grabs Eggdog's body and shakes it profusely* NONONONONO you can't die on me like this, it's too SOON!! You have so much to live for!"

        "Everything is silent."

        e "..."

        a "..."

        d "zzzzzzz"

        a "Oh thank god, he's just sleeping!"

        "Eggdog turns over in its sleep, something falls out of its pocket."

        e "What's that?"

        "Emily picks up BEGG'S EGGDOGDEX from the ground."

        a "Huh. I guess its name is Begg."

        e "What? How can you tell?"

        a "I guess it's the big masking tape on the back of it with the word BEGG written in Sharpie. XD"

        show e thinking

        e "How do you work this thing?"

        "Eggdogdex powers up."

        a "Wow! This dex has the names of all the conventiongoers in it! With this, we'll be able to find everyone!"

        e "Let's go!"

        jump eggdogdex

    else:
        a "We made it!"

        scene bg convention
        play music convention
        show idle

        show a thinking at left

        a "It's... a little deserted."
        a "Are we late after all? Where is everybody?"

        e "Oh my god, is this supposed to be registration!? That's it, I'm leaving a bad review on Google reviews! >:C"

        a "I was expecting some freebies! Where are they? ʘ ʘ"

        a "Are we being pranked right now? Who's funny joke was this?"

        e "Well, I'm not leaving empty handed! Let's take some stuff and leave."

        "Angie turns over the table."

        a "Ahhh!!!!"

        "Underneath the table is a strange white blob... with legs."

        e "What is that?? Some sort of jellyfish?"

        a "No!"

        show a happy

        a "No!! It's an Eggdog!"

        d "Help... help me, please..."

        show a sad

        d "Euuuuughhhhh..."

        a "What happened? You... this place... everything looks terrible!"

        d "Yes, a horrid beast, so grotesque, it makes my spine shiver even thinking about it right now... if I had a spine."

        a "Where is everyone?"

        d "Gone."

        e "Gone how?"

        d "Just gone... That pixelated creature whisked them away... You gotta help me!"

        e "How can we help you?"

        d "...find them..."

        a "Where?!"

        d "*exhales*"

        hide idle

        e "*grabs Eggdog's body and shakes it profusely* NONONONONO you can't die on me like this, it's too SOON!! You have so much to live for!"

        "Everything is silent."

        e "..."

        a "..."

        d "zzzzzzz"

        a "Oh thank god, he's just sleeping!"

        "Eggdog turns over in its sleep, something falls out of its pocket."

        e "What's that?"

        "Emily picks up BEGG'S EGGDOGDEX from the ground."

        a "Huh. I guess its name is Begg."

        e "What? How can you tell?"

        a "I guess it's the big masking tape on the back of it with the word BEGG written in Sharpie. XD"

        show a thinking

        e "How do you work this thing?"

        "Eggdogdex powers up."

        a "Wow! This dex has the names of all the conventiongoers in it! With this, we'll be able to find everyone!"

        e "Let's go!"


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
    e "If only Begg was awake to see all of this it would've been proud."

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

    "You hear a quiet voice call your name...Angie..."

    #HERE OVERHAULING DIALOGUE

    show a deep at center

    "Ah. Nevermind."

    a "Woah what is that? Begg was right - it is hideous!"

    "PUNY HUMANS... YOU'RE ABOUT TO WITNESS HISTORY!"

    e "Wait, that face kinda looks familiar! But it's ~so~ ugly!!"

    "SILENCE!!! *a dark chuckle resonates through the air*"

    "You shiver????"

    a "??????"

    A "EXCUSE ME. I. AM. YOU!!!"

    a "Oh sorry!!"

    "One of Deepfake Angie's arms clobbers Emily, pushing her to the ground. Emily gasps."

    e "Shitshitshitshit; quick, Angie, we gotta fight back!"

    hide a deep
    hide e happy
    jump ending

else:
    scene bg convention
    play music dorm

    show a happy at left
    a "We got all the eggdogs :D"
    a "I can't for when Begg wakes up! Begg's going to be so stoked that its Eggdogdex is complete!"

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

#scene bg deepfake
#"So imagine this is where the deepfake battle happens."


if epath:
    show angDeepfake movie
    e "conversation pending"


    # scene bg stever double
    # play music dorm
    #
    # a "We made it back home! Hurray!"
    #
    # show e laughing at left
    # e "You were so cool back there Angie. The way you took no shit -"
    # e "Like you were a cool knight fighting a dragon or something."
    # e "Hold on - lemme draw a dragon real quick - "
    #
    # scene bg fantasy
    #
    # e "Yeah like this is the kind of mean motherfucker I can see you destroying."
    #
    # a "Wow, thank you Emily. That's really flattering."
    #
    # e "Except I guess the dragon was like... deepfake you...?"
    # e "Hm. Kinda creepy lol."
    #
    # a "Yeah, it kinda was... I wonder where that came from?"
    # a "Who made it, and why? What does it all mean?"
    #
    # "Is it somehow significant that it was a deepfake of me, and that I had to fight it?"
    # "Is there some sort of greater symbolism going on here?"
    #
    # scene bg stever double
    #
    # a "I'm sure whatever it is, it doesn't really matter."
    #
    # show e happy at left
    # e "That's true! I'm sure it doesnt really mean anything lol."
    #
    # a "Yeah it's not that deep."
    #
    # show e laughing
    # e "I'm just glad to be your friend Angie! You're really cool and a total sweetheart!"
    #
    # a "Awww I'm glad to be your friend too!"
    #
    # show e happy
    # show a happy at right
    #
    # "The person reading this text is a legend."
    #
    # hide e happy
    # hide a happy

    jump credits

else:

    show emDeepfake movie

    a "conversation pending"

    # scene black
    # scene bg fuku
    # play music dorm
    #
    # e "Oh HECK yes fuku tea. Finally!"
    #
    # show a happy at left
    # a "Looks like there are already three people inside and the max capacity is 4..."
    # show a laughing
    # a "Do you wanna go in first or shall I?"
    #
    # e "You go ahead, drinks are on ME after all."
    # e "Wait wait, I'm so dumb, I have a better idea. Can you order for the both of us?"
    #
    # a "Sure. What do you want?"
    #
    # e "Anything's good. Surprise me!"
    #
    # a "Alright...That gives me a lot to work off of. I'll do my best?"
    # show a happy
    #
    # e "Okay, even if I hate it, I'll still like it! Don't worry man."
    #
    # a "Okay okay..."
    # hide a happy
    #
    # "Good thing I'm not a picky eater... this way we both get our drinks sooner AND we social distance..."
    # "God that was such a pro gamer move... Emily you're so smart, goddamn."
    #
    # show a happy at left
    #
    # a "Alright, here you go! Hope you like it ( ͡~ ͜ʖ ͡°)!"
    #
    # e "Yo thanks!"
    # "Okay... this is kind of terrible.... but I won't tell her that..."
    #
    # show a laughing
    # a "By the way, thank you so much for stepping up back there..."
    # a "I don't know if I could have gotten through fighting that deepfake version of you without you."
    #
    # e "Yeah that was kind of fucked up wasn't it? Like why was there a giant me?"
    #
    # show a sad
    # a "Hm. Good question... I really don't know."
    # a "... I wonder where that came from?"
    # a "Who made it, and why? What does it all mean?"
    # a "Is it somehow significant that it was a deepfake of you, and that we both had to fight it?"
    # a "Alone, we wouldn't have made it, but with our combined strength we overcame it?"
    # a "That a false image of you was the one responsible for ruining your day,"
    # a "as well as mine... perhaps there's some allegory to be found about personal responsibility..."
    # a "and our hand in controlling our own destiny and responses to difficult events..."
    # a "Is there some sort of greater symbolism going on here?"
    #
    # e "I'm sure whatever it is, it doesn't really matter."
    #
    # show a thinking
    # a "True, it's not that deep."
    # show a laughing
    # a "I'm really glad that I got to hang out with you today! It was so much fun <3"
    #
    # e "Awwwwwwwwwwww I'm happy you're my friend too!"
    #
    # show e happy at right
    # show a happy
    # "The person reading this text is a legend."
    #
    # hide e happy
    # hide a happy

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
