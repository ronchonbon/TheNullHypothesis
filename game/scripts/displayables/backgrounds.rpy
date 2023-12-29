init python:
    
    import math

transform invisible:
    alpha 0.0

transform almost_invisible:
    alpha 0.01

transform top_bar:
    subpixel True

    yanchor 1.0
    ypos 0.1

transform bottom_bar:
    subpixel True

    yanchor 0.0
    ypos 1.8

transform rain_splashes:
    subpixel True

    alpha 0.2
    block:
        ease 0.05 alpha 0.7
        ease 0.5 alpha 0.2
        choice:
            pause 0.1
        choice:
            pause 0.25
        choice:
            pause 0.5
        choice:
            pause 0.75
        choice:
            pause 1.0
        repeat

transform move_to_left(t, x):
    subpixel True

    block:
        xoffset 0
        linear t xoffset -x
        repeat

transform move_to_right(t, x):
    subpixel True

    block:
        xoffset -x
        linear t xoffset 0
        repeat

image solid_black:
    Solid("#000000")

image black_fade:
    Solid("#000000")

    on show:
        alpha 0.0
        linear 0.4 alpha 1.0
    on hide:
        linear 0.4 alpha 0.0

    xysize (1.0, 1.0)

image sky:
    contains:
        "sky_temp"

    xysize (int(3840*background_sampling), int(1400*background_sampling))

image steam1:
    contains:
        At("images/effects/steam1.webp", move_to_left(30.0, int(config.screen_width/background_adjustment)))

    xysize (int(3840*background_sampling), int(2160*background_sampling))

image steam2:
    contains:
        At("images/effects/steam2.webp", move_to_right(45.0, int(config.screen_width/background_adjustment)))

    xysize (int(3840*background_sampling), int(2160*background_sampling))

layeredimage sky_temp:
    if time_index == 0:
        "images/backgrounds/base/sky_morning.webp"
    elif time_index == 1:
        "images/backgrounds/base/sky_day.webp"
    elif time_index == 2:
        "images/backgrounds/base/sky_evening.webp"
    elif time_index >= 3:
        "images/backgrounds/base/sky_night.webp"

    if not weather:
        Null()
    elif time_index == 2:
        "images/backgrounds/base/rain_clouds_evening.webp"
    else:
        "images/backgrounds/base/rain_clouds.webp"

    if time_index == 2:
        "images/backgrounds/base/clouds_evening.webp" at move_to_right(220.0, int(config.screen_width/background_adjustment))
    elif weather:
        "images/backgrounds/base/clouds_rain.webp" at move_to_right(220.0, int(config.screen_width/background_adjustment))
    elif time_index >= 3:
        "images/backgrounds/base/clouds_night.webp" at move_to_right(220.0, int(config.screen_width/background_adjustment))
    else:
        "images/backgrounds/base/clouds.webp" at move_to_right(220.0, int(config.screen_width/background_adjustment))

    if weather:
        Null()
    elif time_index == 2:
        "images/backgrounds/base/wind_evening.webp" at move_to_right(180.0, int(config.screen_width/background_adjustment))
    else:
        "images/backgrounds/base/wind.webp" at move_to_right(180.0, int(config.screen_width/background_adjustment))

    if not weather and time_index == 0:
        "images/backgrounds/base/birds.webp" at move_to_left(150.0, int(config.screen_width/background_adjustment))

layeredimage background:
    always:
        "black_fade" at invisible

    if Player.location in bedrooms or Player.location in ["bg_infirmary"]:
        "[Player.location]"
    elif Player.location in ["bg_campus", "bg_pool"]:
        "[Player.location]_background"
            
    if Player.location not in ["bg_classroom", "bg_study"]:
        Null()
    elif time_index <= 3:
        "images/backgrounds/base/[Player.location]_[lighting].webp"
    else:
        "images/backgrounds/base/[Player.location]_night.webp"
            
    if Player.location not in ["bg_mall"]:
        Null()
    elif mall_damage and time_index <= 3:
        "images/backgrounds/base/[Player.location]_destroyed_[lighting].webp"
    elif mall_damage:
        "images/backgrounds/base/[Player.location]_destroyed_night.webp"
    elif time_index <= 3:
        "images/backgrounds/base/[Player.location]_[lighting].webp"
    else:
        "images/backgrounds/base/[Player.location]_night.webp"

    if Player.location not in ["bg_girls_hallway", "bg_hallway"]:
        Null()
    elif time_index < 3:
        "images/backgrounds/base/[Player.location]_day.webp"
    else:
        "images/backgrounds/base/[Player.location]_night.webp"

    if Player.location != "bg_danger":
        Null()
    elif lights_on and danger_red_alert:
        "images/backgrounds/base/bg_danger_red.webp"
    elif danger_red_alert:
        "images/backgrounds/base/bg_danger_dark_red.webp"
    elif not lights_on:
        "images/backgrounds/base/bg_danger_dark.webp"
    else:
        "images/backgrounds/base/bg_danger.webp"
        
    if Player.location != "bg_lockers":
        Null()
    elif Player.behavior == "showering":
        "images/backgrounds/base/bg_lockers_running.webp"
    else:
        "images/backgrounds/base/bg_lockers.webp"
        
    if Player.location not in ["bg_shower_Player", "bg_shower_Rogue", "bg_shower_Laura", "bg_shower_Jean"]:
        Null()
    elif Player.behavior == "showering":
        "images/backgrounds/base/bg_shower_running.webp"
    else:
        "images/backgrounds/base/bg_shower.webp"

    if Player.location in ["bg_movies", "bg_restaurant", "bg_town"]:
        "images/backgrounds/base/[Player.location].webp"

    if Player.location == "bg_danger" and lights_on:
        "bg_danger_lights" at danger_room_pulsing

    if Player.location in ["traveling", "bg_door", "bg_restaurant_bathroom"]:
        "black_fade"

    transform_anchor True
    align (0.5, 0.5)

    zoom background_adjustment

layeredimage midground:
    always:
        "black_fade" at invisible

    if Player.location != "bg_classroom":
        Null()
    elif time_index <= 3:
        "images/backgrounds/base/bg_classroom_podium_[lighting].webp"
    else:
        "images/backgrounds/base/bg_classroom_podium_night.webp"

    if Player.location == "bg_mall" and time_index < 3:
        "images/backgrounds/base/bg_mall_people_[lighting].webp"

    if Action_screen_showing:
        "background" at blurred_background, Transform(zoom = 1.0/background_adjustment)

    if Player.location in ["bg_lockers", "bg_shower_Player", "bg_shower_Rogue", "bg_shower_Laura", "bg_shower_Jean"] and shower_steam:
        "steam2" at fade_in(2.0)
        
    transform_anchor True
    align (0.5, 1.0)

    zoom background_adjustment

layeredimage foreground:
    always:
        "black_fade" at invisible

    if Player.location != "bg_classroom":
        Null()
    elif time_index <= 3:
        "images/backgrounds/base/bg_classroom_background_[lighting].webp"
    else:
        "images/backgrounds/base/bg_classroom_background_night.webp"
            
    if Player.location == "bg_classroom" and time_index < 2 and weekday < 5 and clock >= math.ceil(0.1*Player.max_stamina):
        "images/backgrounds/base/bg_classroom_students.webp"

    if Player.location == "bg_restaurant" and eating_dinner:
        "images/backgrounds/base/bg_restaurant_chair.webp"

    if Player.location != "bg_study":
        Null()
    elif time_index <= 3:
        "images/backgrounds/base/bg_study_desk_[lighting].webp"
    else:
        "images/backgrounds/base/bg_study_desk_night.webp"

    transform_anchor True
    align (0.5, 0.5)

    zoom background_adjustment

layeredimage cover1:
    always:
        "black_fade" at invisible

    if Player.location in ["bg_campus", "bg_pool"]:
        "[Player.location]_cover"

    if Player.location != "bg_classroom":
        Null()
    elif time_index <= 3:
        "images/backgrounds/base/bg_classroom_foreground_[lighting].webp"
    else:
        "images/backgrounds/base/bg_classroom_foreground_night.webp"
        
    if Player.location in ["bg_lockers", "bg_shower_Player", "bg_shower_Rogue", "bg_shower_Laura", "bg_shower_Jean"] and shower_steam:
        "steam1" at Transform(alpha = 0.8), fade_in(2.0)
    elif Player.location == "bg_restaurant" and eating_dinner:
        "bg_restaurant_table"

    transform_anchor True
    align (0.5, 1.0)

    zoom background_adjustment

layeredimage cover2:
    always:
        "black_fade" at invisible

    if "bg_shower" not in Player.location:
        Null()
    elif shower_open:
        "images/backgrounds/base/bg_shower_doors_open.webp"
    else:
        "images/backgrounds/base/bg_shower_doors_closed.webp"

    transform_anchor True
    align (0.5, 0.5)

    zoom background_adjustment

layeredimage top_bar:
    always:
        "black_fade" at invisible

    if cinematic_bars and (ongoing_Event or not sandbox):
        "black_fade" at top_bar, fade_in(0.4)
    elif cinematic_bars:
        "black_fade" at top_bar, fade_out(0.4)

    transform_anchor True
    align (0.5, 0.5)

layeredimage bottom_bar:
    always:
        "black_fade" at invisible

    if cinematic_bars and (ongoing_Event or not sandbox):
        "black_fade" at bottom_bar, fade_in(0.4)
    elif cinematic_bars:
        "black_fade" at bottom_bar, fade_out(0.4)

    transform_anchor True
    align (0.5, 0.5)
        
layeredimage black_screen:
    always:
        "black_fade" at invisible

    if black_screen:
        "black_fade" at fade_in(0.4)
    else:
        "black_fade" at fade_out(0.4)

    transform_anchor True
    align (0.5, 0.5)

layeredimage filter:
    always:
        "black_fade" at invisible

    if image_filter:
        "images/interface/preferences/[image_filter].webp"

    if Player.desire >= 90:
        "images/interface/Action_menu/climax_fringe.webp" at pulse(intensity = 1.0)
    elif Player.desire >= 80:
        "images/interface/Action_menu/climax_fringe.webp" at pulse(intensity = 0.8)
    elif Player.desire >= 70:
        "images/interface/Action_menu/climax_fringe.webp" at pulse(intensity = 0.6)
    elif Player.desire >= 60:
        "images/interface/Action_menu/climax_fringe.webp" at pulse(intensity = 0.4)
    elif Player.desire >= 50:
        "images/interface/Action_menu/climax_fringe.webp" at pulse(intensity = 0.2)

    if Player.power >= 100:
        "images/interface/Player_power/power_white.webp" at pulse(intensity = 1.0, frequency = 2.0)
    elif Player.power >= 75:
        "images/interface/Player_power/power_white.webp" at pulse(intensity = 0.75, frequency = 1.5)
    elif Player.power >= 50:
        "images/interface/Player_power/power_white.webp" at pulse(intensity = 0.5)
    elif Player.power > 25:
        "images/interface/Player_power/power_white.webp" at pulse(intensity = 0.25)

    if Player.power >= 100:
        "images/interface/Player_power/veins_black.webp" at pulse(intensity = 1.0, frequency = 2.0)
    elif Player.power >= 75:
        "images/interface/Player_power/veins_black.webp" at pulse(intensity = 0.75, frequency = 1.5)
    elif Player.power >= 50:
        "images/interface/Player_power/veins_black.webp" at pulse(intensity = 0.5)
    elif Player.power > 25:
        "images/interface/Player_power/veins_black.webp" at pulse(intensity = 0.25)

    transform_anchor True
    align (0.5, 0.5)

    zoom background_adjustment

image comic_cutout1 = Window(Layer("comic_cutout1"), background = "#000000", padding = (10, 10, 10, 10))

image comic_cutout2 = Window(Layer("comic_cutout2"), background = "#000000", padding = (10, 10, 10, 10))

image comic_cutout3 = Window(Layer("comic_cutout3"), background = "#000000", padding = (10, 10, 10, 10))

image comic_cutout4 = Window(Layer("comic_cutout4"), background = "#000000", padding = (10, 10, 10, 10))