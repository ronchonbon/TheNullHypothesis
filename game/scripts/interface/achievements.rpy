init -1:

    default achievement_messages = []
    default achievement_message = None

    default temp_achievements = [0]

style achievements is default

style achievements_frame:
    background Frame(At("images/interface/belt/update.webp", interface), 10, 10)

    padding (15, 15, 15, 15)

style achievements_text:
    font "agency_fb.ttf"

    size 32
    
screen achievements_screen():
    layer "interface"

    style_prefix "achievements"

    if sandbox and not ongoing_Event:
        timer 10.0 action Function(achievements_screen_result) repeat True

    if achievement_messages and not achievement_message:
        timer 0.2 action [
            SetVariable("achievement_message", achievement_messages[0]), 
            RemoveFromSet(achievement_messages, achievement_messages[0]),
            Play("sound", "sounds/interface/achievement.ogg")]

    if achievement_message:
        fixed align (0.0, 1.0) xysize (int(766*game_resolution), int(277*game_resolution)):
            if achievements[achievement_message]["points"] == 5:
                add "images/interface/belt/achievement_bronze.webp" zoom interface_adjustment
            elif achievements[achievement_message]["points"] == 10:
                add "images/interface/belt/achievement_silver.webp" zoom interface_adjustment
            elif achievements[achievement_message]["points"] == 20:
                add "images/interface/belt/achievement_gold.webp" zoom interface_adjustment
            elif achievements[achievement_message]["points"] == 40:
                add "images/interface/belt/achievement_foil.webp" zoom interface_adjustment

            frame anchor (0.5, 0.5) pos (0.65, 0.5) xysize (0.6, 0.9):
                background None

                text achievement_message

            at transform:
                fade_in(0.4)
                pause 2.5
                fade_out(0.4)

        timer 3.3 action SetVariable("achievement_message", None)

init python:

    def achievements_screen_result():
        global achievement_messsages

        for a in achievements.keys():
            achievement.register(a, stat_max = achievements[a]["goal"])

            if eval(achievements[a]["condition"]) >= achievements[a]["goal"]:
                if not achievement.has(a):
                    if a not in achievement_messages:
                        achievement_messages.append(a)            

            achievement.progress(a, eval(achievements[a]["condition"]))

            if eval(achievements[a]["condition"]) >= achievements[a]["goal"]:
                if not achievement.has(a):
                    achievement.grant(a)

        return