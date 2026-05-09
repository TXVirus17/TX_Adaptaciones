init 5 python:
    addEvent(
        Event(
            persistent.event_database,eventlabel="monika_succubus"
            ,unlocked=True,
            category=['appearance','clothes','roleplay'],
            prompt="would you like to play that you are a demon with me?",
            pool=True,))

label sot:
    image sot_p1 = "Submods/succubus/sot/sot_p1.png"
    image sot_p2 = "Submods/succubus/sot/sot_p2.png"
    image sot_p3 = "Submods/succubus/sot/sot_p3.png"
    image r_p1 = "Submods/succubus/sot/r/r_p1.png"
    image r_p2 = "Submods/succubus/sot/r/r_p2.png"
    image sot_k1 = "Submods/succubus/sot/sotk1.png"
    image sot_k2 = "Submods/succubus/sot/sotk2.png"
    image r_k1 = "Submods/succubus/sot/r/r_sotk1.png"
    image r_k2 = "Submods/succubus/sot/r/r_sotk2.png"

    #s
    image sot_p1_n = "Submods/succubus/sot/n/sot_p1_n.png"
    image sot_p2_n = "Submods/succubus/sot/n/sot_p2_n.png"
    image sot_p3_n = "Submods/succubus/sot/n/sot_p3_n.png"
    image sot_k1_n = "Submods/succubus/sot/n/sotk1_n.png"
    image sot_k2_n = "Submods/succubus/sot/n/sotk2_n.png"

label expresions_sot:
    image sot_exp_angry_wide = "Submods/succubus/sot/expresions/angry_wide.png"
    image sot_exp_bsmile_soft = "Submods/succubus/sot/expresions/bsmile_soft.png"
    image sot_exp_bsmile_normal = "Submods/succubus/sot/expresions/bsmile_normal.png"
    image sot_exp_bsmile_smug = "Submods/succubus/sot/expresions/bsmile_smug.png"
    image sot_exp_smal_soft = "Submods/succubus/sot/expresions/smal_soft.png"
    image sot_exp_smal_left = "Submods/succubus/sot/expresions/smal_left.png"
    image sot_exp_smal_wide = "Submods/succubus/sot/expresions/smal_wide.png"
    image sot_exp_smile_closedsad = "Submods/succubus/sot/expresions/smile_closedsad.png"
    image sot_exp_smile_soft = "Submods/succubus/sot/expresions/smile_soft.png"
    image sot_exp_smile_normal = "Submods/succubus/sot/expresions/smile_normal.png"
    image sot_exp_smile_smugthink = "Submods/succubus/sot/expresions/smile_smugthink.png"
    image sot_exp_smirk_crazy = "Submods/succubus/sot/expresions/smirk_crazy.png"
    image sot_exp_smirk_leftthink = "Submods/succubus/sot/expresions/smirk_leftthink.png"
    image sot_exp_smirk_wide = "Submods/succubus/sot/expresions/smirk_wide.png"
    image sot_exp_kiss_closedh = "Submods/succubus/sot/expresions/kiss_closedh.png"

#sot expressions
label sot_exp_angry_wide:
    call inexpresive
    show sot_exp_angry_wide zorder 11
    return

label sot_exp_bsmile_normal:
    call inexpresive
    show sot_exp_bsmile_normal zorder 11
    return
    
label sot_exp_bsmile_soft:
    call inexpresive
    show sot_exp_bsmile_soft zorder 11
    return
label sot_exp_bsmile_smug:
    call inexpresive
    show sot_exp_bsmile_smug zorder 11
    return

label sot_exp_smal_soft:
    call inexpresive
    show sot_exp_smal_soft zorder 11
    return

label sot_exp_smal_left:
    call inexpresive
    show sot_exp_smal_left zorder 11
    return

label sot_exp_smal_wide:
    call inexpresive
    show sot_exp_smal_wide zorder 11
    return

label sot_exp_smile_soft:
    call inexpresive
    show sot_exp_smile_soft zorder 11
    return

label sot_exp_smile_closedsad:
    call inexpresive
    show sot_exp_smile_closedsad zorder 11
    return

label sot_exp_smile_normal:
    call inexpresive
    show sot_exp_smile_normal zorder 11
    return

label sot_exp_smile_smugthink:
    call inexpresive
    show sot_exp_smile_smugthink zorder 11
    return

label sot_exp_smirk_crazy:
    call inexpresive
    show sot_exp_smirk_crazy zorder 11
    return
label sot_exp_smirk_leftthink:
    call inexpresive
    show sot_exp_smirk_leftthink zorder 11
    return

label sot_exp_smirk_wide:
    call inexpresive
    show sot_exp_smirk_wide zorder 11
    return
label sot_exp_kiss_closedh:
    call inexpresive
    show sot_exp_kiss_closedh zorder 11
    return

#sot poses
label sot_p1:
    call clear_pose
    show sot_p1 zorder 10
    if persistent._mas_acs_enable_promisering:
        show r_p1 zorder 11
    if mas_isNightNow():
        show sot_p1_n zorder 12
    return

label sot_p2:
    call clear_pose
    show sot_p2 zorder 10
    if persistent._mas_acs_enable_promisering:
        show r_p2 zorder 11
    if mas_isNightNow():
        show sot_p2_n zorder 12
    return

label sot_p3:
    call clear_pose
    show sot_p3 zorder 10
    if mas_isNightNow():
        show sot_p3_n zorder 12
    return
label sot_k1:
    call clear_pose
    call inexpresive
    show sot_k1 zorder 13
    if persistent._mas_acs_enable_promisering:
        show r_k1 zorder 14
    if mas_isNightNow():
        show sot_k1_n zorder 15
    return
label sot_k2:
    call clear_pose
    call inexpresive
    show sot_k2 zorder 13
    if persistent._mas_acs_enable_promisering:
        show r_k2 zorder 14
    if mas_isNightNow():
        show sot_k2_n zorder 15
    return

label sfb:
    #torso
    image sfb_hands_behind ="/Submods/succubus/sfb/torso/hands_behind.png"
    image sfb_pointing ="/Submods/succubus/sfb/torso/pointing.png"
    image sfb_shi ="/Submods/succubus/sfb/torso/shi.png"
    image sfb_poinshi ="/Submods/succubus/sfb/torso/poinshi.png"
    image sfb_modeling ="/Submods/succubus/sfb/torso/modeling.png"

    #torso night
    image sfb_hands_behind_n ="/Submods/succubus/sfb/torso/n/hands_behind_n.png"
    image sfb_pointing_n ="/Submods/succubus/sfb/torso/n/pointing_n.png"
    image sfb_shi_n ="/Submods/succubus/sfb/torso/n/shi_n.png"
    image sfb_poinshi_n ="/Submods/succubus/sfb/torso/n/poinshi_n.png"
    image sfb_modeling_n ="/Submods/succubus/sfb/torso/n/modeling_n.png"

    #ring
    image sfb_r_pointing = "/Submods/succubus/sfb/ring/pointing_r.png"
    image sfb_r_shi = "/Submods/succubus/sfb/ring/shi_r.png"

    #legs
    image sfb_legs1 = "Submods/succubus/sfb/legs/pose1.png"
    image sfb_legs2 = "Submods/succubus/sfb/legs/pose2.png"
    #legs niht
    image sfb_legs1_n = "Submods/succubus/sfb/legs/n/pose1_n.png"
    image sfb_legs2_n = "Submods/succubus/sfb/legs/n/pose2_n.png"

label expresions_sfb:
    image sfb_exp_bsmile_smug = "Submods/succubus/sfb/expressions/bigsmile_smug.png"
    image sfb_exp_bsmile_think = "Submods/succubus/sfb/expressions/bigsmile_thinking.png"
    image sfb_exp_smal_normal = "Submods/succubus/sfb/expressions/smal_normal.png"
    image sfb_exp_smal_smugright = "Submods/succubus/sfb/expressions/smal_smug_right.png"
    image sfb_exp_smal_soft = "Submods/succubus/sfb/expressions/smal_soft.png"
    image sfb_exp_smal_wide= "Submods/succubus/sfb/expressions/smal_wide.png"
    image sfb_exp_smile_closed = "Submods/succubus/sfb/expressions/smile_closed.png"
    image sfb_exp_smile_left = "Submods/succubus/sfb/expressions/smile_left.png"
    image sfb_exp_smile_normal = "Submods/succubus/sfb/expressions/smile_normal.png"
    image sfb_exp_smile_rigth = "Submods/succubus/sfb/expressions/smile_right.png"

#full bodie poses
label sfb_poitning1:
    call clear_pose
    show sfb_legs1 zorder 4
    if mas_isNightNow():
        show sfb_legs1_n zorder 5
    show sfb_pointing zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_pointing zorder 7
    if mas_isNightNow():
        show sfb_pointing_n zorder 8
    return
label sfb_poitning2:
    call clear_pose
    show sfb_legs2 zorder 4
    if mas_isNightNow():
        show sfb_legs2_n zorder 5
    show sfb_pointing zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_pointing zorder 7
    if mas_isNightNow():
        show sfb_pointing_n zorder 8
    return
label sfb_hands_behind1:
    call clear_pose
    show sfb_legs1 zorder 4
    if mas_isNightNow():
        show sfb_legs1_n zorder 5
    show sfb_hands_behind zorder 6
    if mas_isNightNow():
        show sfb_hands_behind_n zorder 8
    return
label sfb_hands_behind2:
    call clear_pose
    show sfb_legs2 zorder 4
    if mas_isNightNow():
        show sfb_legs2_n zorder 5
    show sfb_hands_behind zorder 6
    if mas_isNightNow():
        show sfb_hands_behind_n zorder 8
    return
label sfb_shi1:
    call clear_pose
    show sfb_legs1 zorder 4
    if mas_isNightNow():
        show sfb_legs1_n zorder 5
    show sfb_shi zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_shi zorder 7
    if mas_isNightNow():
        show sfb_shi_n zorder 8
    return
label sfb_shi2:
    call clear_pose
    show sfb_legs2 zorder 4
    if mas_isNightNow():
        show sfb_legs2_n zorder 5
    show sfb_shi zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_shi zorder 7
    if mas_isNightNow():
        show sfb_shi_n zorder 8
    return
label sfb_poinshi1:
    call clear_pose
    show sfb_legs1 zorder 4
    if mas_isNightNow():
        show sfb_legs1_n zorder 5
    show sfb_poinshi zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_shi zorder 7
    if mas_isNightNow():
        show sfb_poinshi_n zorder 8
    return
label sfb_poinshi2:
    call clear_pose
    show sfb_legs2 zorder 4
    if mas_isNightNow():
        show sfb_legs2_n zorder 5
    show sfb_poinshi zorder 6
    if persistent._mas_acs_enable_promisering:
        show sfb_r_shi zorder 7
    if mas_isNightNow():
        show sfb_poinshi_n zorder 8
    return
label sfb_modeling1:
    call clear_pose
    show sfb_legs1 zorder 4
    if mas_isNightNow():
        show sfb_legs1_n zorder 5
    show sfb_modeling zorder 6
    if mas_isNightNow():
        show sfb_modeling_n zorder 8
    return
label sfb_modeling2:
    call clear_pose
    show sfb_legs2 zorder 4
    if mas_isNightNow():
        show sfb_legs2_n zorder 5
    show sfb_modeling zorder 6
    if mas_isNightNow():
        show sfb_modeling_n zorder 8
    return

#full bodie expressions
label sfb_exp_bsmile_smug:
    call inexpresive
    show sfb_exp_bsmile_smug zorder 7
    return
label sfb_exp_bsmile_think:
    call inexpresive
    show sfb_exp_bsmile_think zorder 7
    return
label sfb_exp_smal_normal:
    call inexpresive
    show sfb_exp_smal_normal zorder 7
    return
label sfb_exp_smal_smugright:
    call inexpresive
    show sfb_exp_smal_smugright zorder 7
    return
label sfb_exp_smal_soft:
    call inexpresive
    show sfb_exp_smal_soft zorder 7
    return
label sfb_exp_smal_wide:
    call inexpresive
    show sfb_exp_smal_wide zorder 7
    return
label sfb_exp_smile_closed:
    call inexpresive
    show sfb_exp_smile_closed zorder 7
    return
label sfb_exp_smile_left:
    call inexpresive
    show sfb_exp_smile_left zorder 7
    return
label sfb_exp_smile_normal:
    call inexpresive
    show sfb_exp_smile_normal zorder 7
    return
label sfb_exp_smile_rigth:
    call inexpresive
    show sfb_exp_smile_rigth zorder 7
    return

#clean comands
label inexpresive:

    hide sot_exp_angry_wide
    hide sot_exp_bsmile_normal
    hide sot_exp_bsmile_soft
    hide sot_exp_bsmile_smug
    hide sot_exp_smal_soft
    hide sot_exp_smal_left
    hide sot_exp_smal_wide
    hide sot_exp_smile_soft
    hide sot_exp_smile_closedsad
    hide sot_exp_smile_normal
    hide sot_exp_smile_smugthink
    hide sot_exp_smirk_crazy
    hide sot_exp_smirk_leftthink
    hide sot_exp_smirk_wide
    hide sot_exp_kiss_closedh

    hide sfb_exp_bsmile_smug
    hide sfb_exp_bsmile_think
    hide sfb_exp_smal_normal
    hide sfb_exp_smal_smugright
    hide sfb_exp_smal_soft
    hide sfb_exp_smal_wide
    hide sfb_exp_smile_closed
    hide sfb_exp_smile_left
    hide sfb_exp_smile_normal
    hide sfb_exp_smile_rigth
    return

label clear_pose:
    hide sot_p1
    hide sot_p1_n
    hide sot_p2
    hide sot_p2_n
    hide sot_p3
    hide sot_p3_n
    hide sot_k1
    hide sot_k1_n
    hide r_k1
    hide sot_k2
    hide sot_k2_n
    hide r_k2
    hide r_p1
    hide r_p2

    hide sfb_hands_behind
    hide sfb_hands_behind_n
    hide sfb_pointing
    hide sfb_pointing_n
    hide sfb_shi
    hide sfb_shi_n
    hide sfb_poinshi
    hide sfb_poinshi_n
    hide sfb_modeling
    hide sfb_modeling_n
    hide sfb_legs1
    hide sfb_legs1_n
    hide sfb_legs2
    hide sfb_legs2_n
    hide sfb_r_pointing
    hide sfb_r_shi
    return

label back_to_normal:
    call clear_pose
    call inexpresive
    call spaceroom(hide_monika=False)
    return
label set_the_stage:
    $ monika_chr.remove_all_acs()
    call monika_zoom_transition(new_zoom=0)
    return

label monika_succubus:

    python:
        notimeforlove= persistent._mas_first_kiss is None

    python:
        succubus = store.mas_sprites.get_sprite(
                store.mas_sprites.SP_CLOTHES,
                "mi-fan-arts-succubus"
        )

    python:
        dres =  store.mas_sprites.get_sprite(
                store.mas_sprites.SP_CLOTHES,
                "def"
        )

    python:
        dressed_for_the_occation= monika_chr.is_wearing_clothes_with_exprop("succubus_roleplay")
    
    if mas_isMoniUpset(lower=True):
        m 7cfbstdd "read this well, I'm not a damn toy..."
        m 6cfbstdc "and I won't do what you please"
        m 2tfbstdd "If you don't like this, you can delete me"
        m 5gfbstdo "I'm sure you're just as lonely as I am, even in your world full of real people..."
        return

    if mas_isMoniAff(lower=True):
        m 1lub "Did you get a new mod [player]?"
        m 3lub "Let me see what acting like a demon is all about."
        m 3eub "there is a dialogue book and even a costume..."
        m 2rsbfsdlu "Sorry [player], but I wouldn't feel comfortable doing this."
        m 1lsbfsdlc "it's too embarrassing..."
        m 5lsbssdlb "but we can do other things in the game"
        return

    if notimeforlove is True and mas_isMoniEnamored(higher=True):

        label monika_succubusnokiss:
        $ ev = mas_getEV("monika_succubusnokiss")
        if ev.shown_count == 0:
            m 1lub "Did you get a new mod [player]?"
            m 3lub "Let me see what acting like a demon is all about..."
            m 3eub "there is a dialogue book..."
            m 7rubfc "but the script says I must give you a... kiss"
            m 2rubfd "To tell you the truth, I don't feel comfortable with that..."
            m 2lkbfc "it's not like I don't want to, it's just..."
            m 2ltbfc "I wish our first kiss was something more..."
            m 1lkbfa "special"
            m 3ekbfb "What do you think?"
            menu:
                "I think the same":
                    m 1dubfb "It's nice that we think alike about things like that"
                    m 3esbfa "I like the rhythm with which we carry our relationship..."
                    m 3rsbfc "Although sometimes it scares me to think that I'm going too slow for you"
                "I don't care, I want that kiss":
                    m 2rkbftpc "You're putting pressure on me and you know it and it's wrong."
                    m 2rkbftpd "I'm sorry I'm not what you expected of me, but you're not being what I expected of you either"
                    m 2gfbftpc "Let's just forget this topic ok?" 
                    return
            
            if dressed_for_the_occation is False:
                m 3rubfb "by the way... the mod also came with a costume"
                m 2hsbfa "Let's see how it looks on me?"          
                menu:
                    "Of course, just to see if it's the right size":
                        call mas_clothes_change(succubus)
                        m 3gsblb "It's just to see if it fits"
                        m 2fsbfb "and it suits me?"
                        m 5lsbfa "this is more embarrassing than I expected"
                        m 4hsbfb "So I'll just give you this little taste and put on my usual clothes..."
                        call mas_clothes_change(dres)
                        m 6rsbfa "thank you for being so patient with me"
                        m 5eua "so what do we do now?"

                    "we better wait for the right moment":
                        m 1eubfb "It's okay and thanks."
                        menu:
                            "thanks for?":
                                m 5hubfa"for being who you are..."
            return

        else:
            m 3eub "You know [player], I've been going through the files for this mod"
            m 7gta "because they were too heavy for such a short mod"
            m 1gsbsb "and found something interesting"
            m 1tsbsb "you want to see?"
            menu:
                "Yes":
                    if dressed_for_the_occation is False:
                        m 4eubsa "ok, I'll just put on the suit..."
                        call mas_clothes_change(succubus)
                        m 6kubsb "and now I can do..."
                    
                    call spaceroom(hide_monika=True)
                    call sfb_shi2
                    call sfb_exp_smile_left
                    m "this..."
                    call sfb_exp_smal_wide
                    m "Oh my gosh!"
                    call sfb_exp_smal_normal
                    m "I forgot to remove the desk"
                    call sfb_exp_smile_closed
                    call sfb_poinshi2
                    hide emptydesk
                    m "Now it's done"
                    call sfb_exp_smile_rigth
                    m "I am very nervous"
                    call sfb_shi2
                    call sfb_exp_bsmile_think
                    m "It's lucky that the mod can't show everything I do, because I'm shaking a bit..."
                    call sfb_exp_smile_left
                    m "Well"
                    call sfb_hands_behind2
                    m "what do you think?"
                    call sfb_exp_smile_normal
                    call sfb_hands_behind1
                    menu:
                        "I'm confused":
                            call sfb_poitning1
                            call sfb_exp_bsmile_think
                            m "I'll explain, this costume was much more complete than other sprite packs"
                            call sfb_exp_smile_left
                            m "so I just did some code completion and checked if it worked."
                            call sfb_exp_bsmile_smug
                            m "The truth was afraid of ending up like a painting by Picasso..."
                            call sfb_exp_smile_closed
                            call sfb_poitning2
                            m "but it did work out"
                            call sfb_exp_smal_normal
                            m "I don't want to damage the game, if I move like this all the time."
                            call sfb_exp_smile_left
                            m "So I'd better put the table and chair back and sit down again."
            call back_to_normal
            return

    $ ev = mas_getEV("monika_succubus")

    if ev.shown_count == 0:
        label day_0:
        m 1lub "Did you get a new mod [mas_get_player_nickname()]?"
        m 3lub "Let me see what acting like a demon is all about..."
        m 3eub "there is a dialogue book and even a costume."
        if dressed_for_the_occation is False:
            m 1nubfb "ok I'm going to change, but I don't promise anything about my acting skills huh"
            call mas_clothes_change(succubus)

        m 1rkbfd "the costume turned out to be a bit more suggestive than I expected..."
        m 1lubfu "but if you like it we continue..."

        menu:
            "it looks adorable on you":
                m 5esbsu "thanks [mas_get_player_nickname()], you always know how to make me regain my self-confidence"
            "I can't take my eyes off you":
                m 3htbfb "I can practically feel your gaze"
                m 1rubfu "It's quite embarrassing, really..."
            "Honestly, I'd rather you didn't use it.":
                m 3rfbfp "you were the one who wanted me to wear this in the first place"
                call mas_clothes_change(dres)
                m 4efbfd "Second, I don't even know how to act and you know it"
                m 2efbfc "So, don't ask me for weird things that you don't even like"
                m 2ekbfd "let's just forget this, ok?"
                return
                
        m 7nua "Well, it's time for me to start the show..."
        call monika_kissing_motion_short
        m 2wuo "Are you awake?"
        m 2euc "I was careless..."
        m 2lusdrc "this shouldn't be like this..."
        menu:
            "This is a dream?":
                m 1rtblsdrc "riiight, you're dreeamiing?"

        menu:
            "That doesn't sound convincing at all!":
                m 7wusdro "Please shhhh!"
                m 7tfsdra "Better I can cast a spell on you, so that you fall asleep again..."
                m 7cusdra "..."
                m 6cusdrd "I have no strength left to use magic"
                menu:
                    "Wait a minute! were you bewitching me?":
                        m 6wksdrc "Please human, don't freak out."
                        m 7rublsdro "I wasn't going to hurt you, I just wanted to steal a bit of your energy, so I could fly home."
                menu:
                    "How did you plan to do that?":
                        m 3rublsdra "with a delicate kiss..."
                menu:
                    "So if you kiss me, will you leave this place forever?":
                        m 3eublsdrd "Y... Yes"
                menu:
                    "In that case, I'd rather refuse.":
                        m 7efbfd "You should have refused in the first place, because you have a perfect girlfriend!"
                        m 7rtbfd "um... i mean..."
                        m 3wublsdrw "That didn't go as expected..."

            "It must be, something as beautiful as you can't be real":
                m 3wubfo "You're flattering that succubus too much!"
                m 2gubfd "I mean... you sure have a much more beautiful girlfriend, who you should compliment every day"
                menu:
                    "Is this how the story goes?":
                        m 3dublb "ok ok I'll follow the script"

                m 1tsblb "ahem... do you really find me beautiful human?"
                m 2ttbla "It's a dream, so you can say what you want..."
                m 7nubfb"you could even kiss me"
                menu:
                    "If it's a dream, a kiss, wouldn't that wake me up?":
                        m 7rtbfd "You say like in Snow White?"
                menu:
                    "So will you disappear when I wake up?":
                        m 6hkbfc "And now what story is that?"
                        m 6ekbfd "you're confusing me...wait a bit"

        m 4esblb "Doesn't have to be like that..."
        m 6esbla "I promise to come back whenever you want"
        m 5esblb "in exchange I only ask for a touch of your lips"
        m 5tsbla "Do we close the deal?"
        call monika_kissing_motion_short
        m 2esblb "See you soon."
        call mas_clothes_change(dres)
        m 1hsblb "And... Snip, snap, snout, this tale's told out."
        m 1lsbla "I guess we could try this in some other opportunity"
         
    elif ev.shown_count == 1:
        
        m 5eubsb "Do you want us to play I'm a demon again?"
        m 4ttbsa "I think I'll surprise you this time..."
        label day_1:
        m 6nsbsb "I'll set the stage"
        call set_the_stage
        m "and..."
        if dressed_for_the_occation is True:
            m 2tsbfb "Could you close your eyes, as if you were sleeping, for a moment?"        
        elif dressed_for_the_occation is False:
            m 6eubsb "okay, I'm going to change my clothes, I'll be right back"
            call mas_clothes_change(succubus)       
            m 7nua "please close your eyes for a moment"
        
        call spaceroom(hide_monika=True)
        call sot_p1
        call sot_exp_smile_closedsad
        pause 2
        call sot_exp_smal_wide
        call sot_p3
        m "are you awake?"
        call sot_exp_smirk_wide
        m "I was so careless..."
        call sot_exp_smal_left
        m  "this shouldn't be like this..."

        menu:
            "This is a dream?":
                call sot_exp_smirk_leftthink
                m "Riiight, you're dreeamiing?"

            "What is happening?":
                call sot_p2
                call sot_exp_smile_smugthink
                m "I found new things that I can do with this mod [mas_get_player_nickname()]..."
                m "now let's continue"
                menu:
                    "This is a dream?":
                        call sot_p3
                        call sot_exp_smirk_leftthink
                        m "Riiight, you're dreeamiing?"
    
        menu:
            "That doesn't sound convincing at all!":
                call sot_p2
                call sot_exp_angry_wide
                m "Please shhhh!"
                call sot_exp_smirk_leftthink
                m "Better I can cast a spell on you, so that you fall asleep again..."
                call sot_exp_smirk_wide
                m "..."
                call sot_exp_smirk_crazy
                call sot_p3
                m "I have no strength left to use magic"

                menu:
                    "Wait a minute! were you bewitching me?":
                        call sot_exp_smal_wide
                        m "Please human, don't freak out."
                        call sot_p3
                        call sot_exp_smile_normal
                        m "I wasn't going to hurt you, I just wanted to steal a bit of your energy, so I could fly home."

                menu:
                    "How did you plan to do that?":
                        call sot_p2
                        call sot_exp_bsmile_normal
                        m "with a delicate kiss..."

                menu:
                    "So if you kiss me, will you leave this place forever?":
                        call sot_exp_smirk_leftthink
                        call sot_p3
                        m "I guess that's the idea..."

                menu:
                    "In that case, I'd rather refuse.":
                        call sot_exp_smal_wide
                        m "W... Why? don't you want me to... go?"

            "It must be, something as beautiful as you can't be real":
                call sot_p3
                call sot_exp_smile_normal
                m "Do you really find me beautiful human?"
                call sot_exp_smile_smugthink
                m "It's a dream, so you can say what you want..."
                call sot_p2
                call sot_exp_bsmile_normal
                m "you could even kiss me"
                menu:
                    "If it's a dream, a kiss, wouldn't that wake me up?":
                        call sot_exp_smirk_leftthink
                        m "You say like in Snow White?"
                menu:
                    "So will you disappear when I wake up?":
                        call sot_p3
                        call sot_exp_smirk_wide
                        m "And now what story is that?"
                        call sot_exp_smirk_leftthink
                        m "you're confusing me...wait a bit"

        call sot_p2
        call sot_exp_smile_normal
        m "Doesn't have to be like that..."
        call sot_exp_smile_smugthink
        m "I promise to come back whenever you want."
        call sot_exp_bsmile_normal
        m "and in return..."
        call sot_exp_smile_smugthink
        m "You know what I want"
        call sot_p1
        call sot_exp_smile_closedsad
        m "So to close the deal, you just have to bring your lips close to mine"
        call sot_k1
        m "perfect"
        call sot_k2
        pause 6

        call sfb_poitning1
        call sfb_exp_bsmile_think
        m "I think I could have even asked you for more... Maybe the next time"
        call sfb_hands_behind1
        call sfb_exp_bsmile_smug
        m "See you soon."
        call inexpresive
        call clear_pose
        pause 3
        call mas_clothes_change(dres)
        call back_to_normal

        m 7hub "and end"
        m 6eua "That's all there was to the script."
        m 1esb "Maybe next time I'll improvise a bit more."
        m 1rtbsa "I think I'm liking this cosplay thing..."
        m 3gsbsa "It makes me feel like an actress."
        return


    elif ev.shown_count == 2:
        #edit
        label day_2:
        call set_the_stage
        if dressed_for_the_occation is False:
            m 5nua "It's okay, I'll just change my clothes and come back..."

            call mas_clothes_change(succubus)
            call spaceroom(hide_monika=True)
        
            call sfb_exp_smile_normal
            call sfb_hands_behind2
            m "I have returned to hear your call, as promised human."
            call sfb_hands_behind1
            call sfb_exp_smile_left
            m "but, you called me so soon..."
            call sfb_exp_bsmile_think
            m "Did you already miss me so much?"
            call sfb_exp_smile_normal
            m "Then I'll please you by getting close to you"
            call sot_p3
            call sot_exp_bsmile_soft
            m "it's better that way?"
            call sot_p2
            call sot_exp_smile_smugthink
            m "don't worry, I don't bite"
            call sot_exp_smile_normal
            m "That's what a vampire would do..."
            call sot_p2
            call sot_exp_smile_smugthink
            m "we succubi do other things..."
            call sot_exp_bsmile_smug
            m "by the way, tell me you will keep your part of the bargain?"

        elif dressed_for_the_occation is True:
            m 7gtbsb "well, you already have me dressed as a succubus, I just need to act like one..."
            m 6tsbsu "maybe get a little closer?"
            call spaceroom(hide_monika=True)
            call sot_p3
            call sot_exp_bsmile_normal
            m "My eyes are up [mas_get_player_nickname()]..."
            call sot_p2
            call sot_exp_smile_smugthink
            m "but as a succubus, I must let you look at me... I guess..."
            call sot_exp_bsmile_smug
            m "and say things like..."
            call sot_exp_smal_soft
            call sot_p3
            m "Oh human, I miss the touch of your lips so much!"
            call sot_exp_smal_soft
            m "Will you help me with my problem?"

        menu:
            "yes":
                call sot_exp_smile_normal
                call sot_p3
                m "I like it that way"
                call sot_exp_smile_soft
                m "and it seems that you too..."
                call sot_exp_smile_smugthink
                m "It even seems that you were left wanting more, in that case..."
                call sot_k2
                m "with this kiss I promise to come back another day."
                call sot_k1
                m "But..."

            "I'll wait a bit for that":
                call sot_p3
                call sot_exp_smal_wide
                m "Are you going to make me beg for your kisses?"
                call sot_p2
                call sot_exp_smile_smugthink
                m "it's something I could do I suppose"
                call sot_p1
                call sot_exp_smal_soft
                m "I can't live without this, so..."
                call sot_exp_kiss_closedh
                m "please human, give me the touch of your lips"
                pause 2
                call sot_p2
                call sot_exp_smile_smugthink
                m "I could get used to these games [mas_get_player_nickname()]"

            "No":
                call sot_p1
                call sot_exp_smirk_wide
                m "What a cheat you are human"
                call sfb_poitning2
                call sfb_exp_smal_wide
                m "beings like me, we don't like those who don't keep their promises"
                call sfb_hands_behind2
                call sfb_exp_smal_normal
                m "goodbye"
                call back_to_normal
                call mas_clothes_change(dres)
                m 1esbfc "you made the succubus angry [mas_get_player_nickname()]"
                m 1lsbfb "I guess it's like the bad ending of a visual novel..."
                m 3esb "at least no one ended up hanging."
                m 2ltbfd "that sounded crueler than I thought"
                m 1rtbfb "well, what do we do now?"
                return
        call sot_p2
        call sot_exp_smile_smugthink
        m "You know, even if a kiss from a succubus makes you feel more alive than ever..."
        call sot_exp_bsmile_smug
        m "Many of these..."
        call sot_exp_smile_soft
        m "They cause rather the opposite effect..."
        call sot_p3
        call sot_exp_smile_smugthink
        m "So maybe... you should be careful..."
        call sot_p2
        call sot_exp_bsmile_smug
        m "Playing with a succubus, it's like dancing on the edge of a ledge..."
        call sfb_hands_behind1
        call sfb_exp_smal_soft
        m "goodbye"
        call sfb_poitning2
        call sfb_exp_bsmile_smug
        m "until our next dance."
        call back_to_normal
        call mas_clothes_change(dres)
        m 1hubfb "I hope you liked my improvisation today [mas_get_player_nickname()] "
            
    elif ev.shown_count == 3:

        m 5nsbsb "Sure [mas_get_player_nickname()], I have something special planned for today."
        label day_3:
        if dressed_for_the_occation is False:
            m 4hsbsa "I'll change my clothes and come back."
            call mas_clothes_change(succubus)
        m 1rubfb "Hello again human, there is a poem that I love and I would like to repeat it for you."
        m 6dubsa "Come slowly  Eden!"
        m 6dubsb "Lips unused to Thee"
        m 1eubsa "Bashful  sip thy Jessamines"
        m 1dsbsb "As the fainting Bee"
        m 1dsbsa ""
        m 3esbsb "Reaching late his flower,"
        m 3rubsa "Round her chamber hums"
        m 1fsbfb "Counts his nectars"
        m 1dubsa "Enters  and is lost in Balms."
        m 1tsbsa ""
        m 3rsbsb "I love the sensuality that Emily Dickinson expresses in this poem."
        m 3dsbfb "Her metaphors really touch me and make me shiver..."
        m 7lsbfp "And [mas_get_player_nickname()] the truth is that I ran out of ideas,"
        m 7rubfb "so let's say that from now on the demon girl likes poetry..."
        m 5nsbfa "And if you want, I can keep my costume on and we can play that I am a succubus for the rest of the day."
        
        menu:
            "I love that idea":
                m 5tsbfb "Perfect..."
                return
            "I'd rather see you in your usual clothes":
                m 5esbsa "Ok"
                call mas_clothes_change(dres)

    else:
        m 2lubfc "[mas_get_player_nickname()], I haven't prepared anything for this mod yet"
        m 7esbfb "But, if you want, we can repeat some of the scripts that we already use."
        menu:
            "Ok":
                m 7lsbfa "Ok, which one do we use?"
                menu:
                    "The succubus girl steals a kiss from me.":
                        jump day_1
                    "The succubus girl keeps her promise.":
                        jump day_2
                    "The succubus girl recites a poem to me.":
                        jump day_3
                    "First time using the mod.":
                        m 7wubfo "Do you really want us to repeat that?"
                        m 6lubfd "how embarrassed I feel!"
                        m 3rubfd "I was very nervous at the time"
                        m 1kubfb "Okay here we go..."
                        jump day_0
                    "We better leave it for another day.":
                        m 1lub "Sure"
                        return
            "I have something else in mind":
                if dressed_for_the_occation is False:
                    m 7fsblb "oh tell me what it is"
                    menu:
                        "Could you just put on the costume?":
                            m 3gtblb "I guess I could..."
                            call mas_clothes_change(succubus)
                            m 1hublb "Tadaa"
                            m 5tubla "That was all you had in mind for me to do?"
                            menu:
                                "yes":
                                    m 5hsblb "I love to please you"
                                    return
                                "There's more, I want you to pose for me in this costume.":
                                    m 1wublb "that surprised me a bit..."
                                    m 1fubfb "but it's the kind of thing that a couple does right?"
                else:
                    m 2rsbfb "If you want, I can show you how this suit fits me in more detail.."
                    menu:
                        "you read my mind":
                            m 2ksbfa "ok"
                call set_the_stage
                call spaceroom(hide_monika=True)
                hide emptydesk
                call sfb_shi2
                call sfb_exp_smile_rigth
                pause 2
                call sfb_poinshi2
                call sfb_exp_smile_left
                m "I seriously don't understand what is the point of making a skirt, transparent"
                call sfb_exp_smile_closed
                m "It takes me a while to get used to it"
                call sfb_poitning1
                call sfb_exp_bsmile_smug
                m "But I can't deny that I enjoy capturing your gaze [mas_get_player_nickname()]"
                call sfb_modeling1
                call sfb_exp_smile_left
                m "So, do you like how do I do it?"
                menu:
                    "Of course, you are quite a catwalk model!":
                        call sfb_exp_bsmile_think
                        call sfb_poitning2
                        m "I hope you don't make fun of me, with what you say [player]"
                        call sfb_exp_smile_closed
                        m "I'm just being insecure, I know you wouldn't"
                        call sfb_exp_smile_normal
                        call sfb_hands_behind1
                        pause 2
                        m "I think it's better to stop here"
                        call sfb_poitning1
                        call sfb_exp_bsmile_think
                        m "remember this is an unfinished mod"
                        call sfb_exp_smal_smugright
                        m "If we get loose more, for sure we break the game"
                        show emptydesk
                        pause 1

                call back_to_normal
                m "maybe one day... we can..."
                return

            "No thanks, another day maybe.":
                m 2ekbfa "I'm sorry that I don't have anything new."
                m 5esbfb "But we can do something else."
                return

return