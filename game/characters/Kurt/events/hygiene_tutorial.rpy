init python:

    def Kurt_hygiene_tutorial():
        label = "Kurt_hygiene_tutorial"

        conditions = [
            "Player.location == 'bg_danger'",
            
            "Player.sweat >= Player.sweaty_threshold",

            "Player.location not in [Kurt.location, Kurt.destination]",

            "not get_Present(location = Player.location)[0]"]

        waiting = True
        traveling = True

        priority = 98

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Kurt_hygiene_tutorial:
    $ belt_disabled = True

    pause 1.0

    $ ongoing_Event = True

    $ Kurt.outfit = "casual"
    
    call Kurt_teleports_in from _call_Kurt_teleports_in

    $ Kurt.change_arms("neutral")
    $ Kurt.change_face("happy")

    ch_Player "Gah!"
    ch_Kurt "Bruder!"

    $ Kurt.change_face("confused1")
    $ Kurt.change_arms("neutral", right_arm = "extended")

    ch_Kurt "Zee training going well?"
    ch_Player "Dude, you're going to give me a heart-"

    $ Kurt.change_face("smirk2")
    $ Kurt.change_arms("crossed")

    ch_Kurt "I believe you are already aware, but just in case all zee excitement from zee past few days has made you forgetful. . ."

    $ Kurt.change_face("confused1", mouth = "smirk")

    ch_Kurt "Hygiene is quite important."

    $ Kurt.change_face("confused1", mouth = "smirk", eyes = "left")

    ch_Kurt "If you look at zee top right of your screen, you will see a small icon telling you a shower is needed."
    ch_Player "My 'screen'?"

    $ Kurt.change_face("confused1")
    $ Kurt.change_arms("neutral", right_arm = "extended")

    ch_Kurt "Ja, a little icon to zee left of zee temperature."

    $ Kurt.change_face("neutral")
    $ Kurt.change_arms("crossed")

    ch_Kurt "Physical exertion. . ."

    $ Kurt.change_face("suspicious1")

    ch_Kurt ". . . such as training, and vatever gutter your mind trailed off to, can make you sweaty."

    $ Kurt.change_face("smirk2")

    ch_Kurt "Swimming too, zee smell of chlorination can linger for quite a while."
    
    $ Kurt.change_arms("neutral", left_arm = "extended")

    ch_Kurt "I suggest you get used to showering after such activities. And make sure to shower every couple of days even if you don't sink you need one. . ."
    
    $ Kurt.change_face("confused1", mouth = "smirk")
    $ Kurt.change_arms("crossed")

    ch_Kurt "If you don't, I fear zee ladies may not have such a good opinion of you."
    
    $ Kurt.change_face("smirk2")

    ch_Kurt "I alvays find quick showers in zee morning or night are most efficient."
    # "Neglecting to take care of your hygiene will result in a significant penalty to {color=#c11b17}Love{/color} and {color=#f3a3b3}Desire{/color} gained with the girls."
    
    $ Kurt.change_face("happy")
    $ Kurt.change_arms("neutral")

    ch_Kurt "Zat is all."
    ch_Kurt "I have faith in you, mein Bruder."
    ch_Kurt "Don't be stinky."

    call Kurt_teleports_out from _call_Kurt_teleports_out

    $ belt_disabled = False

    $ ongoing_Event = False
    
    return