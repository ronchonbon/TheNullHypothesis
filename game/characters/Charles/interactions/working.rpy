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
    $ Charles.change_face("confused") 

    ch_Charles "You have already worked once today."

    $ Charles.change_face("neutral")  

    ch_Charles "Unfortunately students are not allowed to exceed their daily quota." 

    return

label Charles_no_jobs_asked_once:
    ch_Charles "I appreciate your willingness, but no." 
    ch_Charles "I cannot allow you a second shift, lest another student be unable to work because of it."

    return

label Charles_no_jobs_asked_twice:
    ch_Charles "While there may be opportunities in the future for students to work more than once per day, it will not be allowed for the time being." 

    $ Charles.change_face("angry") 

    ch_Charles "No amount of pleading will change that for the moment."

    return

label Charles_too_late_to_work:
    ch_Charles "I'm afraid we only allow students to work during waking hours" 
    ch_Charles "Maintaining a sensible sleep schedule is important for your studies."

    return

label Charles_too_late_to_work_asked_once:
    $ Charles.change_face("confused") 

    ch_Charles "I am about to go to sleep myself." 
    ch_Charles "There will be plenty of work available in the morning."

    return

label Charles_too_late_to_work_asked_twice:
    $ Charles.change_face("confused") 

    ch_Charles "If you are that restless, might I recommend a training exercise in the Danger Room?" 

    $ Charles.change_face("neutral") 

    ch_Charles "You may find work again in the morning."

    return