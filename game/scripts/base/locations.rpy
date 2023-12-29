init -2:
    
    default lighting = "day"

    define public_locations = [
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
        "bg_campus": "Grounds",
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

    define location_Slots = {
        "bg_campus": {
            "sidewalk": {
                "behavior": None,
                "anchor": [None, 1.0],
                "position": [0.65, 0.93],
                "zoom": 0.28,
                "layer": 4,
                "color_transform": None},
            "steps": {
                "behavior": None,
                "anchor": [None, 1.0],
                "position": [0.46, 0.785],
                "zoom": 0.1,
                "layer": 4,
                "color_transform": None}},
        "bg_classroom": {
            "podium": {
                "behavior": "teaching",
                "anchor": [None, 1.0],
                "position": [0.39, 0.67],
                "zoom": 0.3,
                "layer": 1,
                "color_transform": None}},
        "bg_danger": {
            "training1": {
                "behavior": "training",
                "anchor": [None, 1.0],
                "position": [0.225, 0.95],
                "zoom": 0.3,
                "layer": 4,
                "color_transform": shadow},
            "training2": {
                "behavior": "training",
                "anchor": [None, 1.0],
                "position": [0.65, 0.905],
                "zoom": 0.15,
                "layer": 4,
                "color_transform": shadow}},
        "bg_girls_hallway": {},
        "bg_hallway": {},
        "bg_mall": {
            "shopping": {
                "behavior": None,
                "anchor": [None, 1.0],
                "position": [0.85, 0.91],
                "zoom": 0.4,
                "layer": 4,
                "color_transform": None}},
        "bg_pool": {
            "left_edge": {
                "behavior": None,
                "anchor": [None, 1.0],
                "position": [0.4, 0.61],
                "zoom": 0.14,
                "layer": 4,
                "color_transform": None},
            "far_edge": {
                "behavior": None,
                "anchor": [None, 1.0],
                "position": [0.8, 0.55],
                "zoom": 0.11,
                "layer": 4,
                "color_transform": deep_shadow},
            "diving_board": {
                "behavior": None,
                "anchor": [None, 1.0],
                "position": [0.225, 0.99],
                "zoom": 0.3,
                "layer": 4,
                "color_transform": None},
            "right_edge": {
                "behavior": None,
                "anchor": [None, 1.0],
                "position": [0.85, 0.8],
                "zoom": 0.25,
                "layer": 4,
                "color_transform": deep_shadow}}}