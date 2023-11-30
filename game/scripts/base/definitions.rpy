init -2:

    default black_screen = False

    default focused_Companion = None

    default Present = []
    default left_Slot = None
    default middle_Slot = None
    default right_Slot = None
    default Offscreen = []

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

    default temp_Characters = [CompanionClass("Placeholder")]
    default temp_temp_Characters = [CompanionClass("Placeholder")]
    default temp_Clothes = [ClothingClass(None, "Placeholder", "Placholder", "placeholder", "placeholder", "placeholder", 0, 0, {})]
    default temp_Clothing_types = ["placeholder"]
    default temp_body_parts = ["placeholder"]