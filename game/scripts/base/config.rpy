define config.save_directory = "TheNullHypothesis"

define config.gc_thresholds = (2500, 10, 10)
define config.idle_gc_count = 250

init python:

    config.name = _("The Null Hypothesis")
    config.version = "0.3a"

    config.developer = "auto"

    config.screen_width = 1920
    config.screen_height = 1080
    config.default_fullscreen = True

    if renpy.android:
        config.image_cache_size = 75
    else:
        config.image_cache_size = 200

    config.cache_surfaces = False
    config.optimize_texture_bounds = True
    config.max_fit_size = 8000
    
    config.allow_underfull_grids = True

    config.narrator_menu = True

    # this really slows down the game, don't do it
    config.autosave_on_choice = False
    config.autosave_frequency = 100

    config.has_sound = True
    config.has_music = True
    config.has_voice = False

    config.window_icon = "images/interface/icon.webp"

    config.main_menu_music = "sounds/music/Main Theme.ogg"

    # config.mouse = {}
    # config.mouse['default'] = [("images/interface/cursor.webp", 0, 0)]

    config.thumbnail_width = 250
    config.thumbnail_height = 141

    config.layers = ["master", "cinematic", "filters", "interface", "effects", "transient", "screens", "overlay"]

    config.detached_layers += ["comic_cutout1", "comic_cutout2", "comic_cutout3", "comic_cutout4"]

    config.rollback_enabled = True
    config.rollback_length = 512
    config.hard_rollback_limit = 512

    config.default_music_volume = 0.4
    config.default_sfx_volume = 0.25
    
    config.keymap["rollback"] = ["any_K_PAGEUP", "any_KP_PAGEUP", "K_AC_BACK"]

    preferences.text_cps = 0
    preferences.afm_time = 10

    build.name = "TheNullHypothesis"

    build.classify("**.md", None)
    build.classify("**.bak", None)
    build.classify("LICENSE", None)

    build.classify("**.rpy", "archive")
    build.classify("**.rpyc", "archive")
    build.classify("**.ttf", "archive")
    build.classify("**.png", "archive")
    build.classify("**.webp", "archive")
    build.classify("**.ogg", "archive")

    build.documentation("*.html")
    build.documentation("*.txt")