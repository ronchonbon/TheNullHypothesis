init -2:

    default black_screen = False

    default focused_Girl = None

    default Party = []
    default Contacts = []
    default Keys = []
    default Partners = []

    define stage_far_far_left = 0.15
    define stage_far_left = 0.25
    define stage_left = 0.35
    define stage_center = 0.5
    define stage_right = 0.65
    define stage_far_right = 0.75
    define stage_far_far_right = 0.85
    define stage_far_far_far_right = 0.95

    define time_options = ["morning", "midday", "evening", "night", "late night"]
    define week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    default lighting = "day"

    define public_locations = [
        "bg_bar", 
        "bg_campus", 
        "bg_classroom", 
        "bg_danger", 
        "bg_entrance", 
        "bg_girls_hallway", 
        "bg_hallway", 
        "bg_lockers",
        "bg_mall", 
        "bg_movies", 
        "bg_pool", 
        "bg_restaurant", 
        "bg_study"]

    define location_names = {
        "bg_bar": "Bar",
        "bg_campus": "Campus",
        "bg_Charles": "[Charles.name]'s Room",
        "bg_classroom": "Classroom",
        "bg_danger": "Danger Room",
        "bg_door": "Hall",
        "bg_entrance": "Mansion Entrance",
        "bg_girls_hallway": "Hall",
        "bg_hallway": "Hall",
        "bg_Jean": "[Jean.name]'s Room",
        "bg_Kurt": "[Kurt.name]'s Room",
        "bg_Laura": "[Laura.name]'s Room",
        "bg_mall": "Bayville Mall",
        "bg_movies": "Movie Theater",
        "bg_Player": "[Player.first_name]'s Room",
        "bg_pool": "Pool",
        "bg_restaurant": "Restaurant",
        "bg_Rogue": "[Rogue.name]'s Room",
        "bg_lockers": "Locker Room",
        "bg_Ororo": "[Ororo.name]'s Room",
        "bg_study": "[Charles.name]'s Study",
        "bg_town": "Town",
        "hold": "Away"}

    define map_names = {
        "bg_bar": "Bar",
        "bg_campus": "Grounds",
        "bg_Charles": "[Charles.name]'s Room",
        "bg_classroom": "Classroom",
        "bg_danger": "Danger Room",
        "bg_door": "Hall",
        "bg_entrance": "Entrance",
        "bg_girls_hallway": "Hall",
        "bg_hallway": "Hall",
        "bg_Kurt": "",
        "bg_mall": "Mall",
        "bg_movies": "Theater",
        "bg_pool": "Pool",
        "bg_restaurant": "Restaurant",
        "bg_lockers": "Locker Room",
        "bg_study": "[Charles.name]'s Study",
        "bg_town": "Town"}

    define location_conversational_names = {
        "bg_bar": "the bar",
        "bg_campus": "front of the mansion",
        "bg_Charles": "[Charles.name]'s room",
        "bg_classroom": "the classroom",
        "bg_danger": "the Danger Room",
        "bg_entrance": "the main entrance",
        "bg_girls_hallway": "the hall",
        "bg_hallway": "the hall",
        "bg_Jean": "[Jean.name]'s room",
        "bg_shower_Jean": "[Jean.name]'s room",
        "bg_Kurt": "[Kurt.name]'s room",
        "bg_Laura": "[Laura.name]'s room",
        "bg_shower_Laura": "[Laura.name]'s room",
        "bg_mall": "the mall",
        "bg_movies": "the movie theater",
        "bg_Player": "my room",
        "bg_shower_Player": "my room",
        "bg_pool": "the pool",
        "bg_restaurant": "the restaurant",
        "bg_Rogue": "[Rogue.name]'s room",
        "bg_shower_Rogue": "[Rogue.name]'s room",
        "bg_lockers": "the locker room",
        "bg_Ororo": "[Ororo.name]'s room",
        "bg_shower_Ororo": "[Ororo.name]'s room",
        "bg_study": "[Charles.name]'s study"}

    default lights_on = True
    default door_locked = False

    default danger_red_alert = False

    default showering = False
    default shower_open = True
    default shower_steam = False

    default campus_grass_cut = False

    default mall_damage = False

    default infirmary_bed = False
    default infirmary_in_bed = False
    default infirmary_screen1 = False
    default infirmary_screen2 = False
    default infirmary_screen3 = False

    define subtle_screenshake = Move((0, 2), (0, -2), 0.10, bounce = True, repeat = True, delay = 0.25)
    define small_screenshake = Move((0, 10), (0, -10), 0.10, bounce = True, repeat = True, delay = 0.275)
    define big_screenshake = Move((0, 20), (0, -20), 0.10, bounce = True, repeat = True, delay = 0.5)
    define orgasm_shake = Move((0, 10), (0, -10), 0.10, bounce = True, repeat = True, delay = 0.275)
    define fast_dissolve = Dissolve(1.0)
    define faster_dissolve = Dissolve(0.5)
    define fastest_dissolve = Dissolve(0.1)
    define rumble = Move((0, 4), (0, -4), 0.05, bounce = True, repeat = True, delay = 3.5)
    define harden = ImageDissolve("images/effects/harden.webp", 0.5, 8)
    define shapeshift = ImageDissolve("images/effects/shapeshift.webp", 1.0, 8)

    default season_completed = False

    define chapter_names = ["P", "I", "II", "III", "IV", "V", "VI"]