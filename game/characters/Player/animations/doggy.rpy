transform doggy_left_leg_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        block:
            choice:
                pause 2.0
            choice:
                pause 5.0
            choice:
                pause 10.0

        block:
            choice:
                ease 2.0 rotate -1
            choice:
                ease 2.0 rotate 0
            choice:
                ease 2.0 rotate 1

        repeat

transform doggy_left_leg_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 3.0/speed
        ease 1.5/speed rotate -1
        ease 3.0/speed rotate 0

        repeat
    
transform doggy_left_leg_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed rotate -2*intensity
        ease 0.75/speed rotate 0

        repeat
    
transform doggy_right_leg_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        block:
            choice:
                pause 2.0
            choice:
                pause 5.0
            choice:
                pause 10.0

        block:
            choice:
                ease 2.0 rotate -1
            choice:
                ease 2.0 rotate 0
            choice:
                ease 2.0 rotate 1

        repeat

transform doggy_right_leg_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 3.0/speed
        ease 1.5/speed rotate 1
        ease 3.0/speed rotate 0

        repeat
    
transform doggy_right_leg_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed rotate 2
        ease 0.75/speed rotate 0

        repeat
    
transform doggy_left_arm_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        block:
            choice:
                pause 2.0
            choice:
                pause 5.0
            choice:
                pause 10.0

        block:
            choice:
                ease 2.0 rotate -1
            choice:
                ease 2.0 rotate 0
            choice:
                ease 2.0 rotate 1

        repeat

transform doggy_left_arm_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 3.0/speed
        ease 1.5/speed rotate -0.5
        ease 3.0/speed rotate 0

        repeat
    
transform doggy_left_arm_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed rotate -0.5*intensity
        ease 0.75/speed rotate 0.5*intensity

        repeat
    
transform doggy_right_arm_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        block:
            choice:
                pause 2.0
            choice:
                pause 5.0
            choice:
                pause 10.0

        block:
            choice:
                ease 2.0 rotate -3
            choice:
                ease 2.0 rotate 0
            choice:
                ease 2.0 rotate 3

        repeat

transform doggy_right_arm_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 3.0/speed
        ease 1.5/speed rotate 1
        ease 3.0/speed rotate 0

        repeat
    
transform doggy_right_arm_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed rotate 1*intensity
        ease 0.75/speed rotate -1*intensity

        repeat
    
transform doggy_hair_front_animation0:
    subpixel True
    transform_anchor True

transform doggy_hair_front_animation1:
    subpixel True
    transform_anchor True
    
transform doggy_hair_front_animation2:
    subpixel True
    transform_anchor True
    
transform doggy_head_animation0:
    subpixel True
    transform_anchor True

transform doggy_head_animation1:
    subpixel True
    transform_anchor True
    
transform doggy_head_animation2:
    subpixel True
    transform_anchor True
    
transform doggy_torso_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        parallel:
            block:
                choice:
                    pause 2.0
                choice:
                    pause 4.0
                choice:
                    pause 5.0

            block:
                parallel:
                    ease 2.0 ypos -0.001*sex_sampling/0.38
                    ease 2.0 ypos 0.001*sex_sampling/0.38
                parallel:
                    ease 2.0 yzoom 1.0025
                    ease 2.0 yzoom 0.9975
            repeat

        parallel:
            block:
                choice:
                    pause 2.0
                choice:
                    pause 5.0
                choice:
                    pause 10.0

            block:
                choice:
                    ease 2.0 rotate -0.5
                choice:
                    ease 2.0 rotate 0
                choice:
                    ease 2.0 rotate 0.5
            repeat

transform doggy_torso_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 3.0/speed
        ease 1.5/speed ypos 0.0025*sex_sampling/0.38
        ease 3.0/speed ypos 0.0*sex_sampling

        repeat
    
transform doggy_torso_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed ypos 0.0025*intensity*sex_sampling/0.38
        ease 0.75/speed ypos 0.0*sex_sampling

        repeat

transform doggy_right_arm_self_finger_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_right_arm_self_finger_ass_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, -0.01*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate -1.0

    block:
        ease 0.5 yzoom 0.99
        ease 0.5 yzoom 1.01

        repeat
    
transform doggy_hair_animation0:
    subpixel True
    transform_anchor True

transform doggy_hair_animation1:
    subpixel True
    transform_anchor True
    
transform doggy_hair_animation2:
    subpixel True
    transform_anchor True
    
transform doggy_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_ass_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 3.0/speed
        ease 1.5/speed ypos -0.005*sex_sampling/0.38
        ease 3.0/speed ypos 0.0*sex_sampling

        repeat
    
transform doggy_ass_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed ypos -0.01*intensity*sex_sampling/0.38
        ease 0.75/speed ypos 0.01*intensity*sex_sampling/0.38

        repeat
    
transform doggy_pussy_finger_pussy_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_pussy_finger_pussy_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed xzoom 1.05
        ease 0.75/speed xzoom 1.0

        repeat
    
transform doggy_anus_finger_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_anus_finger_ass_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.95 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed xzoom 1.0
        ease 0.75/speed xzoom 0.95

        repeat
    
transform doggy_pussy_sex_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_pussy_sex_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.75 yzoom 1.0
    rotate 0.0

    block:
        pause 0.75/speed
        linear 1.75/speed xzoom 1.0
        ease 0.7/speed xzoom 1.03
        ease 0.4/speed xzoom 1.05
        ease 0.2/speed xzoom 1.04
        ease 0.7/speed xzoom 1.03
        ease 1.8/speed xzoom 1.05
        ease 1.2/speed xzoom 0.75

        repeat
    
transform doggy_pussy_sex_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.025 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed xzoom 1.05
        ease 0.75/speed xzoom 1.025

        repeat
    
transform doggy_anus_anal_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_anus_anal_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.75 yzoom 1.0
    rotate 0.0

    block:
        pause 1.5/speed
        linear 1.0/speed xzoom 0.95
        ease 0.7/speed xzoom 1.16
        ease 0.4/speed xzoom 1.17
        ease 0.2/speed xzoom 1.16
        ease 0.7/speed xzoom 1.15
        ease 1.8/speed xzoom 1.2
        ease 0.8/speed xzoom 0.75
        pause 0.4/speed

        repeat
    
transform doggy_anus_anal_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.2 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed xzoom 1.275
        ease 0.75/speed xzoom 1.2

        repeat
    
transform doggy_pussy_grind_pussy_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0
    
transform doggy_pussy_grind_pussy_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.92 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed xzoom 1.0
        ease 0.75/speed xzoom 0.92

        repeat
    
transform doggy_anus_grind_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.85 yzoom 1.0
    rotate 0.0
    
transform doggy_anus_grind_ass_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.85 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed xzoom 0.9
        ease 0.75/speed xzoom 0.85

        repeat
    
transform doggy_pussy_dildo_pussy_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_pussy_dildo_pussy_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.95 yzoom 1.0
    rotate 0.0

    block:
        ease 0.375/speed xzoom 0.95
        ease 0.375/speed xzoom 0.92
        ease 0.375/speed xzoom 0.95
        ease 0.375/speed xzoom 0.92

        repeat
    
transform doggy_anus_dildo_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_anus_dildo_ass_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.95 yzoom 1.0
    rotate 0.0

    block:
        ease 0.65/speed xzoom 0.95
        ease 0.1/speed xzoom 0.94
        ease 0.1/speed xzoom 0.95
        ease 0.65/speed xzoom 0.92

        repeat

transform doggy_cock_sex_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0045*sex_sampling/0.38, 0.25*sex_sampling/0.38)
    xzoom 0.95 yzoom 0.95
    rotate 0.0

transform doggy_cock_sex_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0057*sex_sampling/0.38, 0.292*sex_sampling/0.38)
    xzoom 0.95 yzoom 0.95
    rotate 0.0

    ypos (0.292 - (0.292 - 0.14)*starting_depth)*sex_sampling/0.38

    block:
        ease 1.5/speed ypos 0.287*sex_sampling/0.38
        linear 1.5/speed ypos 0.277*sex_sampling/0.38
        ease 1.5/speed ypos 0.207*sex_sampling/0.38
        ease 3.0/speed ypos 0.292*sex_sampling/0.38

        repeat
    
transform doggy_cock_sex_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0055*sex_sampling/0.38, 0.17*sex_sampling/0.38)
    xzoom 0.95 yzoom 0.95
    rotate 0.0

    xpos (0.0055 - (0.0055 - 0.0045)*starting_depth)*sex_sampling/0.38 ypos (0.17 - (0.17 - 0.09)*starting_depth)*sex_sampling/0.38

    block:
        ease 0.75/speed xpos (0.0055 - (0.0055 - 0.0045)*intensity)*sex_sampling/0.38 ypos (0.17 - (0.17 - 0.09)*intensity)*sex_sampling/0.38
        ease 0.75/speed xpos 0.0055*sex_sampling/0.38 ypos 0.17*sex_sampling/0.38

        repeat

transform doggy_cock_anal_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.005*sex_sampling/0.38, 0.18*sex_sampling/0.38)
    xzoom 0.93 yzoom 0.93
    rotate 0.0

transform doggy_cock_anal_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0065*sex_sampling/0.38, 0.23*sex_sampling/0.38)
    xzoom 0.93 yzoom 0.93
    rotate 0.0

    ypos (0.23 - (0.23 - 0.09)*starting_depth)*sex_sampling/0.38

    block:
        ease 1.5/speed ypos 0.22*sex_sampling/0.38
        linear 1.5/speed ypos 0.215*sex_sampling/0.38
        ease 1.5/speed ypos 0.14*sex_sampling/0.38
        ease 3.0/speed ypos 0.23*sex_sampling/0.38

        repeat
    
transform doggy_cock_anal_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0065*sex_sampling/0.38, 0.15*sex_sampling/0.38)
    xzoom 0.93 yzoom 0.93
    rotate 0.0

    xpos (0.0065 - (0.0065 - 0.005)*starting_depth)*sex_sampling/0.38 ypos (0.13 - (0.13 - 0.07)*starting_depth)*sex_sampling/0.38

    block:
        ease 0.75/speed xpos 0.005*sex_sampling/0.38 ypos (0.13 - (0.13 - 0.07)*intensity)*sex_sampling/0.38
        ease 0.75/speed xpos 0.0065*sex_sampling/0.38 ypos 0.13*sex_sampling/0.38

        repeat

transform doggy_cock_grind_pussy_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.004*sex_sampling/0.38, 0.25*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_cock_grind_pussy_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.004*sex_sampling/0.38, 0.28*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed ypos (0.28 - (0.28 - 0.22)*intensity)*sex_sampling/0.38
        ease 0.75/speed ypos 0.28*sex_sampling/0.38

        repeat

transform doggy_cock_grind_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.005*sex_sampling/0.38, 0.18*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate 0.0
    
transform doggy_cock_grind_ass_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.005*sex_sampling/0.38, 0.21*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed ypos (0.21 - (0.21 - 0.16)*intensity)*sex_sampling/0.38
        ease 0.75/speed ypos 0.21*sex_sampling/0.38

        repeat

transform doggy_vibrator_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_vibrator_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        vibrate
        repeat
    
transform doggy_dildo_pussy_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.15*sex_sampling/0.38)
    xzoom 1.08 yzoom 1.08
    rotate 0.0

transform doggy_dildo_pussy_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.02*sex_sampling/0.38)
    xzoom 1.08 yzoom 1.08
    rotate 0.0

    block:
        ease 0.75/speed ypos -0.11*sex_sampling/0.38
        ease 0.75/speed ypos 0.02*sex_sampling/0.38

        repeat
    
transform doggy_dildo_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.00*sex_sampling/0.38, 0.04*sex_sampling/0.38)
    xzoom 0.96 yzoom 0.96
    rotate 0.0

transform doggy_dildo_ass_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.001*sex_sampling/0.38, -0.06*sex_sampling/0.38)
    xzoom 0.96 yzoom 0.96
    rotate 0.0

    block:
        ease 0.75/speed ypos -0.16*sex_sampling/0.38
        ease 0.75/speed ypos -0.06*sex_sampling/0.38

        repeat

transform doggy_male_left_arm_finger_pussy_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.27*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_male_left_arm_finger_pussy_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.005*sex_sampling/0.38, 0.262*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        parallel:
            ease 0.75/speed ypos 0.238*sex_sampling/0.38
            ease 0.75/speed ypos 0.262*sex_sampling/0.38
        parallel:
            ease 0.75/speed xzoom 0.98
            ease 0.75/speed xzoom 1.0
        parallel:
            ease 0.75/speed yzoom 0.94
            ease 0.75/speed yzoom 1.0
        parallel:
            ease 0.75/speed rotate -5
            ease 0.75/speed rotate 0

        repeat

transform doggy_male_left_arm_finger_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0035*sex_sampling/0.38, 0.27*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_male_left_arm_finger_ass_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0035*sex_sampling/0.38, 0.27*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate -5.0

    block:
        parallel:
            ease 0.75/speed ypos 0.25*sex_sampling/0.38
            ease 0.75/speed ypos 0.27*sex_sampling/0.38
        parallel:
            ease 0.75/speed xzoom 0.98
            ease 0.75/speed xzoom 1.0
        parallel:
            ease 0.75/speed yzoom 0.94
            ease 0.75/speed yzoom 1.0
        parallel:
            ease 0.75/speed rotate -11
            ease 0.75/speed rotate -5

        repeat

transform doggy_male_right_arm_finger_pussy_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.27*sex_sampling/0.38)
    xzoom 0.9 yzoom 0.9
    rotate 0.0

transform doggy_male_right_arm_finger_pussy_animation1:
    subpixel True
    transform_anchor True
    
    pos (-0.005*sex_sampling/0.38, 0.262*sex_sampling/0.38)
    xzoom 0.9 yzoom 0.9
    rotate 0.0

    block:
        parallel:
            ease 0.75/speed xpos 0.0*sex_sampling
            ease 0.75/speed xpos -0.005*sex_sampling/0.38
        parallel:
            ease 0.75/speed ypos 0.242*sex_sampling/0.38
            ease 0.75/speed ypos 0.262*sex_sampling/0.38
        parallel:
            ease 0.75/speed xzoom 0.88
            ease 0.75/speed xzoom 0.9
        parallel:
            ease 0.75/speed yzoom 0.85
            ease 0.75/speed yzoom 0.9
        parallel:
            ease 0.75/speed rotate 10
            ease 0.75/speed rotate 0

        repeat

transform doggy_male_right_arm_finger_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (-0.002*sex_sampling/0.38, 0.27*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_male_right_arm_finger_ass_animation1:
    subpixel True
    transform_anchor True
    
    pos (-0.002*sex_sampling/0.38, 0.27*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate 5.0

    block:
        parallel:
            ease 0.75/speed ypos 0.25*sex_sampling/0.38
            ease 0.75/speed ypos 0.27*sex_sampling/0.38
        parallel:
            ease 0.75/speed xzoom 0.98
            ease 0.75/speed xzoom 1.0
        parallel:
            ease 0.75/speed yzoom 0.94
            ease 0.75/speed yzoom 1.0
        parallel:
            ease 0.75/speed rotate 11
            ease 0.75/speed rotate 5

        repeat

transform doggy_male_left_arm_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_male_left_arm_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 3.0/speed
        ease 1.5/speed rotate 0.0
        ease 3.0/speed rotate 0.0

        repeat
    
transform doggy_male_left_arm_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed rotate 0.0
        ease 0.75/speed rotate 0.0

        repeat

transform doggy_male_right_arm_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_male_right_arm_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 3.0/speed
        ease 1.5/speed rotate 0.0
        ease 3.0/speed rotate 0.0

        repeat
    
transform doggy_male_right_arm_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed rotate 0.0
        ease 0.75/speed rotate 0.0

        repeat

transform doggy_right_forearm_self_finger_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_right_forearm_self_finger_ass_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0, -0.01)
    xzoom 1.0 yzoom 1.0
    rotate -1.0

    block:
        ease 1.0 yzoom 0.99
        ease 1.0 yzoom 1.01

        repeat

transform doggy_mask_finger_pussy_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_mask_finger_pussy_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.95 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed xzoom 1.0
        ease 0.75/speed xzoom 0.95

        repeat
    
transform doggy_mask_finger_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_mask_finger_ass_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.95 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed xzoom 1.0
        ease 0.75/speed xzoom 0.95

        repeat

transform doggy_mask_sex_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_mask_sex_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 0.8/speed
        ease 0.6/speed xzoom 1.15
        ease 0.3/speed xzoom 1.105
        ease 0.8/speed xzoom 1.11
        ease 1.0/speed xzoom 1.12
        ease 0.3/speed xzoom 1.11
        ease 0.7/speed xzoom 1.1
        ease 2.0/speed xzoom 1.15
        ease 1.0/speed xzoom 1.0

        repeat

transform doggy_mask_sex_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.2 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed xzoom 1.3
        ease 0.75/speed xzoom 1.2

        repeat
    
transform doggy_mask_anal_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_mask_anal_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        xzoom 1.5
        pause 0.8/speed
        ease 0.6/speed xzoom 1.22
        ease 0.3/speed xzoom 1.23
        ease 0.8/speed xzoom 1.24
        ease 1.0/speed xzoom 1.25
        ease 0.3/speed xzoom 1.24
        ease 0.7/speed xzoom 1.23
        ease 2.0/speed xzoom 1.22
        ease 1.0/speed xzoom 1.0

        repeat

transform doggy_mask_anal_animation2:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.3 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75/speed xzoom 1.35
        ease 0.75/speed xzoom 1.3

        repeat

transform doggy_mask_dildo_pussy_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_mask_dildo_pussy_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.92 yzoom 1.0
    rotate 0.0

    block:
        ease 0.375/speed xzoom 0.95
        ease 0.375/speed xzoom 0.92
        ease 0.375/speed xzoom 0.95
        ease 0.375/speed xzoom 0.92

        repeat
    
transform doggy_mask_dildo_ass_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_mask_dildo_ass_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 0.92 yzoom 1.0
    rotate 0.0

    block:
        ease 0.65/speed xzoom 0.95
        ease 0.1/speed xzoom 0.94
        ease 0.1/speed xzoom 0.95
        ease 0.65/speed xzoom 0.92

        repeat

transform doggy_male_head_eat_pussy_animation0:
    subpixel True
    transform_anchor True
    
    anchor (0.0, 0.0)
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    offset (-int(40*sex_sampling), -int(118*sex_sampling))
    xzoom 2.63*sex_sampling yzoom 2.63*sex_sampling
    rotate 0.0

transform doggy_male_head_eat_pussy_animation1:
    subpixel True
    transform_anchor True
    
    anchor (0.0, 0.0)
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    offset (-int(40*sex_sampling), -int(118*sex_sampling))
    xzoom 2.63*sex_sampling yzoom 2.63*sex_sampling
    rotate 0.0

    block:
        parallel:
            ease 0.75 ypos -0.0025*sex_sampling/0.38
            ease 0.75 ypos 0.0025*sex_sampling/0.38
            repeat
        parallel:
            ease 4.0 rotate -2.0
            ease 4.0 rotate 2.0
            repeat

        repeat

transform doggy_male_head_eat_ass_animation0:
    subpixel True
    transform_anchor True
    
    anchor (0.0, 0.0)
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    offset (-int(40*sex_sampling), -int(118*sex_sampling))
    xzoom 2.63*sex_sampling yzoom 2.63*sex_sampling
    rotate 0.0

transform doggy_male_head_eat_ass_animation1:
    subpixel True
    transform_anchor True
    
    anchor (0.0, 0.0)
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    offset (-int(40*sex_sampling), -int(118*sex_sampling))
    xzoom 2.63*sex_sampling yzoom 2.63*sex_sampling
    rotate 0.0

    block:
        parallel:
            ease 0.75 ypos -0.0025*sex_sampling/0.38
            ease 0.75 ypos 0.0025*sex_sampling/0.38
            repeat
        parallel:
            ease 4.0 rotate -2.0
            ease 4.0 rotate 2.0
            repeat

        repeat

transform doggy_male_tongue_animation0:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_male_tongue_animation1:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        ease 0.75 yzoom 0.5
        ease 0.75 yzoom 1.0

        repeat

transform doggy_cock_cumshot_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.21*sex_sampling/0.38)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

transform doggy_cock_creampie_animation:
    subpixel True
    transform_anchor True
    
    pos ((0.0055 - (0.0055 - 0.0045)*intensity)*sex_sampling/0.38, (0.17 - (0.17 - 0.09)*intensity)*sex_sampling/0.38)
    xzoom 0.95 yzoom 0.95
    rotate 0.0

transform doggy_cock_anal_creampie_animation:
    subpixel True
    transform_anchor True
    
    pos (0.005*sex_sampling/0.38, (0.13 - (0.13 - 0.07)*intensity)*sex_sampling/0.38)
    xzoom 0.93 yzoom 0.93
    rotate 0.0

transform doggy_pussy_creampie_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.05 yzoom 1.0
    rotate 0.0

transform doggy_anus_anal_creampie_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.275 yzoom 1.0
    rotate 0.0

transform doggy_mask_creampie_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.3 yzoom 1.0
    rotate 0.0

transform doggy_mask_anal_creampie_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0*sex_sampling, 0.0*sex_sampling)
    xzoom 1.35 yzoom 1.0
    rotate 0.0