init -1 python:
    mas_background_submod_minecraft = MASBackground(
            "submod_minecraft",
            "Habitación de Minecraft",
            "submod_minecraft",
            "submod_minecraft_n",
            image_rain_day="submod_minecraft_rain",
            image_rain_night=None,
            image_overcast_day=None,
            image_overcast_night=None,
            image_snow_day="submod_minecraft_snow",
            image_snow_night=None,
            hide_calendar=True,
            hide_masks=False,
            disable_progressive=False,
            unlocked=True,
        )

image submod_minecraft = "mod_assets/location/minecraft/minecraft.png"
image submod_minecraft_n = "mod_assets/location/minecraft/minecraft-n.png"
image submod_minecraft_rain_day = "mod_assets/location/minecraft/minecraft_rain.png"
image submod_minecraft_snow_day = "mod_assets/location/minecraft/minecraft_snow.png"
