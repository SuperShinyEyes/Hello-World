# http://www.codeskulptor.org/#user40_LmVKuQyuvY_3.py

import simplegui

DIMENSION = WIDTH, HEIGHT = (500, 300)
CENTER = tuple(i/2 for i in DIMENSION)     # Must be list for moving balls

class Ball(object):
  """docstring for """
  def __init__(self, radius, color, pos=list(CENTER)):
    self.color = color
    self.radius = radius
    self.pos = pos
    self.horizontal_speed = 6
    self.vertical_speed = 3

  def draw(self, canvas):
    canvas.draw_circle(self.pos, self.radius, 10, self.color, self.color)

  def reset(self):
    self.pos = list(CENTER)

  def hit(self):
    edge_right = self.pos[0] + self.radius
    edge_left = self.pos[0] - self.radius
    ## ball hits the right bar
    if edge_right >= right.face and (self.pos[1] > right.top and self.pos[1] < right.bottom):
      return True
    elif edge_left <= left.face and (self.pos[1] > left.top and self.pos[1] < left.bottom):
      return True

  def is_out_on_right(self):
    return self.pos[0] > WIDTH

  def is_out_on_left(self):
    return self.pos[0] < 0

  def move(self, canvas):
    if self.is_out_on_right():
      self.reset()
      left.score += 1
      left.update_length(20)
      right.update_length(-20)
    elif self.is_out_on_left():
      self.reset()
      right.score += 1
      right.update_length(20)
      left.update_length(-20)

    if self.hit():
      self.horizontal_speed = -self.horizontal_speed
    # if self.pos[0] >= WIDTH - self.radius or self.pos[0] <= 0 + self.radius:
    #   self.horizontal_speed = -self.horizontal_speed
    if self.pos[1] >= HEIGHT - self.radius or self.pos[1] <= 0 + self.radius:
      self.vertical_speed = -self.vertical_speed
    self.pos[0] += self.horizontal_speed
    self.pos[1] += self.vertical_speed

    self.draw(canvas)

class Bar(object):
  """docstring for bar"""
  thickness = 10
  def __init__(self, side, color, length):
    self.side = side
    self.color = color
    self.length = length
    self.face = self.get_face()
    self.coordinates = self.get_coordinates()
    self.top = self.coordinates[0][1]
    self.bottom = self.coordinates[-1][1]
    self.velocity = 0
    self.score = 0

  def update_length(self, change):
    self.length += change
    self.coordinates[0][1] -= change/2
    self.coordinates[1][1] -= change/2
    self.coordinates[2][1] += change/2
    self.coordinates[3][1] += change/2

  def update_top_bottom(self):
    self.top = self.coordinates[0][1]
    self.bottom = self.coordinates[-1][1]

  def get_face(self):
    ''' The x coordinate of the side which hits a ball.
        i.e., The side which faces the opponent. '''
    if self.side == 'left':
      return Bar.thickness
    elif self.side == 'right':
      return WIDTH - Bar.thickness

  def get_coordinates(self):
    top = (HEIGHT- self.length)/2
    bottom = (HEIGHT + self.length)/2
    if self.side == 'left':
      return [[0, top],[self.face, top],[self.face, bottom],[0, bottom]]
    elif self.side == 'right':
      return [[self.face, top],[WIDTH, top],[WIDTH, bottom],[self.face, bottom]]

  def draw(self, canvas):
    self.update_top_bottom()
    if self.can_move():
      self.move()
    canvas.draw_polygon(self.coordinates, 12, self.color)
    canvas.draw_line([WIDTH/2, 0], [WIDTH/2, HEIGHT], 3, 'White')

  def is_in_boundary(self):
    return self.top > 0 and self.bottom < HEIGHT

  def can_move(self):
    ## Hits the bottom
    if self.velocity > 0 and self.bottom >= HEIGHT:
      return False
    ## Hits the ceiling
    elif self.velocity < 0 and self.top <= 0:
      return False
    else:
      return True

  def move(self):
    for pos in self.coordinates:
      pos[1] += self.velocity

def is_game_over():
  if right.top > right.bottom:
    boolean = True
    message = "Left won!"
  elif left.top > left.bottom:
    boolean = True
    message = "Right won!"
  else:
    boolean = False
    message = ""
  return boolean, message

# Handler to draw on canvas
def draw(canvas):
  gameover_boolean, message = is_game_over()
  if gameover_boolean:
    canvas.draw_text(str(message), [WIDTH*.5,112], 88, "White")
  green.move(canvas)
  left.draw(canvas)
  right.draw(canvas)
  canvas.draw_text(str(left.score), [WIDTH*.35, 62], 48, "Red")
  canvas.draw_text(str(right.score), [WIDTH*.70,62], 48, "Red")

def keydown(key):
  if key == simplegui.KEY_MAP['down']:
    right.velocity = 5
  elif key == simplegui.KEY_MAP['up']:
    right.velocity = -5
  elif key == simplegui.KEY_MAP['s']:
    left.velocity = 5
  elif key == simplegui.KEY_MAP['w']:
    left.velocity = -5

def keyup(key):
  if key == simplegui.KEY_MAP['down']:
    right.velocity = 0
  elif key == simplegui.KEY_MAP['up']:
    right.velocity = 0
  elif key == simplegui.KEY_MAP['s']:
    left.velocity = 0
  elif key == simplegui.KEY_MAP['w']:
    left.velocity = 0

green = Ball(20, 'green')
right = Bar('right', 'white', 60)
left = Bar('left', 'white', 60)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Start the frame animation
frame.start()
