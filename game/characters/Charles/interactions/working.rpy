label Charles_ask_for_job:
    $ dice_roll = renpy.random.randint(1, 6)

    if dice_roll == 1:
        call Charles_gardening_job from _call_Charles_gardening_job
    elif dice_roll == 2:
        call Charles_pool_cleaning_job from _call_Charles_pool_cleaning_job
    elif dice_roll == 3:
        call Charles_hallway_cleaning_job from _call_Charles_hallway_cleaning_job
    elif dice_roll == 4:
        call Charles_kitchen_cleaning_job from _call_Charles_kitchen_cleaning_job
    elif dice_roll == 5:
        call Charles_gym_cleaning_job from _call_Charles_gym_cleaning_job
    elif dice_roll == 6:
        call Charles_security_maintenance_job from _call_Charles_security_maintenance_job

    return

label Charles_no_jobs:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Charles.change_face("confused1") 

        ch_Charles "You have already worked the maximum amount today."
    elif dice_roll == 2:
        ch_Charles "Another job already?"
    elif dice_roll == 3:
        $ Charles.change_face("confused1") 

        ch_Charles "I'm afraid that's all you can work today."

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Charles.change_face("neutral")  

        ch_Charles "Students are not allowed to exceed their daily quota."
    elif dice_roll == 2:
        $ Charles.change_face("neutral")  

        ch_Charles "I suggest you make the most of your free time, [Player.first_name]."
    elif dice_roll == 3:
        $ Charles.change_face("neutral")  

        ch_Charles "May I suggest attending to your studies instead, [Player.first_name]?"

    return

label Charles_no_jobs_asked_once:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Charles.change_face("confused1") 

        ch_Charles "I appreciate your willingness, but no." 
        ch_Charles "I cannot allow you a second shift, lest another student be unable to work because of it."
    elif dice_roll == 2:
        $ Charles.change_face("confused1") 

        ch_Charles "As I said before, there are no work opportunities available for you."
    elif dice_roll == 3:
        $ Charles.change_face("confused1") 

        ch_Charles "Do not worry, [Player.first_name], there will be plenty more opportunities for you to work in the future."

    return

label Charles_no_jobs_asked_twice:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Charles "While there may be opportunities in the future for students to work more than once per day, it will not be allowed for the time being." 

        $ Charles.change_face("angry1") 

        ch_Charles "No amount of pleading will change that for the moment."
    elif dice_roll == 2:
        $ Charles.change_face("confused1") 

        ch_Charles "Come now, [Player.first_name], surely there are better uses of your time than persisting on this matter."

    return

label Charles_too_late_to_work:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Charles "I'm afraid we only allow students to work during waking hours." 
        ch_Charles "Maintaining a sensible sleep schedule is important for your studies."
    elif dice_roll == 2:
        ch_Charles "Unfortunately, we restrict student working hours to daylight hours."
        ch_Charles "Feel free to come back tomorrow, [Player.first_name]."

    return

label Charles_too_late_to_work_asked_once:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Charles.change_face("confused1") 

        ch_Charles "I am about to go to sleep myself." 
        ch_Charles "There will be plenty of work available in the morning."
    elif dice_roll == 2:
        $ Charles.change_face("confused1")

        ch_Charles "As I said, [Player.first_name], it is too late for students to work."

    return

label Charles_too_late_to_work_asked_twice:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Charles.change_face("confused1") 

        ch_Charles "If you are that restless, might I recommend a training exercise in the Danger Room?"
    elif dice_roll == 2:
        $ Charles.change_face("confused1") 

        ch_Charles "I must insist that you wait until daylight."

    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Charles.change_face("neutral") 

        ch_Charles "You may find work again in the morning."
    elif dice_roll == 2:
        $ Charles.change_face("neutral")

        ch_Charles "There will be plenty of time to engage in work opportunities in the morning."

    return