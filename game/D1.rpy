# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character('Vince', color="#9699f2")
define s = Character('Shawn', color="#b0ad4c")
define h = Character('Hunter', color="#5a9967")
define c = Character('Chyna', color="#a37bad")
define t = Character('Undertaker', color="#385dd8")
define k = Character('Kane', color="#ff0000")
define p = Character('Paul Bearer', color="#9d4141")
define r = Character('Rick Rude', color="#8dd025")
define j = Character('Jamie')
define a = Character('Assistant', color="#e973cc")
define q = Character('???')
define w = Character('Worker')
define st = Character('Stagehand')
define me = DynamicCharacter("povf", color="#ffffff")


# Other junk cuz ren'py hates you (Variables)

define dude = False
define chick = False
define nb = False

define shawn_match = False
define taker_match = False


# The game starts here.

label start:

    $ completed = False

    $ shawn_end = False
    $ hunter_end = False
    $ chyna_end = False
    $ taker_end = False
    $ spr_notif = False

    $ dx_points = 0
    $ shawn_points = 0
    $ hunter_points = 0
    $ chyna_points = 0
    $ taker_points = 0
    $ kane_points = 0


    $ calDate = calDate.replace(second=00, hour=12, minute=00, day=28, month=9, year=1997)





    scene black
    play sound "assets/sfx/phone ring.wav" loop
    "..."
    "..."
    "...Huh?"
    "Ugh, what time is it?"
    "I roll over in my bed, reaching out blindly for the phone."
    stop sound
    play sound "assets/sfx/phone pickup.mp3"
    "When I finally get it in my hands, I mutter a weak hello."

    q "Hello?"
    q "Hey, look, you gotta help me."
    q "I can't explain right now, but I'm in trouble."
    q "Can you go into work tomorrow for me?"
    q "I'll let Vince know."

    "I think I mutter a response, but I don't have time to ask anything before they hang up."
    play sound "assets/sfx/phone hangup.mp3"
    "I'm too sleepy to even process what's happening."
    "Before I realize it, I fall back asleep."
    scene black with fade
    "..."
    scene cg hotel day
    with fade
    play sound "assets/sfx/day.mp3"
    "Oh man, what a weird dream."
    "It felt like my friend had called me during the night and told me to go into work for them."
    "But that's ridiculous."
    "And something about Vince...? What even."

    play music music_morning fadein 1.0
    window hide
    stop sound fadeout 1.0
    call calendar(1)
    window show

    "I get up and stretch, ready to take on the day."
    "I work at the World Wrestling Federation. WWF for short. My job isn't anything special, though."
    "There's a Pay-Per-View coming up this weekend, so the atmosphere is getting tense."
    "But, that's not any of my problem."
    "I travel to the televised shows and help out with menial labour and making sure the guys on the undercard have things they need."
    "I don't deal with Pay-Per-Views or main eventers. I'm not high enough in the ranks."
    "...To be honest, it's kind of a bummer."
    "I {i}wish{/i} I would be allowed to get involved with the lights and glamour."
    "Oh, what am I doing, moping this early in the morning."
    "There's still a show to put on tonight!"

    play sound "assets/sfx/car.mp3"
    scene bg stadium
    with fade

    "This is the place for tonight."
    "I'm glad I don't have to set things up, it seems so exhausting."
    "Let's get inside, see if I can't grab a snack before the pre-show meeting."

    play sound "assets/sfx/walking.mp3"
    scene bg hallway
    with fade
    
    stop music fadeout 1.0
    play sound "assets/sfx/pager.mp3" loop
    "I don't get too far in until my pager starts beeping."
    "I check it, confused. Who could need me right now?"

    stop sound
    play sound "assets/sfx/beep.mp3"
    centered "{font=assets/fonts/DS-DIGIB.TTF}{size=60}GO TO VINCE'S OFFICE{/size}{/font}"

    "...Uh."
    "WHAT?"
    "As ominous as it seems, I don't dare ignore it."
    "Only my close friends and bosses have this number."
    "So this must be serious."

    play sound "assets/sfx/door4.mp3"
    scene bg office
    with fade

    "I knocked on the door before entering, but there wasn't a reply."
    "I've never been in Mr. McMahon's office before..."
    "What on earth could they want with me?"

    show assistant normal with img_dissolve
    play music music_kabul fadein 1.0
    a "Oh, you."
    a "You're the new one, right?"

    "Huh?"

    a "Wait, let me get you a new badge."
    a "First name?"


    $ povf = renpy.input("First name?", allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", length=20)
    if povf == "":
        $ povf ="Lilli"

    me "Uh... %(povf)s."
    me "Wait, what's this all about?"

    a "Last name?"

    $ povl = renpy.input("Last name?", allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", length=20)
    if povl == "":
        $ povl ="Hammond"

    me "%(povl)s. But, why are you — "

    a "And are you a Mister or Missus?"

    menu:
        a "And are you a Mister or Missus?{fast}"

        "Mister":
            $ dude = True
            me "I'm a guy, you can't tell?"
            "The assistant just gives me a look, and goes back to whatever she's doing."

        "Miss":
            $ chick = True
            me "I'm a girl, you can't tell?"
            "The assistant just gives me a look, and goes back to whatever she's doing."

        "Why does it matter?":
            $ nb = True
            me "I'm sorry, why does this matter?"
            "The assistant just gives me a look, and goes back to whatever she's doing."


    if dude == True:
        a "Alright, Mr. %(povf)s %(povl)s, right?"
        me "...Right."
        a "Here's your badge, Mr. %(povl)s. That should get you around the arena just fine."
    elif chick == True:
        a "Alright, Ms %(povf)s %(povl)s, right?"
        me "...Right."
        a "Here's your badge, Ms %(povl)s. That should get you around the arena just fine."
    elif nb == True:
        a "Alright, %(povf)s %(povl)s, right?"
        me "...Right."
        a "Here's your badge, %(povl)s. That should get you around the arena just fine."

    me "What about my current badge?"
    a "That's a main branch badge. You need a Pay-Per-View badge."
    me "There's a difference?"
    me "WAIT... Why do I even need a Pay-Per-View badge?"
    a "So you can work the Pay-Per-View, duh."
    a "Didn't you get a briefing already?"
    me "No! Not at all!"
    show assistant annoyed
    a "Let me get Mr. McMahon."

    stop music fadeout 1.0
    hide assistant with img_dissolve

    "I don't get another word out before she leaves the office briskly."
    "This isn't making {i}any{/i} sense."
    "Why am I getting a Pay-Per-View badge all of a sudden?"
    "I guess I hoped I was going to help out, regardless, but to go so far as needing a specific badge?"
    "Why do I need a briefing?"
    "What the hell is going on?"

    play music music_vince
    show vince happy with img_dissolve
    v "%(povf)s! There you are!"
    me "Mr. McMahon!"
    show vince normal
    v "I've heard a lot of good things about you, I hope you know."
    v "Your friend recommended you to me. You know the one..."
    show vince grumpy
    v "Wait, what was their name again?"
    show vince normal
    v "Oh, whatever. The one who got hurt."

    me "Who got hurt?"
    "Wait a second... This sounds familiar."
    "My dream from last night... Was that actually real?"

    v "It doesn't matter now!"
    v "I've decided to pull you up to the big boy's club for this week."
    v "I hope you understand — emergencies and all."
    v "I believe my assistant has already filled you in?"
    me "No, Mr. McMahon, no one's filled me in."
    me "What's my job, exactly?"
    v "What do you think it is?"
    v "You're a manager!"
    me "M... Manager?"
    me "Mr. McMahon, I've never managed a day in my life."
    "This is almost too much for me to process all at once."
    
    v "Nonsense, your friend told me you would be a perfect fit for the job!"
    me "And which friend is that, Mr. McMahon?"
    "I'm just desperate at this point -- who on earth had called me last night? Who recommended me for this job after an injury?"
    v "There's no cause for concern, %(povf)s!"
    v "Just focus on doing your best for this Pay-Per-View, because if you do well, it will definitely reflect kindly on your company reviews."
    
    "Vince's words do the exact opposite of his intentions and I just start to freak out more."
    "I didn't ask for this responsibility, so why is my career so dependent on it?"
    "But Vince's smiling expectant face is somehow too much for me to just... {i}ignore{/i}, I guess."
    "And, well..."
    "I really do want to do well."
    "I won't lie -- I've wanted a job like this since before I even started working here."
    "It's a dream come true."
    "I've only ever been helping with setting things up and breaking things down, and maybe helping new guys stretch or get water."
    "But to be an honest to god manager?"
    "So while I'm scared shitless... I don't dare complain any further."
    
    me "Well... Alright, but..."
    me "I'm not really sure what my job, uh... Entails, exactly?"
    v "Oh, you can relax %(povf)s. You won't be the {i}only{/i} manager working the Pay-Per-View!"
    v "There are others who will be running around, so not everything will be on your head."
    v "But your friend, the one who isn't here, they usually dealt with the upper card, so that's most likely where you'll be needed."

    "Once again, I do the exact opposite of relaxing."
    me "H... Hold on, I'm sorry, sir, I'm just trying to wrap my head around this."
    me "I'm going to be helping the upper-carders? What, that means..."
    show vince stern
    v "It means what it means, you'll be assisting Michaels and the Undertaker with what they need, as well as the Hart Foundation and any others who require attention."
    me "I'm..."
    "I shut my mouth before I blow it."


    show assistant:
        xpos 0.20
    show vince: 
        xpos 0.65
    with img_dissolve
    "There isn't even any time for me to entirely process everything before the door opens and the assistant makes her way back into the room."
    a "Mr. McMahon, the security guards are here."
    a "They wanna know if you have any special instructions."
    show vince annoyed
    v "Alright, tell them I'll be out in a second."
    hide assistant
    stop music fadeout 1.0
    show vince at center with img_dissolve
    v "Sorry, %(povl)s, I've got a lot on my hands right now, so I won't be able to explain to you your duties anymore."
    v "In fact, I won't be able to help you at all, so you better not mess things up."

    "The mention of the security and Vince's changed demeanour takes me off guard for a moment before I remember."
    "That's right... Stone Cold Steve Austin."
    "He's currently on a hell-raising campaign against the McMahons and the company, and it's actually been causing a lot of commotion backstage."
    "Something about him not being willing to sign a waiver or contract or something?"
    "It all got so complicated so quick, and since neither of the men involved are the kind to work things out peacefully..."
    me "That's alright, Mr. McMahon."
    v "Well, good."
    v "I've got to get going now, I've been needing to up security more and more recently because of that Texan bastard."
    v "If you need anything, ask my assistant."

    "Without another word, Vince turns to leave the office."
    hide vince with Dissolve(1.0)
    "I panic and shoot out an arm, as if I were trying to grab him."
    me "Wait, Mr. McMahon!"
    show vince annoyed with img_dissolve
    v "What is it?"
    me "I'm sorry, sir, I just --"
    me "I just have one more question for you."


    menu:
        #For Vince
        me "I just have one more question for you.{fast}"

        "Is there anything specific I should be prepared for?":
            $ dx_points += 1
            "Something as big as a Pay-Per-View this size probably has a bunch of smaller working parts that I should be aware of, especially now that I kinda have to."
            "And I've never had this much responsibility on only my shoulders."
            "I look at Vince desperately, hoping for some kind of hint that could help me prevent an injury or otherwise."
            v "Well, wrestling has always been dangerous for more than just the fighters."
            v "But, it's ultimately up to you to make sure everyone gets out alive!"
            v "And to make sure we all get the money we're trying so hard for."
            "I can't disagree with him."


        "Has anything bad ever happened at a PPV that I should know of?":
            $ taker_points += 1
            "I know there have been plenty of avoidable injuries, and disastrous accidents. Wrestling is rife with that kind of thing."
            "But if my introduction to my new job is being heralded by some unknown friend being injured, I'm going to be a little more than a little extra superstitious."
            v "The world of wrestling is always unpredictable, so of course there have been incidents."
            v "But it's your job to always be ready for those incidents, anyway!"
            v "Don't worry, I'm sure you'll do fine."
            "I don't know how to reply."

        "Is there anyone else I should be helping?" if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True:
            $ kane_points += 1
            "It seems too good to be true, but I'm still cautious."
            "After all, I've spent so long helping lower-carders that it just seems like too much to throw me into just these big names all of a sudden."
            "Vince laughs at my question, unnerving me."
            v "Of course not!"
            v "What, do you think there's anyone else more important than the main eventers?"
            "I don't have an answer to give."


    v "Is that all, then?"
    me "Y... Yes, Mr. McMahon."
    v "Good."
    v "As I said, ask my assistant if anything is important."
    hide vince with img_dissolve
    play sound "assets/sfx/door.mp3"
    "And just like that, he turns the doorknob and leaves the office."
    
    "I'm already bursting with anxiety, unsure if I should bite my nails first or after pulling my hair out."
    "C'mon, %(povf)s, think!"
    "Main eventers, main eventers, Shawn Michaels and the Undertaker!"
    "It's a special Pay-Per-View, they've been building up to this match for a while."
    "Shawn's been annoying the Undertaker for months now, getting in his way, and now it's culminating to... Oh, God."
    "A chill runs down my back."
    "The Hell in a Cell match."
    "The first of it's kind, a nightmarish structure that will cover the ring and the area around it, with no escape, and no rules."
    "Someone is {i}bound{/i} to be badly injured, there's just no avoiding it."
   
    play music "assets/music/Kabul Flight.mp3" fadein 1.0
    show assistant with img_dissolve
    "While I'm ruminating and my stomach acid is burning holes in my organs, the assistant walks back into the room, expressionless as always."

    if dude == True:
        a "Got everything, Mr. %(povl)s?"
    elif chick == True:
        a "Got everything, Ms %(povl)s?"
    elif nb == True:
        a "Got everything, %(povl)s?"

    me "Uh... yeah."
    "She keeps a cool gaze on me, and my nervousness goes from my future situation to the one at hand."
    "I scratch the back of my neck, wondering if I should risk making small talk or if I should just find the wrestlers I should talk to are."
    "God knows where they'd be anyway."
    "I decide to kill two birds with one stone."
    me "So... You wouldn't happen to know where anyone is, right?"
    show assistant annoyed
    "The assistant smacks on her chewing gum for a second, giving me a look."
    a "Not at all."
    me "Of course."
    me "Sorry for bothering you."

##########################################################################
    #Exploring the arena Pre-Raw [D1]
    scene bg hallway
    with fade
    play sound "assets/sfx/door.mp3"

    "Back out in the hallway, there isn't Vince or any security guards."
    "I guess they left before all the rest of the stagehands and wrestlers showed up to pack the hallways."
    "Honestly... I have no idea what to do."
    "Normally, I would just go and help the stagehands before the show starts, setting up the ring and cleaning up the aisles."
    "And after that, I'd go backstage and help lower card wrestlers get ready, just running basic errands to help everything run smooth."
    "But now, with this new assignment to upper card wrestlers and a fuckin' Pay-Per-View in my sights?"
    "I'll be honest... I'm more than a little shaken."
    "But there's no use in standing mindlessly in the hallway like this."
    "I need to do something."
    "I'll take a short walk around the stadium -- get myself acquainted a little before RAW and clear my mind some."

    scene bg gorilla
    with fade

    "I wander through the backstage area towards the front, following the path a wrestler themselves would take."
    "Slip by giant carts with heavy lights and follow the duct tape path down to Gorilla, the waiting room for the main walk down to the ring."
    "Stagehands are still setting up the room, a cooler with water and ice in the corner and a skinny kid trying to set up a bulky TV so everyone can see what's airing live."
    "I walk up to the curtains, one of my favourite places in the house, the gateway between the fans and the workers."
    "When I turn around, I get a small shock."
    stop music fadeout 1.0

    show shawn absent with img_dissolve
    play music music_shawn fadein 1.0
    "Casually standing near me is Shawn Michaels, the Goddamn Showstopper."
    "He looks a little lost, clearly having walked into the room to find something or someone."

    if dude == True:
        "I instinctively want to reach out and introduce myself, the fanboy in me rejoicing at the opportunity."
    elif chick == True:
        "I instinctively want to reach out and introduce myself, the fangirl in me rejoicing at the opportunity."
    elif nb == True:
        "I instinctively want to reach out and introduce myself, the fan in me rejoicing at the opportunity."

    "But I know better than to do that, especially with my heart rate so high."
    "Besides... I don't really know if I, well. Have permission?"
    "I'm still not entirely sure if Vince called the right person into his office, so trying to tell Shawn that I'm his new manager seems a little too brazen."
    "On top of all that, too, I don't even know what I'd say."
    "Luckily, or unluckily, for me, Shawn doesn't even notice me."
    stop music fadeout 1.0
    hide shawn with dissolve
    "As quick and absent-mindedly as he came in, he leaves the room, still on his search, apparently."
    "The kid working on the television hasn't even paused."
    "I wait a little bit before I leave Gorilla, continuing on my self-made tour."

    scene bg catering
    with fade
    "I follow the clear path to catering, probably the most densely populated place in any stadiums."
    "It's not even so much a place for everyone working to just eat, it's also kind of a hangout place."
    "It's definitely the safest place to kill time without getting in anyone's way when a show is going on."
    "There are only a couple of snacks laid out by now, but once it gets closer to the show, there'll be more options for hungry wrestlers."
    "Catering is, at the very least, the only place that I feel comfortable in right now, with this new position and everything."
    "As I approach the doors to enter the large cafeteria-esque room, I hear the tell tale sounds of an argument."
    "Frustrated sighs and nondescript angry words. Not quite shouting, but nowhere near a normal happy conversation."
    play music music_chyna fadein 1.0
    show hunter annoyed:
        xpos 0.25
    show chyna annoyed: 
        xpos 0.6
    with img_dissolve
    "I turn a little, and see the WWF's strongest couple, Hunter Hearst Helmsley and Chyna clearly aggravated."
    "Their sudden presence makes me jump a little."
    "I wasn't expecting to see either of them here."
    "Chyna rolls her eyes at Hunter, and he sneers at her, saying something under his breath."
    "They're clearly trying their hardest to keep their fight from getting too loud, but as for trying to keep it under wraps? Totally failing."
    "Other stagehands are obviously sneaking worried peeks at them, everyone in the area stepping far away from the two."
    "I've worked with them before, a while ago, before they started hanging out with Shawn all the time."
    "It wasn't much, really, just basic low level assistant things."
    "But by the looks of it, neither of them remember me at all."
    "At the very least, neither of them even offer me a passing glance."
    "And I'm sure as shit not going to say hi or intervene when the mood is this tense."
    stop music fadeout 1.0
    hide hunter
    hide chyna
    with img_dissolve
    "They continue on and walk past me, into catering, their hands balled up into fists."
    "I wonder if Shawn was looking for them earlier, when he wandered into Gorilla."
    "Hopefully he does, and he can stop whatever fight is brewing between the two of them."

    scene bg backhalls
    with fade

    "I take the back way around the arena, to get to the loading dock and crew heavy side."
    "Wrestlers normally never go around that way, there's not really anything for them."
    "But it's where I always work -- or, well. Worked, past tense."
    "Anyway, it's a place that I know fairly well, and just wandering aimlessly around the stadium isn't really doing anything to help my anxiety."
    "I'd rather deign myself to help setting up the ring than just do nothing."
    play music "assets/sfx/trolley.mp3"
    "As I'm approaching the large trucks at the loading dock, a train of large cameramen and their gear rumbles down towards me."
    w "'Scuse me, passin' through!"
    "All of the men and materials takes up almost the entirety of the narrow hallway, and I nervously press myself against the wall."

    if dude == True:
        w "Hey, sir, can you please move!"
    elif chick == True:
        w "Hey, ma'am, can you please move!"
    elif nb == True:
        w "Hey, pal, can you please move!"

    "It seems as if me hiding against the wall isn't enough space for them."
    me "Sorry!"
    "A little bit behind me is a doorway to a supply closet, and I quickly duck in there, feeling like Indiana Jones avoiding a giant boulder."
    play sound "assets/sfx/door.mp3"
    scene black
    with fade
    "I stand in the dark awkwardly for a bit, hearing the rumbling of all the carts passing by."
    "How long do I have to stay in here...?"
    "It's dark, smells like cleaning supplies, and I'm {i}definitely{/i} not meant to be here."
    "But I don't want to accidentally open the door and hit someone holding some $5000 camera."
    stop music fadeout 1.0
    "I wait until the rumbling has gone quiet and then some before I nervously crack open the door."
    
    scene bg backhalls
    show taker surprised
    with fade
    play music music_taker fadein 1.0
    
    me "Oh!"
    "I almost close the door as soon as I open it."
    "Is that..."
    "Holy shit, it's the fucking Undertaker!"
    "He seems just as surprised as I am to see him, and I don't really blame him."
    "I mean, I {i}did{/i} just jump out of a supply closet."
    me "Ah, uh..."
    me "Hi."
    show taker normal
    "The Undertaker doesn't reply, he only gives me a quick look over, making me sweat."
    me "I'm, uh, I'm %(povf)s %(povl)s, a{w=.3}{nw}"
    stop music fadeout 1.0
    hide taker
    with dissolve
    me "I'm, uh, I'm %(povf)s %(povl)s, a{fast}... new manager."
    "Aaaand he's gone."
    "I just watch him walk away quietly, my words falling on non-existent ears."
    "...I don't really know what I expected."
    "I let out a breath that I hadn't noticed I was holding."
    "He's certainly very towering and looming, making the whole introducing myself thing harder than I expected."
    "Man, this week is gonna suck, isn't it?"

##########################################################################
    play music music_fretless fadein 1.0
    scene bg mainsetup
    with fade
    play sound "assets/sfx/09_crowd.mp3"
    "Since I suck at the whole manager thing, I figured I might as well just go back to doing what I do best."
    "Setting up the ring."
    "There are still stagehands swarming the main area, stretching canvas over the wooden base, setting up announcers tables and safety mats."
    "Some of my co-workers, people I actually know are wandering around, carrying boxes of gear or helping each other with unwieldy gates."
    "One of them notices me and waves me over."
    show stagehand normal with img_dissolve
    st "Hey, %(povf)s, where you been?"
    st "We're dyin' over here, help us out."
    me "I got another new job, dude."
    show stagehand shocked
    st "Whaaaat?"
    "I go over to help them set up the corner stage stairs."
    me "Yeah, I got a temporary promotion. I'm a main event manager now."
    st "What the fuck, man! That's so cool."
    show stagehand normal
    st "How'd that even go?"
    me "I have no clue, honestly."
    me "Vince McMahon told me some other manager got injured and called me in to replace them, but couldn't remember their name."
    me "You got any clue?"
    st "Nah... nah."
    st "We don't really know any managers other than you, they're usually all backstage while we're out here sweating."
    "My former co-workers all laugh at that, and I have to give a chuckle too."
    st "Sorry we couldn't be of assistance, O Great One."
    me "Give it a rest."
    me "I'll be back here in a week, they said I'm only up there for the Pay-Per-View, anyway."
    st "Well, hopefully you last longer than that!"
    "I laugh and nod, thinking about how I still wasn't even sure if I wanted to be in this position at all."
    hide stagehand with img_dissolve
    "My stagehand friends go back to work, and I take a step back for another layer of canvas to pass by."
    "It's still weird how I got this job... And it's even weirder how no one can think of who got hurt."
    "Truth be told, I'm annoyed at myself for not knowing."
    "I try to wrack my head for a name, incident, {i}anything{/i} that would give me a clue as to who gave me all this fortune."
    "I just don't really have any friends who work higher up in the company... Everything is so separated."
    "The wrestlers have some crazy seniority system, and that's carried over to the stagehands even, so it's very hard to make friends with someone who works in a different field than you."
    "I used to work as a stagehand, and then I got promoted to lower level match manager duties."
    "With that little responsibility, though, I still spent a lot of time helping set stuff up, if only because I felt obligated to."
    "But even so, I'm not in the same group anymore, so it's strange."
    "I go to sit on the stage, since everything seems to be pretty much done already."
    stop music fadeout 1.0
    "Behind me, I hear a commotion, and follow the sounds to see the biggest troublemakers, probably."

    play music music_shawn
    show hunter:
        xpos 0.15
    show shawn:
        xpos 0.40
    show chyna:
        xpos 0.65
    with img_dissolve

    "Finally, the complete crew."
    "A couple of the newer stagehands and workers are shaking Shawn's hand, almost in reverence."
    "Hunter and Chyna near him are casual, not fighting with each other anymore. At least, not openly fighting."
    "I figure now is as good a time as any to introduce myself."
    "They're probably making the rounds to get all the handshakes in, since, as I said before, WWF has got some crazy seniority respect rules."
    "And if I'm not the only person who'll be approaching him, then it won't be so weird, right? They won't instantly turn me away, right?"
    "I head up to them carefully."
    s "Who do we got here?"
    "Shawn holds out his hand, but his focus isn't anywhere near me."
    "He's clearly thinking I'm just a nobody, and while he's not entirely wrong, I'm kind of a somebody now."
    me "Hi, I'm %(povf)s %(povl)s. I saw you earlier and wanted to introduce myself, but didn't have the chance."
    s "Huh? Yeah, alright."
    "Shawn gives me a sloppy handshake, as if he didn't want to stay touching me."
    s "Look, I'm busy, but if you stick around later, maybe I'll be able to sign something."
    me "No, uh, you've got it wrong."
    me "I'm a manager, I'll be around for this week, helping you for the Pay-Per-View."
    "That finally gets their attention."
    "All three of them turn to look at me, and Shawn scoffs."
    s "Manager?"

    if dude == True:
        s "I don't know if you were told, but I don't need a manager."
    elif chick == True:
        s "Hun, I don't know if you were told, but I don't need a manager."
    elif nb == True:
        s "I don't know if you were told, but I don't need a manager."

    me "That may be so, but I was assigned by Vince McMahon."
    me "It's nice to meet you."
    "Shawn shoots a glance to Hunter, who shakes his head."
    s "Yeah, alright, but, uh..."
    s "You really gotta up the professionalism if you want anyone to take you seriously."
    if dude == True:
        h "Shawn, why are you botherin' with this guy?"
    elif chick == True:
        h "Shawn, why are you botherin' with this chick?"
    elif nb == True:
        h "Shawn, why are you botherin' with this guy?"
    h "Just leave 'em, they aren't worth it."
    "Chyna nods quietly. Her eyes haven't left my face yet."
    me "Um, I, uh, got this job as a replacement."
    me "I've worked with you before, a little."
    "As soon as the words leave my mouth, I want to swallow them back down."
    "Why am I even offering an explanation?"
    "I guess I just want to see if any of them would have an idea of who could've passed this job off to me."
    h "Shit, a replacement?"
    h "You're not even a first choice."
    s "Word to the wise, don't go telling people you don't deserve their attention right off the bat."
    "Chyna nods again, this time with a smirk on her face."
    "I bite my lip, and look away."
    h "C'mon, Shawn, let's go already."
    "Shawn grins and agrees with Hunter, turning around and leaving the main area."
    "Chyna follows the boys, walking at her own pace behind them."
    hide shawn
    hide chyna
    hide hunter
    with img_dissolve
    stop music fadeout 1.0
    "The group of people who had gathered to shake their hands disperses, since Shawn isn't here anymore."
    "I can't help but feel guilty."
    "I go to sit back on the stage again, upset that no one seemed to remember my elusive manager friend or even me."

    play music music_kabul fadein 1.0
    "The set up for the ring is done by now, and the people around are either stagehands setting up the barriers or wrestlers in sweatpants practising moves in the ring."
    "Some members of the Nation of Domination standing by the side of the ring, shouting at Farooq in the ring, who seems to be trying out some new flashy move."
    "The Head Bangers are also here, although they seem to be arguing about something."
    "I think I see a flash of Goldust's wig, and I know I definitely hear Dude Love's laugh."
    "I can recognize pretty much all of these wrestlers, but there isn't a single one who turns their head in my direction."
    "That's a pretty sobering thought."
    "I wonder if any of this will change after my week as a higher class manager."
    "But maybe that's too much to hope for."

    scene bg hallway
    with fade

    "When I get back to my starting point, there's already only a half-hour before the show starts."
    "I ran backstage with some of the other stagehands when they started letting people in, and helped sort out some of the complicated wires connecting all of the CCTVs."
    "I'm pretty frustrated, though, at how little I've done so far."
    "I know it's to be expected, but it's still annoying."
    "I figure with this much time before the show, I should be able to talk to one of the wrestlers I'm supposed to be in charge of."
    if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True:
        "I mean, I guess."
        "Really, I'm not entirely against just letting them do as they wish, since they seem so dead set on ignoring or avoiding me."

##########################################################################  
    menu:
        #Who To Find Again
        "Who should I look for?"
        "Shawn":
            $ dx_points += 1
            "Being entirely honest, I'm actually pretty worried about Shawn."
            "He seemed a little distracted, and if that causes something bad to happen on my first day, it definitely doesn't look good on me."
            "And besides..."
            "Do none of them {i}really{/i} don't remember me at all?"
            "It just sucks that I guess I mean so little to them."
            "I don't really want to, since they're just so clique-ish."
            "It's hard to talk to any of them, and when they're all together in a team, it's genuinely pretty frightening."
            "But, regardless, it's time to do my job."
            "I'll go find them before the show starts, and just make sure it's all okay."
            stop music fadeout 1.0
            scene bg catering
            show hunter:
                xpos 0.15
            show shawn:
                xpos 0.40
            show chyna:
                xpos 0.65
            with fade
            play music "assets/music/Sexy Boy.mp3" fadein 1.0
            "I find the entire crew in catering, sure enough."
            "None of them are in their wrestling gear, and Shawn's even got a open beer in hand."
            "It doesn't really annoy me so much as make me nervous, but I guess it's not really that rare for a wrestler to be drinking in street clothes before the show goes on."
            "They notice me when I get close, and Shawn's the first one to strike."
            s "Lookie here, we got a visitor!"
            s "What's goin' on, huh?"
            me "I'm just... checking on you."
            "Hunter snorts."
            s "Checking on us?"
            
            if dude == True:
                s "Man, what good is that gonna do?"
            elif chick == True:
                s "Babe, what good is that gonna do?"
            elif nb == True:
                s "Man, what good is that gonna do?"
            
            me "It's my job."
            "I know my reply was pretty weak, but I figure stressing my professionalism should do something."
            
            if chick == True:
                s "Look, hun, I've been around for a while."
            elif nb == True:
                s "Look, pal, I've been around for a while."
            elif dude == True:
                s "Look, pal, I've been around for a while."
            
            s "I just wanted to get this out of the way, and let you know that I'm not looking to put up with any sort of shortcomings you might have."
            
            if chick == True:
                h "Y'know, it might sound cruel, but chicks like you? Usually got a {i}lot{/i} of shortcomings."
                "He crudely gestures to my chest as he speaks."
            elif nb == True:
                h "Y'know, it might sound cruel, but people like you? Usually got a {i}lot{/i} of shortcomings."
                "He crudely gestures to my body as he speaks."
            elif dude == True:
                h "Y'know, it might sound cruel, but dudes like you? Usually got a {i}lot{/i} of shortcomings."
                "He crudely gestures to my crotch as he speaks."

            c "We're done here."
            c "If you're planning on being a bother, I'll be happy to show you the door."
            c "Otherwise, you can help yourself."
            "Shawn laughs loudly, probably at my face."
            "I start to feet hot with embarrassment, my chest tightening."
            h "You can go ahead and stay out of the way now."
            "He waves his hand in a shooing motion, making Shawn laugh harder."
            h "Go on, get!"
            hide shawn
            hide hunter
            hide chyna
            with img_dissolve
            stop music fadeout 1.0

            "God, they really are just high school bullies, aren't they?"
            "Despite me knowing that, having had to withstand that entire barrage of insults definitely does its job."
            "I'm demeaned and ashamed, and before I know it, I'm hightailing it out of there, my head tucked low."
            "{i}This{/i} is why I didn't want to see them."
            "Already in a bad mood, I begrudgingly decide to stand near Gorilla."
            "Either I get to watch the show or I get to be around when something bad happens at the show, I guess."

        "Undertaker": #needs adding
            $ taker_points += 1
            "It's not like I'm worried about the Undertaker, but I only really saw him for a couple of seconds."
            "So, I figure, it must be worth it to try and find him and actually introduce myself."
            
        "Neither" if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True: #needs adding
            $ kane_points += 1
            "My job isn't to be in charge of them after all, and no one is expecting that of me."
            "So, why bother?"
            "I'm just here to be there for them if they need me, and if they don't need me, then I'm fine."
            "...I will admit, I'm mostly just peeved."
            "I'd rather just go back to Vince's office and see if there's anything specific waiting for me."
            
##########################################################################
    #Post-Raw

    scene bg gorilla
    with fade
    #$ renpy.movie_cutscene("RAWP1.avi")
    
    play music music_show
    "The show starts, and, well."
    "Michaels and Co. certainly seem proud of themselves."
    "They waltz back in, laughing loudly."
    show hunter:
        xpos 0.15
    show shawn b:
        xpos 0.40
    show chyna:
        xpos 0.65
    with img_dissolve
    s "I don't know what that guy thinks he's got on me, but those Canadian pansies don't scare me a bit."
    s "Oh, what a big man, huh? Yeah right, Hart can suck my dick."
    s "I don't know if he remembers, but {i}I'm{/i} the one who always gets in {i}his{/i} way, not the other way 'round."
    h "He's probably forgotten how pointless he is."
    "The two men walk past me without a thought, as if I never existed."
    "Not really a surprise, to be honest."
    "I figure there'll be more time for them to remember me, anyway."
    hide hunter
    hide shawn b
    show chyna at center
    with dissolve
    "As the men walk away, Chyna accidentally bumps into me with her massive shoulder."
    "I step back as an apology, not wanting to get on her bad side when she hasn't said one decent word to me yet."
    "But she pauses, and looks at me."
    "She gives me a quick nod, as if to apologize, and then continues on following Shawn and Hunter."
    hide chyna with img_dissolve
    "...Well, alright."
    "Not gonna lie, that's a surprise."
    show rick with img_dissolve
    "Rick Rude walks past, and notices me watching the others walk away."
    r "How did you get back here?"
    me "U-uh, excuse me?"
    r "Where is your pass?"
    "I suddenly realize that he thinks I'm a fan, or someone who {i}isn't{/i} meant to be here."
    me "No, um, I'm a -- manager."
    me "I just got hired."
    "He audibly scoffs at me, and shakes his head."
    r "Unbelievable."
    r "This company really is going to shit."
    hide rick with img_dissolve
    "And with that, he walks away, still openly disgusted."
    "I rub my shoulder, looking down."
    "...I still need to get used to all of this."

    scene bg gorilla
    with fade

    "The first match of the night starts, but I stay back from the exit out to the ring."
    "There's a small television set up in the room, relaying the live feed for the people waiting on their cue."
    "I lean against the wall, watching the screen."
    "The matches are varied, as always, with the Hart Foundation interfering in pretty much everything."
    "The wrestlers I watched earlier go onstage and put on a show, pandering to the crowd."
    "It's actually pretty fun, I'll admit."
    "Before being someone employed by the WWF, I'm pretty much first and foremost a fan."
    "It's exciting being able to see Dude Love shamble past me before he heads out to the commentary table, his head bobbing lazily."
    "When Goldust walks by, he practically leaves a trail of glitter behind him, and  I can't help but laugh to myself."
    "Neither Shawn, Hunter, or Chyna show up while the other matches and commercial breaks go on, but I don't really notice."
    "I'm basically just enjoying the free show."
    "When Stone Cold comes on stage and starts shouting at Vince to come out, I groan."
    "Sure enough, Vince angrily stomps out to meet him, and all I can remember is him telling me this morning that he won't be around to help me."
    "Stone Cold shouts for a bit at Vince for wanting him to sign a contract absolving WWF of responsibility from any injuries, and the crowd loses their mind in support for him."
    "Vince clearly has way more than enough on his plate."
    "I guess any assistance I'll be getting from the higher ups will be in the form of his assistant."
    "As \"helpful\" as she is."
    "Stone Cold eloquently wraps up his speech by flipping Vince the double birds, and Vince rubs his forehead as the crowd goes wild."

    scene bg gorilla
    with fade

    "Before I realize it, it's almost time for the main event."
    "I honestly might not have even noticed if it weren't for, well... {p}For the main eventers."
    show hunter s:
        xpos 0.15
    show shawn b:
        xpos 0.40
    show chyna s:
        xpos 0.65
    with dissolve
    "It's a little before we go on commercial break, and they make their presence known."
    "Hunter and Chyna in full regalia, and Shawn still brandishing his precious belt."
    "Hunter doesn't seem as cocky as Shawn is, though, and is pacing lightly around the room."
    s "Hey, man, you freakin' out about something?"
    s "Just chill, he's not gonna be able to get his hands on you."
    h "I'm not freakin' out."
    "Hunter's adamant about how calm he is, but I can see Chyna watching him silently."
    "I never really got the whole \"I'm fine\" thing that wrestlers get wrapped up in."
    "Like, you're nervous, it's fine."
    "I know I would, especially since Hunter's going to be facing off against the Undertaker."
    "Shawn snorts and slaps a hand on Hunter's back."
    s "You'll do fine, man."
    "I accidentally catch his eye, and he turns his head to face me fully."
    hide hunter
    hide chyna
    show shawn at center
    with img_dissolve
    if dude == True:
        s "You, new guy."
    elif chick == True:
        s "You, new girl."
    elif nb == True:
        s "You, new guy."
    s "I'm right, right?"
    s "He's gonna be fine."
    "I open my mouth and blink, thinking of how to reply."
    "Before I can give a yea or nay, Shawn seems to come to his senses and stops looking at me."
    s "Wait, nevermind, you probably haven't even seen a match anyway."
    hide shawn
    show hunter:
        xpos 0.25
    show chyna:
        xpos 0.55
    with img_dissolve
    h "Quit it, Shawn."
    if dude == True:
        h "His opinion means nothing, anyway."
    elif chick == True:
        h "Her opinion means nothing, anyway."
    elif nb == True:
        h "Their opinion means nothing, anyway."
    "Hunter's words are meant to sting, clearly, but they just seem to fall flat."
    "Either I'm getting used to this verbal assault or else he just doesn't have his heart in it."
    show chyna shorts eye roll
    "Chyna looks like she's thinking the same thing as me, and she shakes her head."
    play music music_hunter fadein 1.0
    "Hunter's theme begins, and Shawn's hand on Hunter's back gives him a forceful push."
    show shawn b:
        xpos 0.15
    show hunter s:
        xpos 0.40
    show chyna s:
        xpos 0.65
    with img_dissolve
    s "Show's startin'! Let's go!"
    "Hunter nods, clearly pumping himself up."
    hide shawn
    hide hunter
    hide chyna
    with img_dissolve
    "They turn and head out the exit, to the lights and sound."
    "I watch them on the small screen in the room, looking for any sign of nervousness in Hunter's actions."
    "He seems fine, really, absorbed in the adoration of the crowd."
    "Which, honestly, is a relief."
    stop music fadeout 1.0
    scene bg gorilla dark
    "I'm caught up in watching the show when the lights go dim."
    play sound "assets/sfx/thunder1.mp3"
    "The dark presence behind me makes me jump, and I whip around."
    play music music_taker
    show taker s with img_dissolve
    "The Undertaker, somehow even more ghastly in his coat, right behind me."
    "He hasn't even seemed to notice me, his sights set entirely on the exit to the stage, and whoever dares to lie in his path."
    me "Guh, uh."
    me "Good luck?"
    hide taker with img_dissolve
    "He doesn't offer a glance my way, and walks through the doorway."
    "I watch him quietly until I can't see him from my safe hiding spot in Gorilla, so I turn my attention to the screen."
    play sound "assets/sfx/run_loud.mp3"
    "This time, behind me, I don't feel so much a presence as much as a rush of air."
    "Oh, no..."
    stop music

    #$ renpy.movie_cutscene("RAWP2.avi")

    play music music_stress
    "At this point, I'm not even standing back calmly, watching the show on the small screen."
    "I'm right up against the entrance to the stage, and I'm not alone."
    "Other stagehands and workers are crowding the area, and only a few of them are trying to find order."
    "This isn't really going too well, is it?"
    "I'm sure everyone in the crowd is having a great time, but I'm..."
    "I'm biting my nails in anxiety."
    "Once everything's kind of sorted out, and the bell rings, I expect things to calm down, or become a little more normal."
    "Of course, though, that doesn't happen."
    stop music

    #$ renpy.movie_cutscene("RAWP3.avi")

    play music music_stress
    show rick angry with img_dissolve
    r "Get out of the way!"
    "I turn to see Rick Rude stomping towards me, his fists tight around his briefcase."
    r "I warned Vince, and now he has to pay!"
    "I don't manage to stop myself from reaching out and grabbing his arm before he crosses the threshold onto the stage."
    me "Wait, you can't do this!"
    "I just want him to hold on for a Goddamn second."
    "We both know that when he runs out there, Hunter will be disqualified, and -- {p=0.5}... I don't know."
    "I'm just looking for some semblance of control."
    "Rick sneers at me and pushes me away easily."
    hide rick with img_dissolve
    scene bg gorilla with flash
    play sound "assets/sfx/fall.wav"
    "I hit the ground hard, landing on my hand."
    "My wrist bends back sharply, the pain making me gasp."
    "Rick has already run out onto the stage, wreaking havoc. The bell is ringing, the ref calling off the match."
    "I wobble back up to my feet, wincing at the throbbing in my wrist."
    play sound "assets/sfx/run_02.mp3"
    "A worker comes running up to me."
    w "Hey, are you alright?"
    w "You took a nasty bump there."
    me "Yeah, yeah, I'm fine."

    if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True:
        play sound "assets/sfx/fire.wav" fadein 1.0
        scene bg gorilla
        with red_flash
        "I'm not done saying my words when I feel the crackle of searing heat behind me."
        "Nervously, I whip around, expecting to see something going {i}horrendously{/i} wrong."
        "But there's nothing there."
        stop sound fadeout 1.0
        me "Did -- did you hear that?"
        w "Huh? What do you mean?"
        me "There was -- you didn't feel anything?"
        w "No, man, I've got no clue."
        "But I'm so sure that there was someone."
        "There had to be."
        "It felt so real, like the pyro had gone off behind me, but just no explosions."
        "I feel myself walking towards the origin of where I think the sound came from, but a tight grip on my arm stops me."
        "Before I realize it, the worker had grabbed me to not wander away."
        w "Hey, man, come back here!"

    w "You've gotta stay back, security is gonna be rushing the stage soon."
    w "And if your wrist is hurt, you don't wanna get caught in the crossfire."
    "I take a deep breath before nodding in agreement."
    "What a fucking shitshow."

    #$ renpy.movie_cutscene("RAWP4.avi")

    scene bg stage
    with fade

    "Sure enough, once all the cameras are off, security runs past me, already on high alert because of Stone Cold."
    "I run out with them. My wrist isn't so much of an issue that I'm immobilized or anything."
    "Besides, things went straight to hell out there, it would be asking way too much of me to just stand back when I'm this curious."
    
    scene cg raw end
    with fade

    s "Get this dude away from me!"
    "I don't even know what to help with first."
    "Security guards are working on holding the Undertaker back while Chyna is trying to drag Hunter back towards an exit."
    "The crowd is trying to hang behind, but ushers are shooing them all away quickly, desperately trying to keep the situation under control."
    "I figure I'm best used with the angry Deadman, so I head over that way."
    me "Hey, 'Taker!"
    "I don't know what I'm doing, really, but I know I want to get everything under control before Vince decides to blacklist me forever."
    
    scene bg stage
    show taker s angry
    with fade
    "The Undertaker actually spares a look my way, but it's filled with malice."
    "My body goes cold, but I still try to get a hand on his arm somehow, to drag him back."
    me "Stand back! Just back off, it's not worth it!"
    me "You'll have your chance Sunday!"
    "I don't really know if he can hear me, or if he's understanding what I'm saying."
    "He just seems so filled with rage."
    "But, for whatever God forsaken reason out there, he finally relents, his massive body stepping back from the scaffolding."
    "It's terrifying impressive how sturdy he is, none of the burly guards are able to move him unless he lets them."
    "He shrugs off the men grappling him as if they were gnats and heads off backstage, giving Shawn an especially long glare."
    hide taker with img_dissolve
    stop music fadeout 2.0
    "I gasp in air, once again unaware that I'd been holding it."
    "With the Undertaker gone, Shawn finally hops down to the ground, stumbling over to Chyna holding Hunter's now conscious body."
    "I follow him, and I'm not entirely sure why."
    "I tell myself it's because I want to make sure everything's alright."
    "By this time, most of the crowd is gone, leaving the arena almost entirely empty."
    play music "assets/music/Cool Rock.mp3"
    show shawn shirtless angry with img_dissolve
    "Shawn is livid."
    s "That was bullshit!"
    s "That freak was really tryin' to kill me!"
    hide shawn
    show hunter:
        xpos 0.25
    show chyna:
        xpos 0.55
    with img_dissolve
    "Hunter shakes his head as if to dispel dizziness."
    "Chyna has since let go of him, since he seems to be able to stand on his own two legs by himself now."
    "But she still has an arm slightly extended towards him, either to catch him or offer assistance."
    "Hunter ignores it, regardless of her intentions."
    hide hunter
    hide chyna
    show shawn
    with img_dissolve
    "Shawn looks directly at me, still angry."
    s "What are you doing here?"
    me "I just wanted to check on you, make sure you're okay."
    "I try to keep my voice calm."
    "There's no point in agitating him any further."
    s "There's no need, because everything's fucked up, alright?"
    show shawn b:
        xpos 0.15
    show hunter s:
        xpos 0.40
    show chyna s:
        xpos 0.65
    with img_dissolve
    h "Shawn, man, it's cool."
    s "No, H, it's not."
    s "That fucking freak is shooting fire at me and I'm supposed to just be cool with it?"
    s "Just leave me alone, dammit."
    h "Hey -- "
    play sound "assets/sfx/slap2.mp3"
    "Hunter reaches out to grab Shawn's shoulder, but Shawn smacks it away."
    s "Don't touch me."
    hide shawn with dissolve
    "Shawn stomps away, still fuming."
    "Hunter looks more worried than Chyna, who is still keeping a close eye on Hunter's condition."
    "I think he's fine by now, not really in any sort of danger zone, but I wouldn't really know."
    "I've never been Tombstoned before."
    me "I'm just gonna --"
    "I point in Shawn's direction, but neither Hunter nor Chyna acknowledge me."
    hide hunter
    hide chyna
    with dissolve
    play sound "assets/sfx/walking.mp3"
    "I quickly slip over to where Shawn is, gathering up his belt and shirt."
    show shawn with img_dissolve
    "He notices me and grunts, a mix of a sigh and groan."
    me "Hey, look, I was just..."
    s "What, checkin' to see if I'm okay?"
    s "I'm good."
    "His voice is sharp and curt, but I try to not let it get to me."
    me "What happened out there?"
    me "You said something about fire, what was going on?"
    if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True:
        me "I mean, I think I saw what you were talking about, but..."
        "I trail off, still unsure if what I saw was real or not."
        "Shawn doesn't acknowledge it."
    "Shawn shakes his head and shifts his weight from one leg to the other."
    s "It's fucked up is what it is."
    me "I thought you said you weren't scared of some boogeyman."
    "Shawn laughs, but it's not his usual fare."
    s "What are you harpin' on about?"
    s "You're actin' like you even know half of what's goin' on."
    "I mean, I've been working at WWF for years now."
    "But I don't say that, and just let him speak."
    s "I'm not scared of him, and I've beaten his ass many times before."
    s "He's just some dude with unwashed hair and a dumb eyebrow piercing."
    s "He's not {i}actually{/i} a dead man, but he's still so fuckin' creepy."
    s "He's just..."
    "Shawn seems lost for words, and I mentally finish his sentence with '{i}a scary fucker{/i}.'"
    "He sighs, and the tension in his body seems to lower somewhat."
    s "Look, I'm -- I'm tired."
    s "I'm gonna go."
    hide shawn with dissolve
    "Shawn walks away, avoiding Hunter and Chyna, his belt slung over his shoulder."
    "The couple in question is back to arguing, unsurprisingly."
    "Looks like this Monday hasn't really been kind to anyone, really."
    show hunter:
        xpos 0.25
    show chyna:
        xpos 0.55
    with img_dissolve
    "I walk up to them, to see if there's anything I can offer."
    "Worst they can do is rebuff me, like Shawn."
    c "I don't know why you won't suck it up."
    "Chyna shoots me a look that says very succinctly to back the hell off, so I comply."
    "I step back a few steps, still pretty obviously listening in."
    c "The match went badly, you can just say it."
    c "I didn't think he'd get back up, either."
    h "Will you fucking quit it?"
    c "Hunter, listen, get your head out of your ass."
    c "He nailed you pretty hard, it won't kill you to get your neck checked out."
    h "God, just shut up!"
    h "It's bad enough that freak got a stupid win off of me, I don't need you talking to me like this."
    c "I don't know why I'm concerned about you."
    c "You're such a jackass."
    show hunter at center
    hide chyna
    with img_dissolve
    play sound "assets/sfx/footsteps.mp3"
    "Chyna storms off, leaving Hunter leaning against the audience barrier alone."
    h "This is stupid."
    "He says it almost so quietly I don't catch it, and he slowly heads backstage, too."
    "I hear him grumble something about shared hotel rooms as he goes, unsteady."
    stop music fadeout 1.0

    scene bg gorilla with fade
    "The crowds are all gone by now, the arena pretty much evacuated."
    "Damage control."
    "I consider briefly searching for the Undertaker to ask him how he's doing, but I know better than that."
    "And by that, I mean I know almost for a fact that he's gone to wherever he goes to."
    "A coffin? Who knows."


    if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True:
        scene bg stage with fade
        "I walk back out to the main stage to see if there was anything left behind."
        "I know Shawn remembered his belt, but Hunter had left his robe behind, and I figure it might be a kind move to give it back to him. Maybe endear me to him or something."
        "Sure enough, there's an unattended pile of clothes near the barrier."
        "It's too dark to be Hunter's robe, but I go over to check it out anyway."
        "It's on the wrestler side, so I go to pick it up, thinking I'd return it to Lost and Found or something."
        "Maybe a fan got overzealous and {i}really{/i} wanted someone to have their coat."
        "But as I got closer, I realized that it wasn't just a regular jacket, it was a cloak."
        "The Undertaker's cloak, to be specific."
        "Well, that settles it, right? Now I've definitely got to pick it up."
        "I can bring it to security, or someone who can pass it on to him later, or maybe just give it to him myself."
        "Seems simple enough, right?"
        "I don't know why, but the closer I step towards it, the more my stomach seems to curl up."
        "It's almost as if, instead of just picking up some fabric, I'm risking putting my hand into a bear trap."
        "Something just feels wrong."
        "I even look around me, as if I would catch someone aiming a gun at my head or something."
        "Why am I freaking out about this? It's just a stupid jacket."
        "It's not like it's imbued with dark energy or anything."
        "I take a deep breath and bend over to grab it."
        play sound "assets/sfx/scream.wav"
        scene bg stage
        with red_flash
        play music "assets/music/Mud Bath.mp3"
        "I jolt back up, stumbling back from the jacket."
        "That was a scream -- someone was screaming in pain."
        "There's something wrong with this whole situation, and I'm not supposed to be here."
        "I don't know why I know this, I don't know why there's such a visceral reaction to this, but I don't want to interfere with something I shouldn't be."
        "Genuinely scared, I run backstage, and leave the jacket alone."
        "Someone else can grab that damn thing."
        stop music fadeout 1.0

    scene bg hallway
    with fade
    play music "assets/music/Brittle Rille.mp3"

    "The only people left in the stadium at this point are all crew, running to clean things up for the next show."
    if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True:
        "The whole jacket thing still has me a little shaken up, but nothing I can't handle."
    "I'm signing out in the main office when the worker who helped me earlier sees me and gets my attention."
    w "Hey, you good?"
    w "How's your wrist?"
    me "Oh."
    "I'd totally forgotten about it, actually."
    "Sure enough, it's swollen and red, annoyed at being ignored."
    "I show it to the worker, who gives an approving whistle."
    w "It's lookin' pretty bad."
    w "Let's get you to the clinic real quick, maybe get you an ibuprofen or something."
    me "Yeah, better safe than sorry, right? I guess."
    "The worker chuckles at my apathy, but honestly, I'm just so tired already."
    scene bg hallway
    with fade
    "The medic couldn't really do much, since it definitely wasn't broken."
    "He gave me a box of wrist wraps and a bag of ice, but that was really all of it."
    "I should keep my wrist wrapped up and iced when I can."
    "But for right now, I just want to get to a bed."


##########################################################################
    #Talking to Jamie
    scene bg hotel night with fade

    "When I get back into my hotel room, I'm about eight seconds from passing out on the bed."
    "I only barely manage to wash my face and brush my teeth before I'm laying on the mattress over the covers, looking at the ceiling."
    "Today was..."
    "A lot."

    scene black with Dissolve(2.0)
    stop music fadeout 1.0

    play sound "assets/sfx/phone ring.wav"
    $ renpy.pause (1.0)
    scene bg hotel night with Dissolve(0.2)
    "The sound of my room phone snaps me back to the real world."
    "I'm hesitant to pick it up, since it seems like only bad news has been coming my way so far."
    "But I don't really know who would have this number aside from important people, so..."
    "I slap my face a little to wake myself up and answer the phone."
    stop sound
    play sound "assets/sfx/phone pickup.mp3"
    me "Hello?"
    q "%(povf)s!"
    me "Who is this?"
    me "Wait..."
    "This voice... I know this voice!"
    "How do I know this voice?"
    me "Is this, uh... Jamie?"
    play music music_daily fadein 1.0
    q "Hahaha, took you long enough!"
    j "You seemed so out of it this morning, have you really forgotten about me so quickly?"
    me "Jamie, you fuck! You couldn't have given me any extra warning?"
    j "Hey man, I gave you all the warning you needed."
    j "I'm laid out for now, I can't come into work. Everything's fine, don't worry, but I'm not really in shape to travel."
    j "I figured you were the best bet for the job, so I gave Vince my recommendation."
    me "I can't believe this."

    "Jamie laughs while I fume."
    "Jamie Moore... My senior at work and, well, a 'fellow' match manager."
    "They clearly have a higher standing than I do, though, since they get to deal primarily with main eventers."
    "They've even worked Wrestlemanias before. I can't even get close."
    "So that explains why I all of a sudden had to deal with Shawn Michaels and The Undertaker, but..."
    "But why me in the first place?"
    "We're not even that close of friends."
    "Hell, they never even crossed my mind this entire time."
    "We'd only met once or twice, at company functions."
    "I mean, I guess I thought we were friendly with each other, but they were really just a co-worker, not a friend."
    "We've never spoken to each other about anything that wasn't directly related to our jobs."
    me "Why did you give Vince my name?"
    "I can't keep myself from asking them the only thing on my mind."

    j "You're a hard worker, %(povf)s. You have to have a good head on your shoulders to work with Michaels and 'Taker."
    j "I believed you'd be able to do it."
    me "That's flattering, but still..."
    j "How was your first day with the higher ups?"
    "Jamie cuts me off. I bet they knew what I was going to ask."
    "But why me?"
    "It feels like a the mayor giving a hobo their job because they have the flu."
    "But I'm just so... exhausted."
    "I don't want to push it right now."
    me "Stressful."
    j "Sounds about right."
    "They laugh, and I sit back on the hotel bed, staring at the ceiling."
    j "So, you got the two big ones, huh?"
    j "The main eventers!"
    j "Any major concerns so far?"

    menu:
        #Who Concerns You
        j "Any major concerns so far?{fast}"

        "Shawn Michaels":
            $ dx_points += 1
            me "The Heartbreak Kid, of course."
            "There's absolutely no pause when I speak."
            me "He's just..."
            j "A handful?"
            me "Yeah."
            me "That's a way of putting it."
            j "He's not as bad as he seems. He's just bad at admitting he needs help."
            "I roll my eyes, unable to remember a part of me or my personality that he had yet to insult."
            j "He'll probably bother Vince more than you, though, so just keep an eye on his lackies."
            me "Helmsley and Chyna?"
            j "Yeah, they'll cause trouble if you let them."
            j "Mostly they just hang with Michaels and act like mean girls, but don't forget that they're also their own people."

        "The Undertaker":
            $ taker_points += 1
            me "The Undertaker."
            "There's absolutely no pause when I speak."
            me "He's a, uh..."
            me "...Very intimidating man."
            "Jamie laughs."
            j "He gets scarier the closer you stand to him, doesn't he?"
            me "Yeah."
            "I remember him appearing right next to me right before he went out to the stage, and how it felt like my heart was going to leap out of my chest."
            j "He's a private one, though, with a lot on his mind."
            j "I can't even come close to understanding what he's concerned about, so I'd recommend you don't try."
            j "I mean, you {i}could{/i} but that'd probably be a huge effort, so just be prepared for that."
            j "Just make sure you take care of yourself, first."

        "Not really" if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True:
            $ kane_points += 1
            "I pause for a bit before I speak."
            me "Not really, actually."
            "Jamie is patient while I think about how to continue."
            me "I mean, I don't think this will be easy, but no one seems {i}too{/i} bad so far."
            "Jamie chuckles."
            j "That's a surprise!"
            j "I would've thought 'Taker would've been an issue."
            me "Well, yeah, but, y'know."
            "Very eloquent on my part, I know, but I'm being honest."
            "None of them are easy to handle, but no one will really be making me regret being forced into this position."
            j "I'd say you're right, actually. The real problems come from forces outside the Superstars."
            j "They're a drain on your energy, but not really the final goal, y'know?"



    me "Yeah, got it."
    "I let out a breath, feeling how heavy my body is."
    "Man, I guess I should've expected this."
    "I never realized how much pressure Jamie was under while working."
    "I thought I was just bad at talking to wrestlers, but I guess that's what they're always like."
    "And, well, they must be worse than I thought, if none of them had any idea that Jamie was the one missing."
    "I mean, Jamie works with them a lot, obviously, and there was just amnesia on their part."
    "Okay, I forgot about Jamie, too, but I've got an excuse."
    "I guess. Whatever."
    "I don't want to mess this up."
    "Not the Pay-Per-View, not my job."
    "Not my life."
    j "Do you have anything else you'd like to ask?"
    j "I can't really help out much since I'm stuck at home, but least I can do is offer some words of advice."
    "Jamie's voice is reassuring, and I can tell that I can trust them."
    "I remember feeling like this the first time we met, like Jamie was someone worth hanging around."
    "But our jobs just kept us apart, and when you never see anyone, it's hard to be friends with them."
    me "No, I think I'm good for now."
    "I'm not lying when I speak."
    "There's so many things pressing against the inside of my skull, so many questions I have, but I'm fine."
    "I mostly just want to sleep."
    j "Just stay strong, alright?"

    #Point Check (3 Q so far)
    if dx_points >= 2:
        j "Don't let Michaels annoy you too much."
    elif taker_points >= 2:
        j "Don't let 'Taker bother you too much."
    else:
        j "Don't let those guys get under your skin too much."

    me "You know it."
    me "Thanks again, {i}pal{/i}."
    "Jamie laughs at the sarcasm in my voice."
    j "Hey, I'm kickstarting your career, man!"
    j "You'll thank me for this once the week is up."
    me "Sure, sure."
    j "I'll call you again tomorrow, just to check in."
    me "Wait, how will you get my number?"
    "Jamie laughs again."
    j "Good luck!"
    play sound "assets/sfx/phone hangup.mp3"

    "I hang up the phone."
    "So that at least settles that."
    "So, now that I have my job set up and someone to support me..."
    "I guess all I have to do is just... do well."
    "Yeesh."
    "Well, whatever. I have to get up early tomorrow to travel to the new stadium."
    "I'll just go to sleep and see what happens in the morning."
    stop music fadeout 1.0



    jump Day2






