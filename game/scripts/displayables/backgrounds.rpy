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

image shower_steam_midground:
    At("images/effects/steam2.webp", inverse_background_scale)

    subpixel True

    yalign 1.0

    xoffset -int(2*config.screen_width/background_adjustment)

    block:
        linear 45.0 xoffset 0
        xoffset -int(2*config.screen_width/background_adjustment)
        repeat

image shower_steam_cover:
    At("images/effects/steam1.webp", inverse_background_scale)

    subpixel True

    yalign 1.0

    xoffset 0
    alpha 0.8

    block:
        linear 30.0 xoffset -int(2*config.screen_width/background_adjustment)
        xoffset 0
        repeat
    
layeredimage bg_Player:
    always:
        "images/backgrounds/base/bg_Player_[lighting].webp"
        
    if "acoustic_panels" in Player.inventory.keys() and Player.inventory["acoustic_panels"][0].Owner == Player:
        "images/backgrounds/base/bg_Player_acoustic_panels_[lighting].webp"
        
    if "motorcycle_helmet" in Player.inventory.keys() and Player.inventory["motorcycle_helmet"][0].Owner == Player:
        "images/backgrounds/base/bg_Player_helmet_[lighting].webp"
        
    if "sound_system" in Player.inventory.keys() and Player.inventory["sound_system"][0].Owner == Player:
        "images/backgrounds/base/bg_Player_sound_system_[lighting].webp"
        
    if "electric_guitar" in Player.inventory.keys() and Player.inventory["electric_guitar"][0].Owner == Player:
        "images/backgrounds/base/bg_Player_guitar_[lighting].webp"

    if Player.messy_bed:
        "images/backgrounds/base/bg_Player_messy_bed_[lighting].webp"
    else:
        "images/backgrounds/base/bg_Player_bed_[lighting].webp"
        
    if "record_player" in Player.inventory.keys() and Player.inventory["record_player"][0].Owner == Player:
        "images/backgrounds/base/bg_Player_record_player_[lighting].webp"

    if Player.clothes_on_floor:
        "images/backgrounds/base/bg_Player_clothes_[lighting].webp"

layeredimage bg_danger_lights:
    if danger_red_alert:
        "images/backgrounds/base/bg_danger_lights_red.webp"
    else:
        "images/backgrounds/base/bg_danger_lights.webp"

layeredimage bg_infirmary:
    if time_index < 3:
        "images/backgrounds/base/bg_infirmary_day.webp"
    else:
        "images/backgrounds/base/bg_infirmary_night.webp"

    if infirmary_in_bed and time_index < 3:
        "images/backgrounds/base/bg_infirmary_bed.webp"
    elif infirmary_bed and time_index < 3:
        "images/backgrounds/base/bg_infirmary_bed_empty.webp"
    elif infirmary_in_bed:
        "images/backgrounds/base/bg_infirmary_bed_night.webp"
    elif infirmary_bed:
        "images/backgrounds/base/bg_infirmary_bed_empty_night.webp"
    
    if infirmary_in_bed:
        "images/backgrounds/base/bg_infirmary_screenlight.webp"

    if infirmary_screen1:
        "images/backgrounds/base/bg_infirmary_screens1.webp"

    if infirmary_screen2:
        "images/backgrounds/base/bg_infirmary_screens2.webp"

    if infirmary_screen3:
        "images/backgrounds/base/bg_infirmary_screens3.webp"        

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
        At("black_fade", invisible)

    if Player.location in bedrooms or Player.location in ["bg_infirmary"]:
        "[Player.location]"

    if Player.location not in ["bg_campus", "bg_pool"]:
        Null()
    elif weather:
        "images/backgrounds/base/[Player.location]_[time_index]_[weather].webp"
    elif Player.location == "bg_campus" and not campus_grass_cut:
        "images/backgrounds/base/bg_campus_[time_index]_grass.webp"
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
        At("bg_danger_lights", danger_room_pulsing)

    if Player.location in ["traveling", "bg_door", "bg_restaurant_bathroom"]:
        "black_fade"

    transform_anchor True
    align (0.5, 0.5)

    zoom background_adjustment

layeredimage midground:
    always:
        At("black_fade", invisible)

    if Player.location != "bg_classroom":
        Null()
    elif time_index <= 3:
        "images/backgrounds/base/bg_classroom_podium_[lighting].webp"
    else:
        "images/backgrounds/base/bg_classroom_podium_night.webp"

    if Player.location == "bg_mall" and time_index < 3:
        "images/backgrounds/base/bg_mall_people_[lighting].webp"

    if Action_screen_showing:
        At(At("background", blurred_background), inverse_background_scale)

    if Player.location in ["bg_lockers", "bg_shower_Player", "bg_shower_Rogue", "bg_shower_Laura", "bg_shower_Jean"] and shower_steam:
        At("shower_steam_midground", fade_in(2.0))
        
    transform_anchor True
    align (0.5, 1.0)

    zoom background_adjustment

layeredimage foreground:
    always:
        At("black_fade", invisible)

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
        At("black_fade", invisible)

    if Player.location != "bg_classroom":
        Null()
    elif time_index <= 3:
        "images/backgrounds/base/bg_classroom_foreground_[lighting].webp"
    else:
        "images/backgrounds/base/bg_classroom_foreground_night.webp"
        
    if Player.location in ["bg_lockers", "bg_shower_Player", "bg_shower_Rogue", "bg_shower_Laura", "bg_shower_Jean"] and shower_steam:
        At("shower_steam_cover", fade_in(2.0))
    elif Player.location == "bg_restaurant" and eating_dinner:
        "bg_restaurant_table"

    transform_anchor True
    align (0.5, 1.0)

    zoom background_adjustment

layeredimage cover2:
    always:
        At("black_fade", invisible)

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
        At("black_fade", invisible)

    if cinematic_bars and (ongoing_Event or not sandbox):
        At(At("black_fade", top_bar), fade_in(0.4))
    elif cinematic_bars:
        At(At("black_fade", top_bar), fade_out(0.4))

    transform_anchor True
    align (0.5, 0.5)

layeredimage bottom_bar:
    always:
        At("black_fade", invisible)

    if cinematic_bars and (ongoing_Event or not sandbox):
        At(At("black_fade", bottom_bar), fade_in(0.4))
    elif cinematic_bars:
        At(At("black_fade", bottom_bar), fade_out(0.4))

    transform_anchor True
    align (0.5, 0.5)
        
layeredimage black_screen:
    always:
        At("black_fade", invisible)

    if black_screen:
        At("black_fade", fade_in(0.4))
    else:
        At("black_fade", fade_out(0.4))

    transform_anchor True
    align (0.5, 0.5)

layeredimage filter:
    always:
        At("black_fade", invisible)

    if comic_filter:
        "images/effects/comic.webp"

    if Player.desire >= 90:
        At("images/interface/Action_menu/climax_fringe.webp", pulse(intensity = 1.0))
    elif Player.desire >= 80:
        At("images/interface/Action_menu/climax_fringe.webp", pulse(intensity = 0.8))
    elif Player.desire >= 70:
        At("images/interface/Action_menu/climax_fringe.webp", pulse(intensity = 0.6))
    elif Player.desire >= 60:
        At("images/interface/Action_menu/climax_fringe.webp", pulse(intensity = 0.4))
    elif Player.desire >= 50:
        At("images/interface/Action_menu/climax_fringe.webp", pulse(intensity = 0.2))

    if Player.power >= 100:
        At("images/interface/Player_power/power_white.webp", pulse(intensity = 1.0, frequency = 2.0))
    elif Player.power >= 75:
        At("images/interface/Player_power/power_white.webp", pulse(intensity = 0.75, frequency = 1.5))
    elif Player.power >= 50:
        At("images/interface/Player_power/power_white.webp", pulse(intensity = 0.5))
    elif Player.power > 25:
        At("images/interface/Player_power/power_white.webp", pulse(intensity = 0.25))

    if Player.power >= 100:
        At("images/interface/Player_power/veins_black.webp", pulse(intensity = 1.0, frequency = 2.0))
    elif Player.power >= 75:
        At("images/interface/Player_power/veins_black.webp", pulse(intensity = 0.75, frequency = 1.5))
    elif Player.power >= 50:
        At("images/interface/Player_power/veins_black.webp", pulse(intensity = 0.5))
    elif Player.power > 25:
        At("images/interface/Player_power/veins_black.webp", pulse(intensity = 0.25))

    transform_anchor True
    align (0.5, 0.5)

    zoom background_adjustment

image comic_cutout1 = Window(Layer("comic_cutout1"), background = "#000000", padding = (10, 10, 10, 10))

image comic_cutout2 = Window(Layer("comic_cutout2"), background = "#000000", padding = (10, 10, 10, 10))

image comic_cutout3 = Window(Layer("comic_cutout3"), background = "#000000", padding = (10, 10, 10, 10))

image comic_cutout4 = Window(Layer("comic_cutout4"), background = "#000000", padding = (10, 10, 10, 10))