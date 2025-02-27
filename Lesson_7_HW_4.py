def common_elements():
      x = set(range(0, 101, 3))
      y = set(range(0,101,5))
      print(x)
      print(y)
      union_x_y = x.intersection(y)
      print(union_x_y)
common_elements()