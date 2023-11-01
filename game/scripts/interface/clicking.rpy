screen disable_click(time):
    on "show" action SetVariable("_skipping", False)
    on "hide" action SetVariable("_skipping", True)

    timer time action Hide("disable_click")

    key "mouseup_1" action NullAction()