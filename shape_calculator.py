class Rectangle:
  
  def __init__(self, w, h):
    "Initialize a rectangle with given width and height"
    self.width = int(w)
    self.height = int(h)

  def __repr__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
  
  def set_width(self, x):
    """Set width of rectangle instance"""
    self.width = int(x)
    
  def set_height(self, y):
    """Set height of rectangle instance"""
    self.height = int(y)
    
  def get_area(self):
    """Return area of rectangle instance"""
    area = self.width * self.height
    return area

  def get_perimeter(self):
    """Return perimeter of rectangle instance"""
    perimeter = (self.width * 2) + (self.height * 2)
    return perimeter

  def get_diagonal(self):
    """Return the diagonal length of rectangle"""
    diag = (float(self.width ** 2) + float(self.height ** 2)) ** .5
    
    return diag

  def get_picture(self):
      """Draw rectangle with *"""

      if self.width > 50 or self.height > 50:
          return "Too big for picture."
      else:
          picture_raw = []
          lines = ('*' * self.width) + '\n'
          for p in range(self.height):
              picture_raw.append(lines)
          picture = "".join(picture_raw)
          return picture

  def get_amount_inside(self, shape):
    """How many "shape" can fit inside parent shape without rotation"""
  # determine width and height of passed shape
    shape_w, shape_h = shape.width, shape.height
    
    if shape_w > self.width or shape_h > self.height:
      return 0
    else:
      n_w = self.width // shape_w
      n_h = self.height // shape_h
      amount = (n_w * n_h)
      
      return amount
      
      
      

class Square(Rectangle):
  """Subclass of rectangle"""
 
  def __init__(self, s):
    self.width = int(s)
    self.height = int(s)
    
  def __repr__(self):
    return f'Square(side={self.width})'
  
  def set_side(self, side):
    self.width = int(side)
    self.height = int(side)

  def set_width(self, x):
    self.width = int(x)
    self.height = int(x)

  def set_height(self, y):
    self.width = int(y)
    self.height = int(x)
  