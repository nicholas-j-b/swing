import pyglet
import numpy as np
import math
import itertools
import cfg
import random

class Line:
    def __init__(self, length, numSegments):
        self.length = length
        self.numSegments = numSegments
        self.points = np.array(list(itertools.chain.from_iterable([(cfg.windowWidthHalf 
                         + self.length * i, cfg.windowHeightHalf) for i in range(numSegments + 1)])), 
                               dtype="float32")
        self.cols = [random.randint(0,255) for i in range((numSegments + 1) * 3)]
        self.thetas = np.zeros(numSegments)
        
    def update(self):
        
        
        return self.points
        
                

class Window(pyglet.window.Window):
    def __init__(self):

        super().__init__(width=cfg.windowWidth, height=cfg.windowHeight, visible=True)
        fps = 30.0
        pyglet.clock.schedule_interval(self.update, 1.0/fps)
        pyglet.clock.set_fps_limit(fps)
        
        self.line = Line(cfg.lineLength, cfg.numSegments)

        self.pygline = pyglet.graphics.vertex_list(cfg.numSegments + 1,
            ('v2f/stream', self.line.points),
            ('c3B/static', self.line.cols)
        )
    
    
    def update(self, dt):
        self.pygline.vertices = self.line.update()
        
    
    def on_draw(self):
        self.clear()
        self.pygline.draw(pyglet.gl.GL_LINE_STRIP)











if __name__ == "__main__":
    window = Window()
    window.set_location(200, 10)
    pyglet.app.run()