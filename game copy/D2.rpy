label Day2:

    scene black with dissolve
    "..."
    scene bg hotel day with dissolve
    "...I didn't sleep that well last night."
    play music music_morning fadein 1.0
    window hide
    call calendar(1)
    window show
    "I guess it's to be expected."
    "I fell asleep pretty much instantly, but morning felt like it came way too quick."
    "Ultimately, when I finally got up, it felt like I hadn't really slept at all."
    "I get up and stretch, the pain in my wrist a major bummer."
    "I guess I still have to keep it wrapped up."
    "It's an annoyance, but actually does help the pain."
    "And working in wrestling, I've seen small sprains turn into something much worse, so I don't mind putting the wraps back on."  
    "I get my things together to head out to the new city for the next show."
    "Usually, there isn't house shows on weekdays, but with the Pay-Per-View coming up, Vince wants to hype up the event as much as possible."
    "Therefore, this week is going to be pretty damn busy."
    "I'll be riding to the next show alone, which is..."
    "Well, it sucks."
    "Since my last promotion from stagehand to lower level match manager, I hadn't really been able to ride the buses with the crew."
    "You lose permission to sit near expensive equipment when you're not supposed to be there, after all."
    "I used to always ride with fellow stagehands, but since then, I'd just gotten on the rental car grind."
    "I don't have many manager friends. Jamie, I guess, is an exception."
    "But even then, they were with the higher level managers, anyway."
    "I've mentioned it before, but WWF is so seniority-based that it's honestly rude to be upset about how badly newcomers get treated."
    "And even though I haven't been a newcomer for years, I'm still new."
    "But, whatever."
    "This is starting to get a little too self-pity-ish."
    "I'm used to the routine by now."
    "The next city is four hours from here."
    "From cloudy Albany, New York to slightly less cloudy Rochester, New York."
    "My bags are packed, my wrist is wrapped, and my cassettes are ready."
    "Let's do this!"
    stop music fadeout 1.0

    scene black with Dissolve(1.5)
    play sound "assets/sfx/car.mp3"
    $ renpy.pause (1.0)
    scene bg stage setup with Dissolve(1.5)
    play music music_fretless

    "New arena, same old setup."
    "I arrive with more than enough time for the house show, and by the looks of it, I'm still kind of early."
    "Everyone who needs to be here just kind of gets here on their own time, aside from crew, of course."
    "As long as you're out for your match, then no one really cares."
    "At least house shows are more relaxed than their televised counterparts."
    "Yesterday was a bit much, so I'd reaaaaally love it if we didn't have a repeat."

    scene bg hallway with fade
    "Another upside to house shows is that Vince always lists the matches beforehand, so there's no element of surprise."
    "He doesn't have anything to gain from changing match plans on the fly, so he usually decides them the night before, or even the day of."
    "What this means for everyone is a more stable night, and a more relaxed ride home."
    "I head over to the bulletin board to find the match listing for the night."
    "It's near catering, as always."
    play sound "assets/sfx/10_paper.mp3"
    "Let's see here..."
    centered "{font=assets/fonts/TrashHand.ttf}{size=+30}MATCH LISTINGS FOR 9/30/1997{/size}{/font}"
    play sound "assets/sfx/10_paper.mp3"
    centered "{font=assets/fonts/TrashHand.ttf}{size=+10}Hunter Hearst Helmsley VS. Rockabilly{p}...{p}Shawn Michaels VS. Ken Shamrock{/size}{/font}"
    play sound "assets/sfx/10_paper.mp3"
    centered "{font=assets/fonts/TrashHand.ttf}{size=+10}...{p}The Undertaker VS. Goldust{/size}{/font}"
    "Oh, thank God."
    "Those two are stressful enough alone, I definitely don't need them fighting each other before the Pay-Per-View."
    "Well, at least in the ring."
    "It's my job to make sure there's no fights in the parking lot, which is sadly a possibility."

    play sound "assets/sfx/footsteps.mp3"
    scene bg hallway with fade
    "It's impressive how every stadium just blurs together."
    "I passed by catering, munching on most of the snack items, replacing a decent lunch with something much less healthy."
    "Now I'm back in the main hallway, the vein of the arena that runs past all the locker rooms and important areas."
    "There was nothing of note anywhere, and my walkthrough was just to get myself acquainted, just in case."
    "Especially after last night..."
    "I just want to make sure that if anything bad happens, I at least know where the fire exits are."
    "It's starting to get closer to showtime, so wrestlers are starting to wander in, hidden in baggy clothes, carrying duffel bags."
    "Time for me to keep an eye out for the troublemakers I'm in charge of."
    stop music fadeout 1.0

    c "You're unbelievable."
    "Well then."
    play music music_chyna fadein 1.0
    show hunter:
        xpos 0.25
    show chyna:
        xpos 0.55
    with img_dissolve
    "Chyna and Hunter are already arguing again."
    "It's not really a surprise, although it is unexpected."
    "It feels like things have gotten worse with them, somehow. Not since yesterday, but just in general."
    "To be honest, it's pretty uncomfortable to see them fight all the time like this, not even loud or obnoxious, just very personal."
    "They've got this ongoing lover's spat that's starting to involve more people, and I know from experience that it sucks."
    "For their own sake, I decide to step in, try and intervene or something."
    "I'm not expecting them to use me as their relationship counsellor all of a sudden or anything, but, I don't know."
    "I just want to help them."
    play sound "assets/sfx/walking.mp3"
    "I step up to them cautiously, as if I was going to spook them otherwise."
    "My discretion goes to waste. Hunter notices me instantly, and sneers at me."
    show hunter angry
    h "What do you think you're doing?"
    me "Sorry, I just thought --"
    h "No one cares."

    scene bg hallway 
    show hunter:
        xpos 0.25
    show chyna:
        xpos 0.55
    with hpunch
    play sound "assets/sfx/fall.wav"
    "Hunter plants a huge hand square on my chest and pushes me away, making me stumble."
    "I manage to catch myself in time, so I don't fall on my wrist again like yesterday, but I definitely hit the wall."
    hide hunter
    show chyna at center
    with img_dissolve
    play sound "assets/sfx/walking.mp3"
    "Hunter, unrepentant, already walks away, his shoulders tense."
    "Chyna gives me a long look, but doesn't speak a word."
    "At this point, I think I'm used to this."
    "I look back at her, although I'm not entirely sure what emotion I'm showing on my face."
    hide chyna with img_dissolve
    stop music fadeout 1.0
    "Silently, Chyna turns and follows Hunter, equally as tense."
    "Some of the people backstage noticed the entire exchange, and I can feel their curious looks."
    "They're probably all wondering what this newbie is doing interfering with Helmsley and Chyna's argument, like a Goddamn imbecile."
    "It's just painful seeing them fight like that all the time."

    if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True:
        "I'm nursing my emotional wound when I hear a high pitched voice behind me."
        q "Ex-cuuuse me!"
        "I naturally step out of the way, wondering how I knew the voice."
        play music music_confused
        show paul with img_dissolve
        "I recognize the man behind the voice instantly."
        "That's... Paul Bearer, the man who brought the Undertaker up through the ranks."
        "But, he's basically been MIA recently, since he and the Undertaker had their falling out."
        "He notices me looking at him and gives me an odd look."
        p "Is there something you need?"
        "His tone is accusatory and insulting, somehow."
        "I shake my head, and he continues on his way."
        hide paul with img_dissolve
        "I watch him go, confused."
        "Why is here in the arena?"
        "Does the Undertaker know about this?"
        "Am I supposed to alert him?"
        stop music fadeout 1.0
        "Wait, what am I doing, thinking this hard about this."
        "I shake my head. I don't know a damn thing about the Undertaker, anyway."
        "There's no point in getting caught up in this now."

    scene bg backhalls with fade
    "Out of pure curiosity, I head around the back of the stadium."
    "I'm not sure if I'll find the Undertaker here or not, but it's worth a hot."
    "To be honest, it'd be pretty funny if he {i}were{/i} back here, like he's some sort of raccoon who hangs out with the dumpsters."
    "I don't even know if he's here or not, to be honest."
    "But, the Undertaker is usually very prompt to shows and matches. He's earnest in that way."
    "It's not like he's ever called in a sick day."
    "Can dead men even get sick?"
    "...That's a joke. He's not a dead man."
    "As Shawn said, he's just a scary guy with an eyebrow piercing."
    "Anyway, I'm approaching this arena's loading dock area, the same place I met the Undertaker yesterday."
    "It's not strange for wrestlers to come in through this way, anyway, since it's more secluded and has easier access than the main or side doors."
    "Some of the crew recognize me and give me small nods and waves of hello. I reciprocate in kind."
    "I'm not finding the Undertaker anywhere, and I guess it was a pipe dream."
    "I turn around to head back to the front, and catch a glimpse of long dark hair."
    "...Most wrestlers have long hair, but I take a chance and head towards it."

    play sound sound_footsteps
    show taker with img_dissolve
    play sound "assets/sfx/thunder1.mp3"
    "Sure enough, it's the man of the hour."
    "He notices me approaching him and turns around, taciturn as ever."
    me "Hey!"
    "No response, but I expected as much."
    "Being so near him is actually pretty scary, but I bite down whatever fear I have and try to put on a positive face."
    "He's not even doing anything, but he's just so tall, dark, and intimidating."
    play music "assets/music/05_Marty_Gots_a_Plan_incompetech.mp3" fadein 2.0
    me "I hope I'm not interrupting you, I just wanted to talk to you about your match today!"
    me "Did you see the listings? They're up in the main hall."
    me "You've got a match against Goldust! You're the main event."
    "Other than a small nod, there's no other reaction from the Undertaker."
    me "I know you've had a bunch of matches with him already, so I'm sure you've got this in the bag."
    me "And I bet you're as glad as I am that you won't be dealing with Helmsley or Michaels tonight."
    me "We definitely don't need any more incidents mucking up the works."
    "I know I'm totally just prattling off, but the quieter the Undertaker stays, the more awkward I feel, and I try to fill the silence."
    me "Speaking of, thanks for last night."
    me "I'm glad we could end the show without too much stress."
    me "But all that matters is that we're one step closer to the Pay-Per-View!"
    me "Everything's running smooth administratively, so fingers crossed that it goes the same with the talent."
    "...Okay, this is exhausting."
    "I'm sure he just wants to bail on me now, anyway."
    "I hesitate for a second, then look the big man in the eyes, trying to gauge his mood."
    "Surprisingly enough, he doesn't seem annoyed or angry."
    "In fact, he actually seems attentive."
    "I'm at a loss for words."
    "I can tell he notices, because he turns to leave, assuming my rambling has finally come to an end."
    me "Um, bye."
    "The Undertaker pauses, gives me a small nod, and then walks away."
    hide taker with img_dissolve
    stop music fadeout 1.0
    "...{p=0.5}Strange."

    scene bg hallway with fade
    "The main hallway is starting to noticeably fill up when I get back."
    "Wrestlers in all states of dress crowd the match listings, wanting to see how early they can leave and head to a hotel."
    "The stagehands seem more frantic than usual, making me relieved that it's not really any of my concern."
    if taker_points >= 3:
        "Although, the relief does make me feel a bit guilty..."
    "I'm still waiting on a certain wrestler to show up, anyway."
    "Maybe I should find Hunter and Chyna again, they might know where Shawn is."
    "But, I don't really want to get pushed around again."
    "I'll just hang out near the front doors for a while, maybe catch him coming in or something."
    "I'm pretty sure he's not in the stadium already. I feel like I would've been able to tell if he caused a disturbance."
    "...Like right now."
    show shawn with img_dissolve
    play music music_shawn fadein 1.0
    "Shawn's clearly... off."
    "I hear his laughter coming from down the hall, and when I go to find the source, I see him with a beer in hand, chatting with one of the more attractive stagehands."
    "He notices me and rolls his eyes, clearly over me."
    s "I'll see you later babe, gotta work now."
    "The stagehand makes a sad sound, her hand trailing off his chest, but she walks away anyway."
    "I don't recognize her, but that's not a surprise. Whether she's a ring rat or not isn't really any of my concern."
    "Shawn can bone half the city if he wants, as long as it doesn't interfere with his wrestling."
    "And him being drunk can definitely interfere."
    "I step closer, and Shawn audibly sighs."
    s "What is it? You got somethin' you wanna say?"
    me "I'm just checking on you."
    me "I'm worried, Shawn."
    s "Pffft."
    s "Worried about what?"
    if chick == True:
        s "Don't tell me you're jealous, babe."
        "I ignore that."
    me "You're drunk, Shawn, and you have a match tonight."
    me "Have you even looked at the match list?"
    "Shawn shrugs, and I can tell he's getting annoyed."
    s "You really {i}are{/i} new to this."
    
    if chick == True:
        s "This ain't nothin', babe."
    else:
        s "This ain't nothin'."

    s "Not the first time anyone's shown up to a show drinkin' a beer and definitely not the last."
    s "So you can just calm right down, 'kay?"
    "Shawn's definitely"






#Match To Watch

    "I get asked to help, but I'm allowed to watch a match first."

    menu:
        "Shawn's":
            $ dx_points += 1
            $ shawn_match = True

        "The Undertaker's":
            $ taker_points += 1
            $ taker_match = True

        "Neither" if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True:
            $ kane_points += 1

    "Ok cool."


    if shawn_match == True:
        "It's time to watch Shawn's match."

    st "Help me move crates."

    if shawn_match == False and taker_match == False:
        "Taker's match is about to start, but I opted out. Cameras are weird."

    "Shawn, Hunter, and Chyna all left before the main event was over."
    "Taker came backstage."

    if taker_match == True:
        "I watched his match."
    if taker_match == False:
        "I didn't watch his match."

    "I ask Taker if he is doing alright. He replies."
    "I ask him if he is in any pain. He replies."

    if taker_match == False:
        "The conversation ends here."
    if taker_match == True:
        "I mention the glitter in his hair."





#Staying Late
    menu:
        "Stay behind":
            $ taker_points += 1
            "I stay behind."
            t "Aren't you afraid of the dark?"
            me "No."
            t "You should be."

        "Just leave":
            $ dx_points += 1
            "I will go home."

        "Look around first" if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True:
            $ kane_points += 1
            "There is a spooky broken lock."





#Point Check

    j "How are things?"

    if dx_points >=3:
        me "DX does suck."

    elif taker_points >=3:
        me "It's hard to talk to Taker."

    else: #default to taker text
        me "It's hard to talk to Taker."

    "Time to sleep."

    if dx_points >=3:
        jump Day3_DX
    elif taker_points >=3:
        jump Day3_TK
    else:
        jump Day3_TK

    return





