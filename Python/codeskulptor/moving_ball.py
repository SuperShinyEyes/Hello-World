import simplegui

DIMENSION = WIDTH, HEIGHT = (500, 300)
CENTER = [i/2 for i in DIMENSION]     # Must be list for moving balls


class Ball(object):
  """docstring for """
  def __init__(self, radius, color, pos=CENTER):
    self.color = color
    self.radius = radius
    self.pos = pos

  def draw(self, canvas):
    canvas.draw_circle(self.pos, self.radius, 10, self.color, self.color)

def mouse_handler(pos):
  green.pos=pos

def draw(canvas):
  green.draw(canvas)

green = Ball(20, 'green')
frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_mousedrag_handler(mouse_handler)
frame.set_draw_handler(draw)

frame.start()
