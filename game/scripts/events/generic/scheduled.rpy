init python:

    def Player_something_scheduled():
        label = "Player_something_scheduled"

        conditions = [
            "time_index in Player.schedule.keys()"]

        priority = 99
        repeatable = True

        waiting = True
        traveling = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable, waiting = waiting, traveling = traveling)

label Player_something_scheduled:
    $ instructions = Player.schedule[time_index]
    $ del Player.schedule[time_index]

    while instructions:
        if isinstance(instructions[0], list):
            if eval(instructions[0][0]):
                $ exec(instructions[0][1])
        
        $ instructions.remove(instructions[0])

    return