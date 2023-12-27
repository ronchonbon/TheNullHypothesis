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

layeredimage bg_Player:
    if lighting == "evening":
        "images/backgrounds/base/bg_Player_day.webp"
    else:
        "images/backgrounds/base/bg_Player_[lighting].webp"
        
    if "acoustic_panels" in Player.inventory.keys() and Player.inventory["acoustic_panels"][0].Owner == Player:
        "images/backgrounds/base/bg_Player_acoustic_panels.webp"
        
    if "motorcycle_helmet" in Player.inventory.keys() and Player.inventory["motorcycle_helmet"][0].Owner == Player:
        "images/backgrounds/base/bg_Player_helmet.webp"
        
    if "sound_system" in Player.inventory.keys() and Player.inventory["sound_system"][0].Owner == Player:
        "images/backgrounds/base/bg_Player_sound_system.webp"
        
    if "electric_guitar" in Player.inventory.keys() and Player.inventory["electric_guitar"][0].Owner == Player:
        "images/backgrounds/base/bg_Player_guitar.webp"

    if Player.messy_bed:
        "images/backgrounds/base/bg_Player_messy_bed.webp"
    else:
        "images/backgrounds/base/bg_Player_bed.webp"
        
    if "record_player" in Player.inventory.keys() and Player.inventory["record_player"][0].Owner == Player:
        "images/backgrounds/base/bg_Player_record_player.webp"

    if Player.clothes_on_floor:
        "images/backgrounds/base/bg_Player_clothes.webp"

    if lighting == "evening":
        "images/backgrounds/base/bg_Player_day_hard_light.webp" at Transform(blend = "multiply")
    else:
        "images/backgrounds/base/bg_Player_[lighting]_hard_light.webp" at Transform(blend = "multiply")

    if lighting in ["day"]:
        "images/backgrounds/base/bg_Player_[lighting]_screen.webp" at Transform(blend = "screen")

    if lighting == "evening":
        "images/backgrounds/base/bg_Player_day_linear_dodge.webp" at Transform(blend = "add")
    else:
        "images/backgrounds/base/bg_Player_[lighting]_linear_dodge.webp" at Transform(blend = "add")

    if lighting == "evening":
        "images/backgrounds/base/bg_Player_day_multiply.webp" at Transform(blend = "multiply")
    else:
        "images/backgrounds/base/bg_Player_[lighting]_multiply.webp" at Transform(blend = "multiply")

layeredimage bg_campus_background:
    if time_index == 0:
        "images/backgrounds/base/bg_campus_sky_morning.webp"
    elif time_index == 1:
        "images/backgrounds/base/bg_campus_sky_day.webp"
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_sky_evening.webp"
    elif time_index >= 3:
        "images/backgrounds/base/bg_campus_sky_night.webp"

    if not weather:
        Null()
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_rain_clouds_evening.webp"
    else:
        "images/backgrounds/base/bg_campus_rain_clouds.webp"

    always:
        "sky"

    if time_index == 2:
        "images/backgrounds/base/bg_campus_mansion_evening.webp"
    else:
        "images/backgrounds/base/bg_campus_mansion.webp"

    if campus_grass_cut:
        "images/backgrounds/base/bg_campus_grass.webp"
    else:
        "images/backgrounds/base/bg_campus_grass_uncut.webp"

    if not weather:
        "images/backgrounds/base/bg_campus_lighting.webp"

    if not weather:
        "images/backgrounds/base/bg_campus_lighting_linear_dodge.webp" at Transform(blend = "add")

    if weather == "snow" or snow_left:
        "images/backgrounds/base/bg_campus_snow.webp"

    if weather == "rain":
        "images/backgrounds/base/bg_campus_puddles_linear_dodge.webp" at Transform(blend = "add")
    elif weather == "snow":
        "images/backgrounds/base/bg_campus_steam_linear_dodge.webp" at Transform(blend = "add")

    if weather == "rain":
        "images/backgrounds/base/bg_campus_puddles.webp"
    elif weather == "snow":
        "images/backgrounds/base/bg_campus_steam.webp"

    if time_index >= 3:
        "images/backgrounds/base/bg_campus_night_hard_light.webp" at Transform(blend = "multiply")
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_evening_hard_light.webp" at Transform(blend = "multiply")

    if time_index >= 3:
        "images/backgrounds/base/bg_campus_night_color_dodge.webp" at Transform(blend = "multiply")
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_evening_color_dodge.webp" at Transform(blend = "add")

    if time_index in [0]:
        "images/backgrounds/base/bg_campus_morning_mist.webp"

    if time_index >= 3:
        "images/backgrounds/base/bg_campus_night_linear_dodge.webp" at Transform(blend = "add")
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_evening_linear_dodge.webp" at Transform(blend = "add")
    elif time_index == 0:
        "images/backgrounds/base/bg_campus_morning_linear_dodge.webp" at Transform(blend = "add")

    if weather == "rain":
        "images/backgrounds/base/bg_campus_rain_splashes.webp" at rain_splashes

layeredimage bg_campus_cover:
    if time_index >= 3:
        "images/backgrounds/base/bg_campus_left_tree_night.webp"
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_left_tree_evening.webp"
    else:
        "images/backgrounds/base/bg_campus_left_tree.webp"

    if time_index >= 3:
        "images/backgrounds/base/bg_campus_right_tree_night.webp"
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_right_tree_evening.webp"
    else:
        "images/backgrounds/base/bg_campus_right_tree.webp"

    if weather != "rain":
        Null()
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_rain_evening.webp"
    else:
        "images/backgrounds/base/bg_campus_rain.webp"

    if weather != "snow":
        Null()
    elif time_index >= 3:
        "images/backgrounds/base/bg_campus_snowstorm_night.webp"
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_snowstorm_evening.webp"
    else:
        "images/backgrounds/base/bg_campus_snowstorm.webp"

    if weather == "snow" and time_index in [0, 1]:
        "images/backgrounds/base/bg_campus_snowstorm_linear_dodge.webp" at Transform(blend = "add")

layeredimage bg_danger_lights:
    if danger_red_alert:
        "images/backgrounds/base/bg_danger_lights_red.webp"
    else:
        "images/backgrounds/base/bg_danger_lights.webp"

layeredimage bg_infirmary:
    if time_index >= 3:
        "images/backgrounds/base/bg_infirmary_dark.webp"
    else:
        "images/backgrounds/base/bg_infirmary.webp"

    if infirmary_in_bed:
        "images/backgrounds/base/bg_infirmary_bed.webp"
    elif infirmary_bed:
        "images/backgrounds/base/bg_infirmary_bed_empty.webp"
    
    if infirmary_in_bed:
        "images/backgrounds/base/bg_infirmary_screenlight.webp"

    if infirmary_screen1:
        "images/backgrounds/base/bg_infirmary_screens1.webp"

    if infirmary_screen2:
        "images/backgrounds/base/bg_infirmary_screens2.webp"

    if infirmary_screen3:
        "images/backgrounds/base/bg_infirmary_screens3.webp"

    if time_index >= 3:
        "images/backgrounds/base/bg_infirmary_night_hard_light.webp" at Transform(blend = "multiply")

    if time_index >= 3:
        "images/backgrounds/base/bg_infirmary_night_linear_dodge.webp" at Transform(blend = "add")

layeredimage bg_restaurant_table:
    always:
        "images/backgrounds/base/bg_restaurant_table.webp"

    if food_arrived:
        "images/backgrounds/base/bg_restaurant_Player_plate.webp"

    if drinking_wine:
        "images/backgrounds/base/bg_restaurant_glass.webp"

    if not ordered_food:
        "images/backgrounds/base/bg_restaurant_menu.webp"

    if drinking_wine:
        "images/backgrounds/base/bg_restaurant_bottle.webp"

    if food_arrived:
        "images/backgrounds/base/bg_restaurant_Character_plate.webp"

    always:
        "images/backgrounds/base/bg_restaurant_shakers.webp"

layeredimage background:
    always:
        "black_fade" at invisible

    if Player.location in bedrooms or Player.location in ["bg_infirmary"]:
        "[Player.location]"
    elif Player.location == "bg_campus":
        "bg_campus_background"

    if Player.location not in ["bg_pool"]:
        Null()
    elif weather:
        "images/backgrounds/base/[Player.location]_[time_index]_[weather].webp"
    else:
        "images/backgrounds/base/[Player.location]_[time_index].webp"
            
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

    if Player.location == "bg_campus":
        "bg_campus_cover"

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

    if comic_filter:
        "images/effects/comic.webp"

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