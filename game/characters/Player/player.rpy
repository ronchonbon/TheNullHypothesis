init -2:
    
    define Player_color = "#000000"
    define ch_Player = Character("Player")

init -2 python:

    def create_Player(first_name, last_name):
        Player = PlayerClass(
            first_name, last_name,
            voice = ch_Player)

        Player.call_sign = "Null"
            
        return Player