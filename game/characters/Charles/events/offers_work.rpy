init python:

    def Charles_offers_work():
        label = "Charles_offers_work"

        conditions = [
            "day > 4 and time_index < 3",

            "not Party"]

        traveling = True

        priority = 1

        return EventClass(label, conditions, traveling = traveling, priority = priority)

label Charles_offers_work:
    $ ongoing_Event = True
    
    $ renpy.dynamic(temp_destination = Player.destination)

    $ Charles.give_trait("telepathic")

    ch_Charles "Please come to my study, [Player.first_name]."
    ch_Charles "There is a matter I have not gotten the chance to bring to your attention yet."
    "You're not sure exactly how to respond to telepathy. . ."
    "You just say your response out loud."
    ch_Player "Uh, can you hear me? I'll be right there."
    ch_Charles "Yes, [Player.first_name], you need not speak out loud for me to hear you."
    "Was that chuckling you felt from him?"
    "You turn around and head to Xavier's study."

    $ Charles.remove_trait("telepathic")

    call send_Characters(Charles, "bg_study") from _call_send_Characters_302
    call set_the_scene(location = "bg_study") from _call_set_the_scene

    $ Charles.change_face("neutral")

    pause 1.0

    $ Charles.change_face("happy")

    ch_Charles "Hello, [Player.first_name]. Thank you for coming."
    ch_Player "Of course. Nothing bad happened, right?"
    ch_Charles "Do not worry, this is a simple matter that I think will benefit you."
    ch_Charles "You see, our 'unique' student population provides a set of challenges to the maintenance of campus grounds."
    ch_Charles "With many students growing into their powers and struggling for control of them, accidents are a frequent occurence."
    ch_Charles "I am of the belief that this is a good opportunity to have students themselves work around the mansion - to help maintain their home."
    ch_Charles "An opportunity to build character and camaraderie."
    ch_Player "So, basically, if someone blows a hole in the wall, students go and fix it?"
    ch_Charles "If it is a small task. We would not ask you to do anything unreasonable."
    ch_Charles "Rest assured, there is also a {i}monetary{/i} incentive."
    ch_Charles "Do you have any questions?"

    $ asking_questions = True
    $ asked_how_much = False
    $ asked_how_many_times = False
    $ asked_accidents = False

    while asking_questions:
        menu:
            extend ""
            "How much can I earn per task?" if not asked_how_much:
                ch_Charles "You will be generously compensated."
                ch_Charles "It may vary slightly, but the school pays well above minimum wage."

                $ asked_how_much = True
            "How many times can I work per day?" if not asked_how_many_times:
                ch_Charles "We limit students to one task per day, so as to give everyone a chance to work."
                ch_Charles "And to not distract them from their studies."

                $ asked_how_many_times = True
            "Are there really that many accidents around campus?" if not asked_accidents:
                $ Charles.change_face("neutral")

                ch_Charles "I'm afraid student accidents, historically, have not been the only source of damage to the campus. . ."

                $ Charles.change_face("sad")

                ch_Charles "External threats are always a factor."

                $ asked_accidents = True
            "No more questions, thanks.":
                $ asking_questions = False

    $ Charles.change_face("happy")

    ch_Charles "Just come to me whenever you'd like to work, and I will find a task for you."
    ch_Charles "Now, if that is all, you may go about your day."
    ch_Player "Thanks, Professor."

    if Player.location != temp_destination:
        "You leave the study and continue on your way."

    $ Charles.give_trait("gives_work")
    $ Charles.give_trait("has_jobs")

    if Player.location != temp_destination:
        call move_location(temp_destination) from _call_move_location

    $ ongoing_Event = False

    return