label Day4_TK:

    "I am flown out to the arena."

    if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True and if kane_points >= 7:
        "There's a spooky noise."
        menu:
            "Check the noise":
                $ kane_points +=1
                jump Day4_K

            "Keep walking":
                pass

    if persistent.shawn_end == True and persistent.hunter_end == True and persistent.chyna_end == True and persistent.taker_end == True and if kane_points <= 6:
        "There's a spooky noise but I keep walking."


    "Taker's story continues."


    #jump Day5_T