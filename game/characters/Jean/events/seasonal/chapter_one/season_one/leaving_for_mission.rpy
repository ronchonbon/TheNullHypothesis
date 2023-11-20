init python:

    def Jean_leaving_for_mission():
        label = "Jean_leaving_for_mission"

        conditions = [
            "day > 4",
            
            "((Player.location in bedrooms or Player.location in ['bg_girls_hallway', 'bg_hallway', 'bg_mall']) and Player.destination in ['bg_campus', 'bg_classroom', 'bg_danger', 'bg_pool', 'bg_lockers']) or ((Player.destination in bedrooms or Player.destination in ['bg_girls_hallway', 'bg_hallway', 'bg_mall']) and Player.location in ['bg_campus', 'bg_classroom', 'bg_danger', 'bg_pool', 'bg_lockers'])",
            
            "not Party",
            
            "time_index < 3 and weather != 'rain'"]

        traveling = True

        priority = 1

        return EventClass(label, conditions, traveling = traveling, priority = priority)

label Jean_leaving_for_mission:
    $ ongoing_Event = True

    $ temp_destination = Player.destination

    $ active_Girls.append(Jean)
    $ unlocked_locations.update({Jean.home: "renpy.call('travel', Jean)"})

    $ check_predicted_images()

    call remove_Characters(location = "bg_campus", fade = False) from _call_remove_Characters_46
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_50

    "As you're walking across campus you hear someone call out to you."

    ch_Jean "[Player.first_name]!"

    "You look around to see [Jean.name] running towards you."

    # call change_Outfit(Jean, Jean.Wardrobe.Outfits["Casual 2"], instant = True) from _call_change_Outfit_4

    call add_Characters(Jean) from _call_add_Characters_3

    $ Jean.change_face("happy")

    ch_Player "Hey, [Jean.name]."
    ch_Player "I haven't seen you around lately."
    ch_Player "Are we in different classes or something?"

    $ Jean.change_face("smirk2")

    ch_Jean "I'm a senior, but I'm also a part of the X-Men. I go out on missions occasionally!"
    ch_Jean "That keeps me super busy."
    ch_Jean "Actually, our team leader, Cyclops, just took most of the members out on a big mission."
    ch_Jean "Oh, duh, you probably haven't met him yet. He'll introduce himself as Scott." 

    $ Jean.change_face("neutral")

    ch_Jean "Anyways, I'm heading out with the rest of the team to take care of a problem that popped up closer to home, so I won't be around for a few days."

    $ Jean.change_face("sad")

    ch_Player "Damn. . . that's impressive. Well, please be careful." 

    $ Jean.change_face("worried2", blush = 1)

    ch_Player "Hopefully I'll see you around more when you get back." 

    $ Jean.change_face("neutral", blush = 1)

    "Jean looks at you for a second before responding."

    ch_Jean ". . . You will."

    $ Jean.change_face("worried1")

    ch_Jean "How have you been doing by the way?"
    ch_Jean "I-"

    $ Jean.change_face("neutral", eyes = "down")

    call phone_buzz from _call_phone_buzz
    
    "Her phone buzzes."
    ch_Jean "Shit. . ."

    $ Jean.change_face("smirk1")

    ch_Jean "I gotta go now, it was nice seeing you again!"

    call send_Characters(Jean, "hold") from _call_send_Characters_52

    $ ongoing_Event = False

    if Player.location != temp_destination:
        call travel(temp_destination) from _call_travel_1
    
    return