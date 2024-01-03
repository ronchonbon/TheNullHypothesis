init python:

    def get_color_transform(location):
        if location in ["bg_campus", "bg_pool"] and weather in ["rain", "snow"] and time_index < 2:
            color_transform = raining
        elif location in ["bg_campus", "bg_classroom", "bg_mall", "bg_pool"] and time_index == 0:
            color_transform = morning
        elif (location in bedrooms or location in ["bg_girls_hallway", "bg_hallway", "bg_study", "bg_campus", "bg_classroom", "bg_mall", "bg_pool"]) and time_index == 1:
            color_transform = daylight
        elif location in ["bg_girls_hallway", "bg_hallway", "bg_study", "bg_campus", "bg_classroom", "bg_mall", "bg_pool"] and time_index == 2:
            color_transform = sunset
        elif location in ["bg_study", "bg_campus", "bg_classroom", "bg_mall", "bg_pool"] and time_index > 2:
            color_transform = moonlight
        elif location in ["bg_girls_hallway", "bg_hallway"] and time_index > 2:
            color_transform = candlelit
        elif location == "bg_restaurant":
            color_transform = candlelit
        elif location == "bg_movies":
            color_transform = theater
        elif lighting == "moonlight":
            color_transform = moonlight
        elif lighting == "candlelit":
            color_transform = candlelit
        elif time_index == 4:
            color_transform = lights_off
        else:
            color_transform = indoors

        return color_transform

    def get_sprite_position(Character):
        return Character.sprite_position[0]

    def fade_to_black(delay):
        global black_screen

        black_screen = True

        renpy.pause(delay, hard = True)

        return

    def fade_in_from_black(delay):
        global black_screen
        
        black_screen = False

        renpy.pause(delay, hard = True)

        return

label show_Character(Character, t = None, sprite_anchor = None, x = None, y = None, sprite_zoom = None, sprite_rotation = None, sprite_layer = None, color_transforms = None, animation_transforms = None, fade = 0.5):
    $ check_predicted_images()
    
    $ Character.position = "standing"

    if Player.location == "bg_restaurant" and eating_dinner:
        if not x:
            $ x = Character.sprite_position[0]

        if not y:
            $ y = eval(f"{Character.tag}_standing_height")

        $ x += 0.01
        $ y += 0.03
        $ sprite_zoom = 1.4*eval(f"{Character.tag}_standing_zoom")
    elif Player.location == "bg_town":
        if not x:
            $ x = Character.sprite_position[0]

        if not y:
            $ y = eval(f"{Character.tag}_standing_height")

        $ y += 0.07

    $ different = False

    if sprite_anchor is None:
        $ sprite_anchor = eval(f"{Character.tag}_standing_anchor")
    elif sprite_anchor[1] == 1.0:
        $ sprite_anchor[0] = eval(f"{Character.tag}_standing_anchor")[0]
        $ sprite_anchor[1] = eval(f"{Character.tag}_standing_bottom")

    if Character.sprite_anchor[0] != sprite_anchor[0] and Character.sprite_anchor[1] != sprite_anchor[1]:
        $ different = True

    $ Character.sprite_anchor = sprite_anchor
    
    if x is not None:
        if Character.sprite_position[0] != x:
            $ different = True

        $ Character.sprite_position[0] = x

    if y is not None:
        if Character.sprite_position[1] != y:
            $ different = True

        $ Character.sprite_position[1] = y
    else:
        $ Character.sprite_position[1] = eval(f"{Character.tag}_standing_height")

    if sprite_zoom is None:
        $ sprite_zoom = eval(f"{Character.tag}_standing_zoom")

    if Character.sprite_zoom != sprite_zoom:
        $ different = True

    $ Character.sprite_zoom = sprite_zoom

    if sprite_rotation is not None:
        if Character.sprite_rotation != sprite_rotation:
            $ different = True

        $ Character.sprite_rotation = sprite_rotation

    if sprite_layer is not None:
        if Character.sprite_layer != sprite_layer:
            $ different = True

        $ Character.sprite_layer = sprite_layer
    else:
        $ Character.sprite_layer = 7

    if (Character in all_Companions and not renpy.showing(f"{Character.tag}_sprite standing")) or (Character in all_NPCs and not renpy.showing(f"{Character.tag}_sprite")) or different or color_transforms or animation_transforms:
        $ renpy.hide(f"{Character.tag}_sprite")
        
        if fade:
            if (((Character in all_Companions and renpy.showing(f"{Character.tag}_sprite standing")) or (Character in all_NPCs and renpy.showing(f"{Character.tag}_sprite"))) and not different) or animation_transforms:
                $ fade = False

        if t is not None and not black_screen and not Character.behavior == "teaching":
            $ transform_list = [
                change_sprite_anchor(Character.sprite_anchor[0], Character.sprite_anchor[1]),
                zoom_sprite(Character.sprite_zoom, t = t),
                move_sprite(Character.sprite_position[0], Character.sprite_position[1], t = t),
                rotate_sprite(Character.sprite_rotation, t = t)]
        else:
            $ transform_list = [
                change_sprite_anchor(Character.sprite_anchor[0], Character.sprite_anchor[1]),
                zoom_sprite(Character.sprite_zoom),
                move_sprite(Character.sprite_position[0], Character.sprite_position[1]),
                rotate_sprite(Character.sprite_rotation)]

        if color_transforms:
            python:
                for c_t in color_transforms:
                    transform_list.append(c_t)
        else:
            $ color_transform = get_color_transform(location = Player.location)
            $ transform_list.append(color_transform)

        if animation_transforms:
            python:
                for a_t in animation_transforms:
                    transform_list.append(a_t)

        if Character in all_Companions:
            $ renpy.show(f"{Character.tag}_sprite standing", at_list = transform_list, zorder = Character.sprite_layer, tag = f"{Character.tag}_sprite")
        else:
            $ renpy.show(f"{Character.tag}_sprite", at_list = transform_list, zorder = Character.sprite_layer, tag = f"{Character.tag}_sprite")

        if fade:
            with Dissolve(fade)

        if not Character.History.check("seen_Player", tracker = "recent"):
            $ Character.History.update("seen_Player")

    return

label hide_Character(Character, fade = 0.5, send_Offscreen = True):
    $ check_predicted_images()

    if fade:
        if not renpy.showing(f"{Character.tag}_sprite"):
            $ fade = False

    $ renpy.hide(f"{Character.tag}_sprite")

    if fade:
        with Dissolve(fade)

        $ renpy.pause(fade, hard = True)

    $ Character.sprite_position = [0.0, eval(f"{Character.tag}_standing_height")]

    $ Character.change_face()
    $ Character.change_arms()

    if send_Offscreen:
        if Character == left_Slot:
            $ left_Slot = None

        if Character == middle_Slot:
            $ middle_Slot = None

        if Character == right_Slot:
            $ right_Slot = None

        if Character.destination == Player.location:
            $ send_Characters_Offscreen(Character)

    return

label show_pose(Character, pose, t = None, x = None, y = None, sprite_zoom = None, sprite_rotation = None, sprite_layer = None, color_transforms = None, animation_transforms = None, fade = False):
    $ Character.position = pose

    $ check_predicted_images()
    
    $ Character.sprite_anchor = eval(f"{Character.tag}_{pose}_anchor")

    $ different = False

    if x is not None:
        if Character.sprite_position[0] != x:
            $ different = True

        $ Character.sprite_position[0] = x

    if y is not None:
        if Character.sprite_position[1] != y:
            $ different = True

        $ Character.sprite_position[1] = y
    else:
        $ Character.sprite_position[1] = eval(f"{Character.tag}_{pose}_height")

    if sprite_zoom is None:
        $ sprite_zoom = eval(f"{Character.tag}_{pose}_zoom")

    if Character.sprite_zoom != sprite_zoom:
        $ different = True

        $ Character.sprite_zoom = sprite_zoom
    
    if sprite_rotation is not None:
        if Character.sprite_rotation != sprite_rotation:
            $ different = True

        $ Character.sprite_rotation = sprite_rotation

    if sprite_layer is not None:
        if Character.sprite_layer != sprite_layer:
            $ different = True

        $ Character.sprite_layer = sprite_layer
    
    if not renpy.showing(f"{Character.tag}_sprite {pose}") or different or color_transforms or animation_transforms:
        if fade:
            if (renpy.showing(f"{Character.tag}_sprite {pose}") and not different) or animation_transforms:
                $ fade = False

        if pose != "standing":
            if t is not None and not black_screen:
                $ transform_list = [
                    change_sprite_anchor(Character.sprite_anchor[0], Character.sprite_anchor[1]),
                    zoom_sprite(Character.sprite_zoom, t = t),
                    move_sprite(Character.sprite_position[0], Character.sprite_position[1], t = t),
                    rotate_sprite(Character.sprite_rotation, t = t)]
            else:
                $ transform_list = [
                    change_sprite_anchor(Character.sprite_anchor[0], Character.sprite_anchor[1]),
                    zoom_sprite(Character.sprite_zoom),
                    move_sprite(Character.sprite_position[0], Character.sprite_position[1]),
                    rotate_sprite(Character.sprite_rotation)]
        else:
            if t is not None and not black_screen:
                $ transform_list = [
                    change_sprite_anchor(Character.sprite_anchor[0], Character.sprite_anchor[1]),
                    zoom_sprite(Character.sprite_zoom, t = t),
                    move_sprite(Character.sprite_position[0], Character.sprite_position[1], t = t),
                    rotate_sprite(Character.sprite_rotation, t = t)]
            else:
                $ transform_list = [
                    change_sprite_anchor(Character.sprite_anchor[0], Character.sprite_anchor[1]),
                    zoom_sprite(Character.sprite_zoom),
                    move_sprite(Character.sprite_position[0], Character.sprite_position[1]),
                    rotate_sprite(Character.sprite_rotation)]

        if color_transforms:
            python:
                for c_t in color_transforms:
                    transform_list.append(c_t)
        else:
            $ color_transform = get_color_transform(location = Player.location)
            $ transform_list.append(color_transform)

        if animation_transforms:
            python:
                for a_t in animation_transforms:
                    transform_list.append(a_t)

        $ renpy.show(f"{Character.tag}_sprite {pose}", at_list = transform_list, zorder = Character.sprite_layer, tag = f"{Character.tag}_sprite")
        
        if fade:
            with Dissolve(fade)

    return