# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Emily", color="#3be5c6")
define a = Character("Angie", color="#edb0d7")
define d = Character("Mysterious Eggdog", color = "#737373")
define A = Character("DEEPFAKE ANGIE", color="#d71d1d")
define E = Character("DEEPFAKE EMILY", color="#1d1db6")

define audio.bird = "audio/bird.wav"

define audio.convention = "audio/convention.mp3"
define audio.dorm = "audio/dorm.mp3"
define audio.danger = "audio/danger.mp3"
define audio.happybirthday = "audio/happybirthday.mp3"

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

image attack1:
    "attack1/attack1_ 00.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 01.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 02.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 03.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 04.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 05.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 06.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 07.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 08.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 09.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 10.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 11.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 12.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 13.png"
    size(1041.3,663.3)
    0.1
    "attack1/attack1_ 14.png"
    size(1041.3,663.3)
    0.1
    repeat

image attack2:
    "attack2/attack2_ 03.png"
    size(1041.3,663.3)
    0.1
    "attack2/attack2_ 04.png"
    size(1041.3,663.3)
    0.1
    "attack2/attack2_ 05.png"
    size(1041.3,663.3)
    0.1
    "attack2/attack2_ 06.png"
    size(1041.3,663.3)
    0.1
    "attack2/attack2_ 07.png"
    size(1041.3,663.3)
    0.1
    "attack2/attack2_ 08.png"
    size(1041.3,663.3)
    0.1
    "attack2/attack2_ 09.png"
    size(1041.3,663.3)
    0.1
    "attack2/attack2_ 10.png"
    size(1041.3,663.3)
    0.1
    "attack2/attack2_ 11.png"
    size(1041.3,663.3)
    0.1
    "attack2/attack2_ 12.png"
    size(1041.3,663.3)
    0.1
    "attack2/attack2_ 13.png"
    size(1041.3,663.3)
    0.1
    "attack2/attack2_ 14.png"
    size(1041.3,663.3)
    0.1
    # "attack2/attack2_ 15.png"
    # size(1041.3,663.3)
    # 0.1
    # "attack2/attack2_ 16.png"
    # size(1041.3,663.3)
    # 0.1
    repeat

image attack3:
    "attack3/attack3_ 00.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 01.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 02.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 03.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 04.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 05.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 06.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 07.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 08.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 09.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 10.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 11.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 12.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 13.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 15.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 16.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 17.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 18.png"
    size(1041.3,663.3)
    0.1
    "attack3/attack3_ 19.png"
    size(1041.3,663.3)
    0.1
    # "atack3/attack3_ 20.png"
    # size(1041.3,663.3)
    # 0.1
    # "atack3/attack3_ 21.png"
    # size(1041.3,663.3)
    # 0.1
    # "atack3/attack3_ 22.png"
    # size(1041.3,663.3)
    # 0.1
    # "atack3/attack3_ 23.png"
    # size(1041.3,663.3)
    # 0.1
    # "atack3/attack3_ 24.png"
    # size(1041.3,663.3)
    # 0.1
    repeat

image bg convention = "bg convention.jpg"
image bg deepfake = "deepfake.png"
image bg fantasy = "bg fantasy.jpg"
image bg fuku = "bg fuku.png"
image bg stever double = "dorm.png"
image conv transition= "conv transition.png"
image eggdogdex = "Eggdogdex.jpg"
image ePokemonBG = "EmilyPokemonBG.png"
image aPokemonBG = "AngiePokemonBG.jpg"

image aDogProps = "aDogProps0.png"
image eDogProps = "eDogProps0.png"

image bdayCard = "bdayCard.jpg"

image transition2 movie = Movie(size=(1280,720), play="Transition2again.webm", image="bg convention.jpg", loop=False)
image transition1 movie = Movie(size=(1280,720), play="Transition1.webm", loop=False)



image ticket = "ticket.png"

image emDeepfake movie = Movie(size=(1280,720), play="EmilyDeepFakeConversation.webm")
image emDeepfakeIdle movie = Movie(size=(1280,720), play="EmilyDeepFakeIdle.webm")

image angDeepfake movie = Movie(size=(1280,720), play="AngieDeepFakeConversation.webm")
image angDeepfakeIdle movie = Movie(size=(1280,720), play="AngieDeepFakeIdle.webm")

# The game starts here.

label start:

    play music dorm

    "You're sleeping..."
    "..."
    "..."
    "..."
    "..."
    "...Is this the real life?"
    "Is this just fantasy?"
    "Caught in a landslide..."
    "....Wait wasn’t there an essay due last night?"
    "...."
    "..."
    "I’m just a little boy nobody loves me"
    "..."
    "But you are loved."
    "Loved one, what is your name?"

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

    e "Angie you're always really on top of things! It's funny, usually you're the one dragging me out of bed! Like you wake up at 8 am everyday! It's too powerful..."

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
    scene bg convention
    #$ renpy.movie_cutscene("Transition1.webm", delay=14, loops=0, stop_music=False)
    $ renpy.movie_cutscene("EggDogConvention2020.webm", delay=24, loops=0, stop_music=False)
    show bg convention

    #show transition1 movie
    #show transition2 movie


    #show conventionStill

    if epath:


        #scene bg convention
        play music convention fadeout 1.0 fadein 1.0
        #show idle

        e "We're here!"
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
        show idle
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

        hide idle with dissolve

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

        show eggdogdex
        with dissolve

        a "Wow! This dex has the names of all the convention goers in it! With this, we'll be able to find everyone!"

        e "Let's go!"

        jump eggdogdex

    else:


        #scene bg convention
        play music convention fadeout 1.0 fadein 1.0
        #show idle

        a "We made it!"

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
        show idle
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

        hide idle with dissolve

        e "*grabs Eggdog's body and shakes it profusely* NONONONONO you can't die on me like this, it's too SOON!! You have so much to live for!"

        "Everything is silent."

        e "..."

        a "..."

        d "zzzzzzz"

        a "Oh thank god, he's just sleeping!"

        "Eggdog turns over in its sleep, something falls out of its pocket."

        e "What's that?"

        "Emily picks up BEGG'S EGGDOGDEX from the ground."

        show a thinking

        a "Huh. I guess its name is Begg."

        e "What? How can you tell?"

        a "I guess it's the big masking tape on the back of it with the word BEGG written in Sharpie. XD"

        e "How do you work this thing?"

        "Eggdogdex powers up."
        show eggdogdex
        with dissolve

        a "Wow! This dex has the names of all the convention goers in it! With this, we'll be able to find everyone!"

        e "Let's go!"


        jump eggdogdex

label eggdogdex:

    scene black


#pokemon battle scene starts
#feel free to change the scrpit of the battle
#add dialoge of eggdog attacking back

    jump battle30Health


label battle30Health:
    if epath:
        scene aPokemonBG
        "A wild Kpop Eggdog appears!"
        show attack1
        show aDogProps
        #show angie's eggdog
        #show 30 health bar
        menu angieAttackOptions:
            "SARANGHAE <3":
                    hide attack1
                    jump battle20Health

            "BOBA BRIBE":
                    hide attack1
                    jump battle20Health

            "A VERY NICE COMPLIMENT":
                    hide attack1
                    jump battle20Health
    else:
        scene ePokemonBG

        "A wild Torchy's Eggdog appears!"
        show attack1
        show eDogProps
        #show torchy eggdog
        #show 30 health bar
        menu emilyAttackOptions:
            "CONK":
                    hide attack1
                    jump battle20Health

            "SUBLIME TEXT EDITOR":
                    hide attack1
                    jump battle20Health

            "AND ONE SPICY BOI":
                    hide attack1
                    jump battle20Health


label battle20Health:
    if epath:
        scene aPokemonBG
        show attack2
        show aDogProps
        "Critical hit!"
        "Kpop Eggdog used YA GOT NO JAMS."
        #hide 30 health bar
        #show 20 health bar
        menu angieAttackOptions2:
            "SARANGHAE <3":
                    hide attack2
                    jump battle10Health

            "BOBA BRIBE":
                    hide attack2
                    jump battle10Health

            "A VERY NICE COMPLIMENT":
                    hide attack2
                    jump battle10Health
    else:
        scene ePokemonBG
        show attack2
        show eDogProps
        "Critical hit!"
        "Torchy's Eggdog used TACO CRUNCH."
        #hide 30 health bar
        #show 20 health bar
        menu emilyAttackOptions2:

            "CONK":
                    hide attack2
                    jump battle10Health

            "SUBLIME TEXT EDITOR":
                    hide attack2
                    jump battle10Health

            "AND ONE SPICY BOI":
                    hide attack2
                    jump battle10Health


label battle10Health:
    if epath:
        scene aPokemonBG
        show attack3
        show aDogProps
        "It's super effective!"
        "Kpop Eggdog used ITZY SHOULDER DANCE."
        #hide 20 health bar
        #show 10 health bar
        menu angieAttackOptions3:

            "SARANGHAE <3":
                    hide attack3
                    jump battle0Health

            "BOBA BRIBE":
                    hide attack3
                    jump battle0Health

            "A VERY NICE COMPLIMENT":
                    hide attack3
                    jump battle0Health
    else:
        scene ePokemonBG
        show attack3
        show eDogProps
        "It's super effective!"
        "Torchy's Eggdog used YEEHAW."
        menu emilyAttackOptions3:

            "CONK":
                    hide attack3
                    jump battle0Health

            "SUBLIME TEXT EDITOR":
                    hide attack3
                    jump battle0Health

            "AND ONE SPICY BOI":
                    hide attack3
                    jump battle0Health


label battle0Health:
    if epath:
        scene aPokemonBG
        #hide angie's eggdog
        #hide 10 health bar
        "You caught the Kpop Eggdog!"
    else:
        scene ePokemonBG
        #hide Torchy Eggdog
        #hide 10 health bar
        "You caught the Torchy's Eggdog!"


#pokemon battle scene ends

if epath:

    scene bg convention
    play music dorm fadeout 1.0 fadein 1.0

    show e happy at left
    e "We got all the eggdogs!"
    e "If only Begg was awake to see all of this it would've been proud."

    a "Yeah... they sure would have. Thank you for helping me do this."

    e "No problem! This was actually kinda fun. Like an epic quest!"

    a "It was pretty thrilling... especially the part where that one doggy boi refused to go into into the Eggdogball..."

    e "And we both had to sit on it so the Eggdogball wouldn't reopen! Man, that was so fun."

    a "Maybe they should just do this for Eggdogcon every year!"
    "...And the Universe unanimously agreed that that was a big brain strat..."

    e "I absolutely agree. It'll be like Easter except non religious and with talking eggs..."
    e "A zombie Easter...but with dogs!"
    e "Hmmmmmm... advanced hide and seek.... me likey."
    e "That aside, I wonder what happened to the big monster who caused all this in the first place? Where did it go?"

    a "Maybe... it just left?"

    e "Hm. I sure hope so. There no way this could come back to bite us in the ass later right?"

    a "Definitely."

    e "Great! Let's head home!"

    a "Yeah, I'm beat. All in all, a pretty on point and fun Eggdogcon!"

    e "Yup! Let's just walk out those doors and leave. Easy as pie."

    a "Mm-hmm! I'll follow you!"

    hide e happy

    play music danger fadeout 1.0 fadein 10.0

    "You hear a quiet voice call your name...Angie..."

    "Angie..."
    a "What is that voice??"
    e "Who are you?"
    "MUAHAHAHA YOU'RE TOO LATE. I'VE ALREADY HARVESTED THE ESSENCE FROM ALL THOSE SOFT EGGDOGS."

    a "No... you're wrong! We found all the eggdogs and we released them from your spell!"

    "HAHAHAHA THAT WAS ALL A DIVERSION. YOU NEVER KNEW WHAT THE PURPOSE OF THIS ENTIRE CONVENTION WAS DIDN'T YOU?"

    e "What??? Isn't it just a place for eggdog enthusiasts to get free stickers and merch???"

    "WELL, YES, BUT I BET YOU DIDN'T EVEN READ THE BROCHURE FOR THE VENUE."

    e "You got us there."

    "THE CONVENTION WAS ALSO WHERE EGGDOG TECH WAS GOING TO REVEAL THEIR NEWEST EGGDOGINATOR THAT CAN TURN EGGS INTO EGGDOGS."

    e "What???? How did we not hear about this."
    a "Is this what happened when we were late??"

    "YOU SEE, THE EGGDOGINATOR RUNS OF EGGDOGINITE, A POWERFUL GEMSTONE WORSHIPPED BY MAN AND EGGDOG ALIKE. BUT INSTEAD OF TURNING EGGS INTO USELESS EGGDOGS I'VE HARNESSED THE EGGDOGINITE TO ITS FULL POTENTIAL..."
    "AND I'M GOING TO USE ITS POWER TO WIPE THIS SAD CONVENTION AND ALL THE EGGDOGS OFF THE FACE OF THE PLANET. PUNY HUMANS YOU'RE ABOUT TO WITNESS HISTORY."

    a "Why are you doing this???"

    "WHY AM I DOING THIS?? YOU'RE REALLY ASKING ME THAT RIGHT NOW??? HAHA... BWAHAHAHAHA...!!! BECAUSE I CAN!!"

    a "Show your face you coward!"

    show a deep at center

    a "..."
    a "Omg Begg was right - it is hideous."

    a "You can kidnap the eggdogs, you can even take the eggdoginite, but I'm not going to let you destroy this planet."

    e "Angie.... that face looks familiar."

    a "Be quiet I'm in the middle of my rant."
    a "And I'm gonna stop you, you hideous beast!!!"

    "SILENCE... HAHAHAHAHAHAHA you fool... I AM YOU."

    a ":0"
    e ":0"

    A "PREPARE TO DIE."


    hide a deep
    hide e happy
    jump ending

else:

    scene bg convention
    play music dorm fadeout 1.0 fadein 1.0

    show a happy at left
    a "We got all the eggdogs :D"
    a "I can't for when Begg wakes up! Begg's going to be so stoked that its Eggdogdex is complete!"

    e "Heck yeah they sure would have. Thanks for helping me find all the Eggdogs!"

    a "You're welcome~! This was fun. It felt like an epic quest!"

    e "Right?  We really did a heccin hecc... remember when that one doggy boi was too scared to go into into the Eggdogball,"
    e "so you showed it that shiny thing and it felt better?"

    a "Shiny thing... Oh my wallet?"

    a "Yeah... well I'm just glad she's feeling better now, even if now I’m too broke for boba."
    e "..."
    a "..."
    e "Want me to get it back for you?"

    a "Eh... It's alright. There were only like, 2 dollars in there anyways. I think I can get it back later."
    e "Alright."
    a "Man, this was fun... we should do this again!"
    a "Maybe they should just do this for Eggdogcon every year!"

    e "Wow you're right... god that's so big brain."

    a "It'll be like Easter! Except... hm... with zombie eggs!"

    e "Hmm technically they’re not zombies, just eggs that are alive."

    e "Buuuuuuut... advanced hide and seek is sparking joy."

    a "Ooooh... a d v a n c e d  h i d e  a n d  s e e k .... v e r y  n i c e ,  v e r y  n i c e . . . "
    a "Speaking of...I wonder what happened to the big monster who caused all this in the first place? Hm...Where did it go?"
    a "Maybe... it just left?"

    e "Hm. I sure hope so."

    a "Hopefully that wont come back to bite us in the butt later."

    e "Definitely."

    a "... Cool~! ( ◑‿◑)ɔ┏🍟--🍔┑٩(^◡^ ) Let's head to Fuku!"

    e "Dude, yes! All in all, this was a pretty on point and fun Eggdogcon!"

    a "Yup! Let's get out of here, I'm exhausted."

    e "Me too, it's been a long day. I'll follow you!"

    hide a happy

    #NEW

    play music danger fadeout 1.0 fadein 10.0

    "You hear a quiet voice call your name...Emily..."

    "Emily..."
    e "What is that voice??"
    a "Who are you?"
    "MUAHAHAHA YOU'RE TOO LATE. I'VE ALREADY HARVESTED THE ESSENCE FROM ALL THOSE SOFT EGGDOGS."

    e "No... you're wrong! We found all the eggdogs and we released them from your spell!"

    "HAHAHAHA THAT WAS ALL A DIVERSION. YOU NEVER KNEW WHAT THE PURPOSE OF THIS ENTIRE CONVENTION WAS DIDN'T YOU?"

    a "What??? Isn't it just a place for eggdog enthusiasts to get free stickers and merch???"

    "WELL, YES, BUT I BET YOU DIDN'T EVEN READ THE BROCHURE FOR THE VENUE."

    a "You got us there."

    "THE CONVENTION WAS ALSO WHERE EGGDOG TECH WAS GOING TO REVEAL THEIR NEWEST EGGDOGINATOR THAT CAN TURN EGGS INTO EGGDOGS."

    a "What???? How did we not hear about this."
    e "Is this what happened when we were late??"

    "YOU SEE, THE EGGDOGINATOR RUNS OF EGGDOGINITE, A POWERFUL GEMSTONE WORSHIPPED BY MAN AND EGGDOG ALIKE. BUT INSTEAD OF TURNING EGGS INTO USELESS EGGDOGS I'VE HARNESSED THE EGGDOGINITE TO ITS FULL POTENTIAL..."
    "AND I'M GOING TO USE ITS POWER TO WIPE THIS SAD CONVENTION AND ALL THE EGGDOGS OFF THE FACE OF THE PLANET. PUNY HUMANS YOU'RE ABOUT TO WITNESS HISTORY."
    e "Why are you doing this???"

    "WHY AM I DOING THIS?? YOU'RE REALLY ASKING ME THAT RIGHT NOW??? HAHA... BWAHAHAHAHA...!!! BECAUSE I CAN!!"

    e "Show your face you coward!"

    show e deep at center

    e "!!!"

    e "Omg Begg was right - it is hideous."

    e "You can kidnap the eggdogs, you can even take the eggdoginite, but I'm not going to let you destroy this planet."

    a "Emily.... that face looks familiar."

    e "Be quiet I'm in the middle of my rant."
    e "And I'm gonna stop you, you hideous beast!!!"

    "SILENCE... HAHAHAHAHAHAHA you fool... I AM YOU."

    e ":0"
    a ":0"

    E "PREPARE TO DIE."

    hide e deep
    hide a happy

    jump ending

label ending:
    scene black
    play music danger
#scene bg deepfake
#"So imagine this is where the deepfake battle happens."


if epath:
    show angDeepfake movie

    A "PUNY HUMANS! GIVE UP AND I MIGHT CONSIDER SPARING YOU (as a consideration of our shared rugged good looks and impeccable fashion sense :0)"
    a "Uh... first of all, ew you look nothing like me and second of all we’re not going down without a fight!"
    A "YOU DARE MOCK ME, THE NEXT SUPREME RULER OF THE WORLD??"
    a "It wasn’t mocking; It was an honest judge of your appearance."
    e "YEAH WHO WANTS TO LOOK LIKE YOUR FUGLY ASS."
    a "... (; -_-)"
    A  "THAT’S IT! PREPARE TO MEET YOUR DOOM"
    e "I can’t get a good enough angle on it...wait no...you...her...it??"
    e "Ok Angie, looks like you’re gonna have to battle it on your own"
    a "Wait how am I supposed to take down a 60 ft deepfake of myself??"
    e "..."
    e "...I have no idea..."
    a "..."
    e "..."
    e "Wait I do have an idea! To defeat an eggdog conqueror-warlord, all you have to do is…"
    a "stream dynamite?"
    e "...have an eggdog battle!"
    a "..."
    e "..."
    a "yeah battle...that’s what I meant..."
    e "...ok... well anyways battling seems like the only thing we can do for now so let's just try it."


    hide angDeepfake

    stop music
    scene black
    ""
    play music dorm
    show angDeepfakeIdle movie
    A "bleh omg I’m deded. Take this treasure to remember our time together..."
    hide angDeepfakeIdle movie
    with dissolve
    "The Angie deepfake fades into dust, leaving behind a small piece of cardstock"


    e "hmm it looks like a postcard addressed to…"
    e "you"
    "Emily hands over the card to Angie"
    "As Angie turns the card to the back it reads..."
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

    jump birthday

else:

    show emDeepfake movie
    E "PUNY HUMANS! GIVE UP AND I MIGHT CONSIDER SPARING YOU (as a consideration of our shared rugged good looks and impeccable taste in the mems :0)"
    e "Uh...first of all, ew you look nothing like me and second of all we’re not going down without a fight!"
    E "YOU DARE MOCK ME, THE NEXT SUPREME RULER OF THE WORLD??"
    e "Yeah! What are you gonna do about it, fake me? Shrink down and fight me!"
    a "YEAH! WE AREN’T AFRAID OF YOUR FAKE ASS."
    e "...Angie...I’m so touched"
    a "aww you’re welcome anytime ≧◉ᴥ◉≦ "
    E  "THAT’S IT! PREPARE TO MEET YOUR DOOM"
    a "I can’t get a good enough angle on it...wait no...you...her...it??"
    a "Ok Emily, looks like you’re gonna have to battle it on your own"
    e "Wait how am I supposed to take down a 60 ft deepfake of myself??"
    a "..."
    a "...I have no idea..."
    e"..."
    a "..."
    a "Wait I do have an idea! To defeat an eggdog conqueror-warlord, all you have to do is…"
    e "drincc bepis?"
    a "...have an eggdog battle!"
    e "..."
    a "..."
    e "yeah battle...that’s what I meant..."
    a "...ok...well anyways battling seems like the only thing we can do for now so lets just try it."


    hide emDeepfake movie
    stop music
    scene black
    ""
    play music dorm
    show emDeepfakeIdle movie
    E "bleh omg I’m deded. Take this treasure to remember our time together..."
    hide emDeepfakeIdle movie
    with dissolve
    "The Emily deepfake fades into dust, leaving behind a small piece of cardstock"
    a "hmm it looks like a postcard addressed to…"
    a "you"
    "Angie hands over the card to Emily"
    "As Emily turns the card to the back it reads..."



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

    jump birthday

label birthday:
    scene black

    show bdayCard with dissolve
    window hide
    pause(10)
    play music happybirthday fadeout 1.0 fadein 3.0
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
