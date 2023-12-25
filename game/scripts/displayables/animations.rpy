transform fade_in(delay):
    alpha 0.0
    linear delay alpha 1.0

transform fade_out(delay):
    linear delay alpha 0.0

transform stat_rising(x_position):
    ypos 0.25 alpha 0.0
    choice:
        xpos x_position alpha 1.0
    choice:
        pause 0.01
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.02
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.03
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.04
        xpos x_position + 0.03 alpha 1.0
    choice:
        pause 0.05
        xpos x_position alpha 1.0
    choice:
        pause 0.06
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.07
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.08
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.09
        xpos x_position + 0.03 alpha 1.0
    parallel:
        linear 2.0 ypos 0.0
    parallel:
        linear 2.0 alpha 0.0

transform stat_falling(x_position):
    ypos 0.0 alpha 0.05
    choice:
        xpos x_position alpha 1.0
    choice:
        pause 0.01
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.02
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.03
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.04
        xpos x_position + 0.03 alpha 1.0
    choice:
        pause 0.05
        xpos x_position alpha 1.0
    choice:
        pause 0.06
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.07
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.08
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.09
        xpos x_position + 0.03 alpha 1.0
    parallel:
        linear 2.0 ypos 0.25
    parallel:
        linear 2.0 alpha 0.0

transform vibrate:
    subpixel True
    transform_anchor True

    ease 0.01 xoffset -2
    ease 0.02 xoffset 2
    ease 0.01 xoffset 0
    ease 0.01 xoffset -2
    ease 0.02 xoffset 2
    ease 0.01 xoffset 0
    ease 0.01 xoffset -2
    ease 0.02 xoffset 2
    ease 0.01 xoffset 0
    ease 0.01 xoffset -2
    ease 0.02 xoffset 2
    ease 0.01 xoffset 0

transform tremble(repetitions):
    subpixel True
    transform_anchor True
    
    block:
        ease 0.04 xoffset -0.7
        ease 0.08 xoffset 0.7
        ease 0.04 xoffset 0
        repeat repetitions

transform pulse(intensity, frequency = 1.0):
    alpha 0.0

    block:
        ease 2.0/frequency alpha 1.0*intensity
        ease 2.0/frequency alpha 0.0
        
        repeat

transform danger_room_pulsing:
    block:
        linear 1.0 alpha 0.0
        linear 1.0 alpha 2.0
        repeat

transform spin:
    block:
        linear 60 rotate 360
        rotate 0
        repeat

label knock_on_door(times = 1, intensity = 0.75):
    $ renpy.pause(0.5, hard = True)

    if times > 1:
        show expression "images/effects/knock.webp" as knock onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.4)

            zoom 0.0
            alpha 0.0

            block:
                ease 0.1 zoom intensity alpha 1.0
                ease 0.25 alpha 0.0
                repeat times - 1
    else:
        show expression "images/effects/knock.webp" as knock onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.4)

            zoom 0.0
            alpha 0.0

            ease 0.1 zoom intensity alpha 1.0
            ease 0.25 alpha 0.0

    $ renpy.pause(times*0.35, hard = True)

    return

label phone_buzz(times = 1, intensity = 0.5):
    if times > 1:
        show expression "images/effects/buzz.webp" as buzz onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.5)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom intensity alpha 1.0

            block:
                vibrate
                pause 0.5
                repeat times - 1

            ease 2.0 alpha 0.0
    else:
        show expression "images/effects/buzz.webp" as buzz onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.5)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom intensity alpha 1.0

            vibrate
            pause 0.5

            ease 2.0 alpha 0.0

    $ renpy.pause(times*0.5, hard = True)

    return