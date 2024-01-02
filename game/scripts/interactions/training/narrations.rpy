label chapter_1_season_1_training_narrations:
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        "You make sure to train as [Laura.name] instructed and practice all the techniques and exercises she taught you." 
        "Her prescribed workouts take you multiple hours to fully complete, and you're completely spent by the end."
    elif dice_roll == 2:
        "You start practicing techniques the way [Laura.name] showed you."
        "She was very specific, but without any supervision, you have to be careful not to start developing bad habits."
        "After making sure you do every last workout, you can barely walk properly. It probably took you 3 hours to finish everything."
    elif dice_roll == 3:
        "You look at the list of exercises and workouts [Laura.name] gave you to do. It'll probably take 3 hours to finish everything."
        "You dive in head first and make sure to do every last repetition."
        "It doesn't quite take the full 3 hours, but nearly."
    elif dice_roll == 4:
        "[Laura.name] said you're not ready to practice scenarios on your own, so you just focus on exercises and improving your technique."
        "There are plenty of other people training as well, and you do your best not to let their training influence you."
        "After a couple of hours, you're satisfied and finish the session with a light workout."
    elif dice_roll == 5:
        "You continue working on the various exercises and techniques [Laura.name] directed you on."
        "You're feeling a bit more fatigued today than usual, and it takes longer to finish everything."
        "By the end, your legs feel like jelly, and you spend even more time trying to stretch everything out."

    return

label chapter_1_season_2_training_narrations:
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        "You look over the training regimen [Laura.name] left you with."
        "It's a {i}lot{/i}, so you get to work."
        "You thought it would take way longer to complete and while you're exhausted, you made reasonable time."
    elif dice_roll == 2:
        "You get started and continue to surprise yourself with how much your exercise capacity has increased."
        "Several hours of hard cardio would've previously wiped you out for the entire day."
        "Now, after innumerable exercises and repetitions, you're tired, but can already feel your body recovering."
    elif dice_roll == 3:
        "You get the short blade [Laura.name] has been teaching you how to use. . . the sharp one."
        "It's closer to a long knife than a sword."
        "She might have a point, making you practice with a real one, so you can properly respect it."
        "You manage to only cut yourself a couple times, and the rest of the workout goes smoothly, if taking a long time."
    elif dice_roll == 4:
        "You throw yourself into all the exercises and practice the hand-to-hand techniques with vigor."
        "Fighting seems to come naturally to you. . . which should probably be disconcerting, but you try not to think about it."
        "After several hours, you thoroughly exhaust yourself and feel satisfied with your effort."
    elif dice_roll == 5:
        "Starting with a warm up, you notice your flexibility has been getting better lately."
        "[Laura.name] still doesn't think you're ready to take advantage of all the Danger Room has to offer, so you just focus on honing your current skills."
        "By the end, you feel like you could eat an entire cow and wonder if your improved strength and stamina also requires more calories than normal."

    return

label chapter_1_season_3_training_narrations:
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        "You start the training as normal, focusing on honing your body and your skills."
        "Once you're satisfied, you activate your power and push yourself to exhaustion."
        "Your work capacity and time with the power active is increasing, but progress is slow."
    elif dice_roll == 2:
        "Today, you start by activating your power and try to maintain it throughout the entire session."
        "You only make it just over halfway, before you're exhausted."
        "You slog through to the end, at least a bit better than last time."
    elif dice_roll == 3:
        "You practice with a wide variety of weapons, doing more damage to yourself, than to your imaginary opponents."
        "Activating your power, you only manage to hit yourself even harder, growing clumsier with the weapons, despite increased proprioception."
        "The small injuries heal quickly enough, and you're only left with some bruises as the exhaustion washes over you."
    elif dice_roll == 4:
        "You throw yourself into the training, focusing on technique, trying to push harder than last time."
        "Activating your power seems to amplify your clumsiness and unrefined skills."
        "Maybe your standards are just out of whack, considering your only frame of reference is a monster like [Laura.name]."
    elif dice_roll == 5:
        "Starting with a warm up, you notice the exercises continuing to get easier."
        "Your technique and skills are also consistently improving, but there's still a long way to go."
        "Your power control doesn't seem to be making quite as much progress, since it's still all or nothing."
        "On the flip side, at least you continue to improve its duration."

    return

label chapter_1_season_4_training_narrations:
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        "You make sure nobody is nearby and dive into your training."
        "Keeping your power on for the entire session is doable now, but still seems to make you extra clumsy."
        "You're still improving, slowly but surely."
    elif dice_roll == 2:
        "Today, you start by activating your power, but limit it significantly."
        "Keeping a leash on it takes up a lot of your focus, but it allows you to train for longer than normal."
        "The backlash isn't quite so bad, but you could still use a nap."
    elif dice_roll == 3:
        "By now, [Laura.name] has made sure you're familiar with a plethora of different weapons."
        "As you practice with many different types, you're still not quite sure what kind you prefer."
        "Having your power active still makes you clumsy, and you manage to cut yourself more than once."
    elif dice_roll == 4:
        "You work on technique, but with and without your powers."
        "Normally a person would've stagnated by now, but your specific advantages allow you to continue to improve."
        "You're satisfied with your progress so far, but compared to [Laura.name], you're still a defenseless infant."
    elif dice_roll == 5:
        "Wrestling your power under control has been getting easier, but still takes a lot of focus."
        "Constantly changing it throughout the workout is an even bigger drain and dramatically shortens the time you can use it."
        "It's better than last time, at least."

    return