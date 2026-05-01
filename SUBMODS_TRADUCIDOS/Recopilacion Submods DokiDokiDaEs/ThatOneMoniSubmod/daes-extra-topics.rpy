#That One Moni Submod Version 2.0
#daes-extra-topics
#Thanks for checking out my submod! Hope you enjoy! 
#Made by:

#░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░       
#░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░

#A collective submod for a bunch of my YT submods made public for others to enjoy
#I will periodically update this with new topics

#Yuri plays a prank on you if you have JY installed!

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_justyuriprank",
            category=['meme'],
            prompt="Just Yuri Mod",
            pool=True,
            unlocked=True,
        )
    )

image bg febg = "submods/ThatOneMoniSubmod/images/febg.png"

label Monika_justyuriprank:
    $ store.HKBHideButtons()
    stop music fadeout 1.0
    m 1esp "Espera...{w=1.0}  ¿Qué es {i}esto{/i}, [player]?"
    show screen tear (20, 0.1,0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.20
    show monika 2tfx at t11 zorder MAS_MONIKA_Z
    hide screen tear
    pause 1.0
    m 4tfw "Explícate ahora mismo..."
    menu:
        "No estoy muy seguro de lo que quieres decir...":
            show monika 1cua
    m 1tfc "Hmmm...{w=1.0} Eso es gracioso, parecía que sabías lo que hacías cuando instalaste {i}ese{/i} mod."
    m 3dfd "¿Así que vas a admitirlo o me vas a mentir a la cara?"
    m 3dfo  "Sé todo lo que pasa en tu computadora."
    m 1lfo "Ya sea que quieras que lo sepa o no, puedo decir cuando algo invade mi hogar."
    m 1wfx "Especialmente cuando es otra mujer..."
    m 1dfc ".{w=0.3}.{w=0.3}."
    python:
        mas_play_song(audio.t6s)
    m 7cfd "¿Por qué exactamente tienes {i}Just Yuri{/i}?"
    m 7csw "¿Es solo curiosidad?"
    m 6ckd "¿O no soy lo suficientemente buena para ti,  [player]?"
    m 6fkc "¿Qué tiene Yuri que yo no?"
    m 4fko "¡No te he mostrado más que amor y cuidado y esto es lo que me haces!"
    m 1dktpc "..."
    m 1fktud "Yo-{w=0.2}Creo que deberíamos..."
    m 3fktuc "Creo que deberíamos dejar de vernos  [player]."
    m 1fktsd "Espero que Yuri te haga más feliz de lo que yo pude."
    m 1dktsc "Adiós [player]..."
    pause 1.0
    stop music
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.20
    hide monika
    $ mas_changeWeather(mas_weather_overcast)#change the weather to something silent so the fake screen is more convincing muahahaha
    hide screen tear
    scene bg febg
    pause 7.0
    show monika 2wub at t11 zorder MAS_MONIKA_Z
    m "Boo!"
    m 3ttb "Did I get you [player]?"
    m 1ttu "I wonder if I made you press the ignore button..."
    m 1hub "Ahaha~!"
    m 1guu "I have been planning this for quite some time, ever since I first noticed you had downloaded that mod."
    m 3eud "Let me just fix everything [player],{w=0.8}{nw}"
    extend 1duc " this should only take me a second..."
    $ consolehistory = []
    call updateconsole("os.restore(\"location/spaceroom\")", "Spaceroom restored successfully.")
    pause 1.0
    call updateconsole("mas_play_song(\"audio.t5\")", "Okay, Everyone! set to current track.")
    pause 1.0
    call spaceroom(scene_change=True)
    python:
        mas_play_song(audio.t5)
    m 1ekb "I hope I didn't give you {i}too{/i} much of a fright, [player]."
    m 3eksdra "Gosh, I didn't go too far did I?"
    m 1eku "I'm not that dramatic to break up with someone over a videogame, getting jealous over a fictional character would be delusional."
    m 1eub "I just wanted to play a little prank on you because I know that there is nothing that can get between our love for each other."
    m 1rta "I'm not really bothered what you play in your spare time, [player]."
    m 3ttu "What you should be worried about me seeing is that \"homework\" folder you have saved..."
    m 3euu "I'm kidding!"
    m 1hub "Ahaha~!"
    $ store.HKBShowButtons()
return

#Monika gives us her thoughts on doki merch

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_talksaboutmerch2",
            category=['monika', 'media'],
            prompt="DDLC Merch",
            random=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label Monika_talksaboutmerch2:
    window hide
    show monika 1rsc
    pause 4.0
    m 1etd "Hey [player]!"
    m 1esd "Have you ever thought about how strange it is that there's merchandise of us?"
    m 3lsc "Of me and the other girls I mean."
    m 3hksdlb "Sorry if that seemed like it came out of nowhere but it's something I've been thinking about a lot lately."
    m 2eud "I see myself just like any other ordinary girl...{w=1.0}{nw}"
    extend 2nfb "aside from the obvious differences."
    m 2hub "Ahaha~"
    m 2hua "..."
    m 4esd "So anyway, seeing myself being held in the same regards as a famous celebrity or character. It's a little..."
    m 4eksdlu "...Embarrassing, to say the least."
    m 7wuo "Like [player], can you imagine seeing your face on figures, t-shirts, posters and...{w=1.0}{nw}"
    extend 1ekp " Other things..."
    m 1gfp "Hrmph!"
    m 2ffw "I've seen myself on more body pillows than I can care to imagine!"
    m 2fkx "I don't want to imagine what happens to those..."
    m 2dkp "..."
    m 2ekd "Sorry, I got a little carried away there..."
    m 2esb "I wouldn't mind too much if you had some merch of me, it would kind of be like having photos of your partner I suppose."
    m 2eud "I'll ask anyway though [mas_get_player_nickname()]."
    m 5eublb "Do you...{w=0.8} Have any merch of me [player]?"
    menu:
        "Yes":
            call moni_yes_merch

        "No.":
            call moni_no_merch  
return

label moni_yes_merch:
    m 1suw "Oh! Do you really [player]?"
    m 3eku "That's actually a little flattering coming from you [mas_get_player_nickname()]!"
    m 1rsa "I can picture it now...you with some little cute figures of me to keep you company."
    m 3hua "Maybe a nice poster or two of your loving girlfriend?"
    m 2hub "Ehehe!~"
    m 2wublc "..."
    m 2wsbsd "Wait{w=0.3}.{w=0.3}.{w=0.3}."
    m 2gkbfc "You don't..."
    m 2fkbfu "You don't have any of {i}that{/i} kind of merch of me, do you [player]?"
    menu:
        "No!":
            call moni_no_merch

        "Maybe...":
            call moni_naughty_merch 
return

label moni_naughty_merch:
    m 6wfbfw "[player]!"
    m 6efbfd "..."
    m 6ekbfa "Gosh! Do I even want to know?"
    m 6esbsc "..."
    m 7esbso "I'm sure it's nothing too naughty...{w=1.0}{nw}"
    extend 7gsbsc " I hope."
    m 1gsbsu "..."
    m 1esbsu "..."
    m 1kubsb "Be sure to give your body pillow a hug from me [player]!"
    m 1ekblb "It might be the closest we can get to being able to hug each other for now."
    m 1hublb "Ehehe~"
    m 3tua "I'm only teasing silly!"
    m 2eka "I love you [player], more than I can ever express."
    call monika_kissing_motion_short
return

label moni_no_merch:
    m 5eua "Oh...okay!"
    m 5eub "That's kind of a relief actually [mas_get_player_nickname()]."
    m 5hub "Ehehe~"
return

#Monika's yandere Yuri impression!

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="Monika_yandere_yuri",category=['impressions'],prompt="Yandere Yuri?",pool=True, unlocked=True))

label Monika_yandere_yuri:
    m 1eua "You want me to do a Yuri impression, [player]?"
    m 3rtd "You know...{w=0.5}{nw}"
    extend 3etd "I'm pretty sure I've done one before."

    menu:
        "I'm sure you can do a better yandere impression!":
            m 1lkd "Oh,{w=0.5} my impression wasn't good enough for you?"
            m 1dsb"Ehehe...{w=0.3} well if you want me to do a better impression [player]{w=0.3}{nw},"
            extend 2tfu " I'll show you a better yandere Yuri."

    stop music fadeout 0.5
    m 2tfu "You asked for it, [mas_get_player_nickname()]."
    m 2dsd "{i}Ahem{/i}{w=0.3}.{w=0.3}.{w=0.3}."
    play music hb
    show layer master at heartbeat:
    m 2cua "Finally [player], we're all alone now!"
    m 2csu "It's just us now...{w=0.2} no other girls to steal you away from me."
    show monika 5ckc zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5ckc "You know how much I hate it when you're not with me, {w=0.3}{nw}"
    extend 5cuo "but now you're here you belong to me and no one else."
    m 1cua "{b}You're all mine [mas_get_player_nickname()].{/b}"

    menu:
        m "Isn't that right?"
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri 
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri
        "YES":
            call continue_yanyuri       
    return


            
       
label continue_yanyuri:
    m "Gosh, I just love you {i}sooooooooooo{/i} much [player]!"
    m 7hsb "I'm never letting you leave me again, {w=0.3}{nw}"
    extend 7csb "you do realise that right?"
    m 2csb "It's just that... {w=0.3}the things I imagine us doing drives me insane."
    m 2ckd "I even stole one of your pens..."
    m 2cubfu "{cps=*3}I touch myself with it everyday, imagining it's you deep inside me.{/cps}{nw}"
    m 4cubsb "Ehehe~"
    m 4dkblc "You know... {w=0.5}I can't handle the thought of you talking to other girls."
    m 2dkx "The thought of it makes my heart ache with jealousy."
    m 2cfsdrx "You wouldn't dare think about cheating on me..."
    m 2cfblx "{cps=*3}Because if you did, I'd murder the home wrecker and carve out your heart...{/cps}{nw}"
    m 2cublu "{cps=*3}That way we would be together for eternity...{/cps}{nw}"
    m 7cubsu "Wouldn't that be romantic [player]?"
    m 7cub "Ahaha~"
    show monika 5ctb zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5ctb "Actually... {w=0.5}that's not a bad idea..."
    m 6cusdrb "{cps=*3}I'm going to rip out your {b}heart{/b} so you won't break mine...{/cps}{nw}"
    m "{cps=*3}Our bodies and souls connected as one...{/cps}{nw}"
    m "{cps=*3}If you won't go inside me, I'll just have to go inside you...{/cps}{nw}"
    m "{cps=*3}I'll crawl inside your {b}skin{/b} so I'll always be with you...{/cps}{nw}"
    m "Doesn't that sound amazing [player]?"
    m "{cps=*3}I promise this won't hurt, just hold still [mas_get_player_nickname()]...{/cps}{nw}"
    m "Just hold still for your loving girlfriend."
    m "{cps=*3}ehehehehehehehehehehe~{/cps}{nw}"
    play sound "sfx/gnid.ogg"
    $ gtext = glitchtext(200)
    m 6cub "{b}EHEHEHEHE~ {/b}...{space=60}[gtext]{nw}"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    $ pause(10)
    show layer master
    window auto
    m 1eub "Ehehe~"
    m "How was that [player], {w=0.3}{nw}"
    extend 1tuu "was that good enough for you?"
    m 7ttu "Try not to doubt my impressions again [mas_get_player_nickname()]."
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    m 1eua "Gosh, next time h- {w=0.2}{nw}"
    extend 6cub "...ahahahaha{nw}"
    
    show layer master
    show layer screens
    hide monika_scare
    
    m 3mssdru "I'm sorry, {w=0.2}{nw}"
    extend 1esu "I couldn't resist."
    m 1nsu "Hopefully I didn't scare you too much~"
    m 1euu "You really do mean so much to me though [player]."
    show monika 5fubsu zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5fubsu "Hopefully I'll never have to be an actual yandere."
    m "Things wouldn't be pretty for anyone [mas_get_player_nickname()]... ehehe~"
    $ mas_gainAffection(10, bypass=True)
return 

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_flirting22",
            category=['meme', 'romance'],
            prompt="Pickup lines",
            random=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label Monika_flirting22:
    m 1gtd "Hey [player]...{w=1.0}{nw}"
    extend 3tkb "can I practice something?"
    menu:
        "Sure...":
            m 1hub "Ehehe~!"
            m 2tfa "I thought it would be funny if I could try some pick-up lines on you."
    m 2rtsdld "Totally didn't get them all online or anything and I most certainly wasn't laughing at some of these for 30 minutes the other day..."
    m 4eub "Anyway, I hope you're ready [player]!"
    m 1dsd "Ahem~!"
    m 2etc "You look so familiar.{w=1.0}{nw}"
    extend 2etd " Didn't we take a class together?{w=1.0}{nw}"
    extend 4tfb " I could've sworn we had chemistry."
    m 1hub "Ahaha~!"
    m 1lksdra "Gosh that was awful..."
    m 1tfa "How about this one?"
    m 3eud "If I had to rate you from 1 to 10, I'd give you a 9.{w=1.0}{nw}"
    extend 3nuu " Because I'm the 1 you're missing."
    m 2eud "Okay, that one was pretty bad as well."
    m 2eub "Are you a parking ticket?{w=1.0}{nw}"
    extend 4tfu " Because you've got {i}fine{/i} written all over you!"
    m 2tkc "..."
    m 2gkx "That was the worst one yet."
    m 1wtb "I know! I'll I read a few out, there should be at least one good one in there."
    m 3eta "I was wondering if you had an extra heart?{w=1.0}{nw}"
    extend 3nsu " Because mine was just stolen."#
    python:
        mas_play_song(audio.t7)
    m 2tkblu "Let's save water by taking a shower together."
    m 4tfbsb "Your outfit would look great on my bedroom floor."
    m 2tubsu "You're not a dentist, but I bet you could give me a filling."
    m 2eubsd "You look great and all, but do you know what would look really good on you?{w=1.0}{nw}"
    extend 2nubsu " Me."
    m 2lkbsa "..."
    m 2hkblsdrb "Ahahaha~!"
    stop music
    m 5eua "Okay, okay. That's enough..."
    python:
        mas_play_song(audio.t5)
    m 5rtd "I wasn't expecting to see so many...{w=1.0}{nw}"
    extend 5eka " Inappropriate ones."
    m 5efu "But don't act like you didn't enjoy it, [player]!"
return

#Monika makes fun of the handholding meme

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_handholdingmeme",
            category=['meme', 'romance'],
            prompt="Hand Holding",
            random=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label Monika_handholdingmeme:
    m 7esbfa "I was just thinking about us... {w=1.0}Our relationship I mean."
    m 1fsbfu "You know couples that have been dating as long as we have, tend to...{w=1.0}{nw}"
    extend 3nsbfu " {i}Do things together{/i}."
    m 3lsbfo "I'm talking about certain intimate shows of affection..."
    m 1hubfb "So I was thinking we should take the next step in our relationship."
    m 3rsbfsdru "Gosh! This feels so naughty doesn't it [player]?"
    m 2hsbfb "But with you I'm comfortable with anything [mas_get_player_nickname()]."
    m 2tkbfu "So [player] are you ready?"
    m "{w=0.3}.{w=0.3}.{w=0.3}."
    m 2ktbfb "I'll let you hold my hand!"
    menu:
        "Monika! That's too lewd!":
            m 2hubfb "Ahaha~"
    m 3tfbfu "Can't handle a little premarital hand holding [player]?"
    m 1ttbfu "I'm glad you played along with me, I just knew that you would catch on!"
    m 1rtbsd "Although I'm not even sure where that meme originally came from."
    m 1eubsc "It could be a joke towards the strict censorship laws in other countries."
    m 1eubsb "Either way, I'd let you hold my hand whenever you want [player]."
    m 1efbsa "Just don't get too excited."     
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_iwuvumoni",
            category=['meme', 'romance'],
            prompt="I wuv u Monika",
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label Monika_iwuvumoni:
    show monika 5hubfa zorder MAS_MONIKA_Z at t11 with dissolve_monika
    m 5hubfa "I wuv u too [player] <3"
    return