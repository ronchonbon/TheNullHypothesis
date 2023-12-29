init -5 python:

    import pygame
    import math

    def get_mouse_position():
        return renpy.get_mouse_pos()
 
    class TrackCursor(renpy.Displayable):
        def __init__(self, child, paramod, **kwargs):
            super(TrackCursor, self).__init__()
 
            self.child = renpy.displayable(child)
            self.x = 0
            self.y = 0
            self.actual_x = 0
            self.actual_y = 0
 
            self.paramod = paramod
            self.last_st = 0
 
        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            
            if self.x is not None:
                st_change = st - self.last_st
 
                self.last_st = st
                self.actual_x = math.floor(self.actual_x + ((self.x - self.actual_x)*(st_change))*self.paramod)
                self.actual_y = math.floor(self.actual_y + ((self.y - self.actual_y)*(st_change))*self.paramod)
 
                cr = renpy.render(self.child, width, height, st, at)
                rv.blit(cr, (self.actual_x, self.actual_y))
 
            renpy.redraw(self, 0)

            return rv
 
        def event(self, ev, x, y, st):
            hover = ev.type == pygame.MOUSEMOTION
            click = ev.type == pygame.MOUSEBUTTONDOWN

            if hover:
                if (x != self.x) or (y != self.y) or click:
                    self.x = -x/self.paramod
                    self.y = -y/self.paramod