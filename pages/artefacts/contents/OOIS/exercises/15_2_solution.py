import turtle

class Point:
  """Represents a point. 

    attributes: x and y.
    """

class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

class Circle:
  """Represents a circle. 

    attributes: center and radius.
    """
    
def point_in_circle(point, circle):
  x_diff = (point.x - circle.center.x) * (point.x - circle.center.x)
  y_diff = (point.y - circle.center.y) * (point.y - circle.center.y)
  return x_diff + y_diff < circle.radius * circle.radius

def rect_in_circle(rectangle, circle):
  top_left_point_of_the_rectangle = Point()
  top_left_point_of_the_rectangle.x = rectangle.corner.x
  top_left_point_of_the_rectangle.y = rectangle.corner.y
  
  top_right_point_of_the_rectangle = Point()
  top_right_point_of_the_rectangle.x = rectangle.corner.x + rectangle.width
  top_right_point_of_the_rectangle.y = rectangle.corner.y
  
  bottom_left_point_of_the_rectangle = Point()
  bottom_left_point_of_the_rectangle.x = rectangle.corner.x
  bottom_left_point_of_the_rectangle.y = rectangle.corner.y + rectangle.height
  
  bottom_right_point_of_the_rectangle = Point()
  bottom_right_point_of_the_rectangle.x = rectangle.corner.x + rectangle.width
  bottom_right_point_of_the_rectangle.y = rectangle.corner.y + rectangle.height
  
  return (
    point_in_circle(top_left_point_of_the_rectangle, circle) and
    point_in_circle(top_right_point_of_the_rectangle, circle) and
    point_in_circle(bottom_left_point_of_the_rectangle, circle) and
    point_in_circle(bottom_right_point_of_the_rectangle, circle)
  )

def rect_circle_overlap(rectangle, circle):
  top_left_point_of_the_rectangle = Point()
  top_left_point_of_the_rectangle.x = rectangle.corner.x
  top_left_point_of_the_rectangle.y = rectangle.corner.y
  is_top_left_point_inside_circle = point_in_circle(top_left_point_of_the_rectangle, circle)
  
  top_right_point_of_the_rectangle = Point()
  top_right_point_of_the_rectangle.x = rectangle.corner.x + rectangle.width
  top_right_point_of_the_rectangle.y = rectangle.corner.y
  is_top_right_point_inside_circle = point_in_circle(top_right_point_of_the_rectangle, circle)
  
  bottom_left_point_of_the_rectangle = Point()
  bottom_left_point_of_the_rectangle.x = rectangle.corner.x
  bottom_left_point_of_the_rectangle.y = rectangle.corner.y + rectangle.height
  is_bottom_left_point_inside_circle = point_in_circle(bottom_left_point_of_the_rectangle, circle)
  
  bottom_right_point_of_the_rectangle = Point()
  bottom_right_point_of_the_rectangle.x = rectangle.corner.x + rectangle.width
  bottom_right_point_of_the_rectangle.y = rectangle.corner.y + rectangle.height
  is_bottom_right_point_inside_circle = point_in_circle(bottom_right_point_of_the_rectangle, circle)
  
  return (
    is_top_left_point_inside_circle or 
    is_top_right_point_inside_circle or
    is_bottom_left_point_inside_circle or
    is_bottom_right_point_inside_circle
  )

def draw_circle(turtle, circle):
  """Draws a rectangle.
    t: Turtle
    rect: Rectangle
    """
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.setheading(0)
    t.pd()

    for length in rect.width, rect.height, rect.width, rect.height:
        t.fd(length)
        t.rt(90)

def main():
#     box = Rectangle()
#     box.width = 100.0
#     box.height = 200.0
#     box.corner = Point()
#     box.corner.x = 50.0
#     box.corner.y = 50.0

#     circle = Circle
#     circle.center = Point()
#     circle.center.x = 150.0
#     circle.center.y = 100.0
#     circle.radius = 75.0

#     print(point_in_circle(box.corner, circle))
#     print(rect_in_circle(box, circle))
#     print(rect_circle_overlap(box, circle))
  bob = turtle.Turtle()

  # draw the axes
  length = 400
  bob.fd(length)
  bob.bk(length)
  bob.lt(90)
  bob.fd(length)
  bob.bk(length)

  # draw a rectangle
  box = Rectangle()
  box.width = 100.0
  box.height = 200.0
  box.corner = Point()
  box.corner.x = 50.0
  box.corner.y = 50.0

  draw_rect(bob, box)

  # draw a circle
  circle = Circle
  circle.center = Point()
  circle.center.x = 150.0
  circle.center.y = 100.0
  circle.radius = 75.0

  draw_circle(bob, circle)

  # wait for the user to close the window
  turtle.mainloop()


if __name__ == '__main__':
    main()
