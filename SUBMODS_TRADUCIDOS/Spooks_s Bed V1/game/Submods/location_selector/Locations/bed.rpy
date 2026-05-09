init 1 python in mas_background:

    # verify all backgrounds
    for flt_bg in BACKGROUND_MAP.itervalues():
        flt_bg.verify()

###START: IMAGE DEFINITIONS
#Day images
image submod_bed_day = "mod_assets/location/bed/bed.png"
image submod_bed_rain = "mod_assets/location/bed/bed_rain.png"
image submod_bed_overcast = "mod_assets/location/bed/bed_overcast.png"
image submod_bed_snow = "mod_assets/location/bed/bed_snow.png"

#Night images
image submod_bed_night = "mod_assets/location/bed/bed-n.png"
image submod_bed_rain_night = "mod_assets/location/bed/bed_rain-n.png"
image submod_bed_overcast_night = "mod_assets/location/bed/bed_overcast-n.png"
image submod_bed_snow_night = "mod_assets/location/bed/bed_snow-n.png"

#Sunset images
image submod_bed_ss = "mod_assets/location/bed/bed-ss.png"
image submod_bed_rain_ss = "mod_assets/location/bed/bed_rain-ss.png"
image submod_bed_overcast_ss = "mod_assets/location/bed/bed_overcast-ss.png"
image submod_bed_snow_ss = "mod_assets/location/bed/bed_snow-ss.png"



init -1 python:
    submod_background_bed = MASFilterableBackground(
        # ID
        "submod_bed",
        "Bed",

        # mapping of filters to MASWeatherMaps
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_bed_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_bed_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_bed_overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_bed_snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_bed_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_bed_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_bed_overcast_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_bed_snow_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_bed_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_bed_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_bed_overcast_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_bed_snow_ss",
            }),
        ),

        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),

        disable_progressive=False,
        hide_masks=False,
        hide_calendar=True,
        unlocked=True,
        entry_pp=store.mas_background._bed_entry,
        exit_pp=store.mas_background._bed_exit,
        ex_props={"skip_outro": None}
    ) 


init -2 python in mas_background:
    def _bed_entry(_old, **kwargs):
        """
        Entry programming point for Furnished_spaceroom3 background
        """
        if kwargs.get("startup"):
            pass

        else:
            if not store.mas_inEVL("bed_switch_dlg"):
                store.pushEvent("bed_switch_dlg")

        store.monika_chr.tablechair.table = "BE"
        store.monika_chr.tablechair.chair = "BE"

        if store.seen_event("mas_monika_islands"):
            store.mas_unlockEVL("mas_monika_islands", "EVE")

    def _bed_exit(_new, **kwargs):
        """
        Exit programming point for Furnished_spaceroom3 background
        """
        #Lock islands greet to be sure
        store.mas_lockEVL("mas_monika_islands", "EVE")

        #COMMENT(#) IF NOT NEEDED
        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

        if _new == store.mas_background_def:
            store.pushEvent("return_switch_dlg")       

###START: Topics
label bed_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "Ahhh, qué acogedor.",
            "¡Qué cama tan cómoda!",
            "Agradable y acogedor...",
        ]))

    m 1hua "[switch_quip]"

    return

label return_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "Solo nosotros dos~",
            "¿Extrañas el look clásico?",
            "Me trae recuerdos...",
        ]))

    m 1hua "[switch_quip]"

    return