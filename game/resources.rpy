# Resources used by the whole game
init -1:
    # -- Transitions to use with set_state() ---------------------------
    python:
        img_dissolve = Dissolve(0.2, alpha=True)


        # -- Music ---------------------------------------------------------
        music_shawn = "assets/music/Sexy Boy.mp3"
        music_vince = "assets/music/No Chance In Hell.mp3"
        music_hunter = "assets/music/Blue Blood.mp3"
        music_chyna = "assets/music/Who I Am.mp3"
        music_taker = "assets/music/UT Graveyard Symphony.mp3"
        music_kane = "assets/music/burned.mp3"

        music_kabul = "assets/music/Kabul Flight.mp3"
        music_silly = "assets/music/silly_fun_loop.mp3"
        music_morning = "assets/music/Orangebeat - Akki_Loop.mp3"
        music_fretless = "assets/music/Fretless.mp3"
        music_daily = "assets/music/Orangebeat - Daily Life Suite_Loop_1_relax.mp3"
        music_stress = "assets/music/Corruption.mp3"
        music_show = "assets/music/Delay Rock.mp3"
        music_confused = "assets/music/Awkward Meeting.mp3"
        music_scared = "assets/music/Mud Bath.mp3"
        music_mystic = "assets/music/Lightless Dawn.mp3"
        music_mischevious = "assets/music/Sneaky Snitch.mp3"
        music_afterhours = "assets/music/Brittle Rille.mp3"
        

        # -- Sounds ---------------------------------------------------------

        sound_footsteps = "assets/sfx/footsteps.mp3"
        sound_walking = "assets/sfx/walking.mp3"
        sound_car = "assets/sfx/car.mp3"
        sound_door = "assets/sfx/door.mp3"
        sound_doorslow = "assets/sfx/door4.mp3"
        sound_knocking = "assets/sfx/knocking.mp3"
        sound_fall = "assets/sfx/fall.mp3"
        sound_phonehang = "assets/sfx/phone hangup.mp3"
        sound_phonepick = "assets/sfx/phone pickup.mp3"
        sound_phonering = "assets/sfx/phone ring.wav"




# -- Images ---------------------------------------------------------

init python:
    import os
    def define_characters(characterImageFolder, excludeFirstXFolders=0, flip=False):
        for path in renpy.list_files():
            if path.startswith(characterImageFolder + "/"):
                path_list = path.split("/")
                path_list[-1] = os.path.splitext(path_list[-1])[0]
                path_list = tuple(path_list[excludeFirstXFolders:])
                renpy.image(path_list, path)
                if flip:
                    renpy.image(path_list + ("flip", ), im.Flip(path, horizontal=True))
                    
    define_characters("images", 1)




define red_flash = Fade(0.0, 0.1, 0.1, color="#ff0000")
define flash = Fade(0.1, 0.1, 0.1, color="#ffffff")

init:

    #Backgrounds
    #image bg hotel day = "images/BG/hotelday.png"
    #image bg hotel night = 
    #image bg gorilla dark = image bg ruin_path_night = im.MatrixColor("images/BG/gorilla.png", im.matrix.tint(0.5,0.5,0.6), * im.matrix.brightness(-0.2))


    #Vince
    #image vince normal = "images/Vince/vince normal.png"


    #Shawn


    #Hunter


    #Chyna


    #Taker


    #Kane


    #Bearer


    #Rick


    #Assistant


    #Stagehand


    #CGs
    image cg1 = "images/cg1.jpg"
    image cg2 = "images/cg2.jpg"












