class Circle:
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    # todo

class Square:
  def __init__(self, side):
    self.side = side

  def __str__(self):
    # todo


class ColoredShape:
  def __init__(self, shape, color):
    self.color = color
    self.shape = shape

  def resize(self, factor):
    # todo
    # note that a Square doesn't have resize()

  def __str__(self):
    # todo