def hello():
def pack(arg1, arg2, arg3):
  my_list = [arg1, arg2, arg3]
  return my_list

def eat_lunch():

  def eat_lunch(lunchbox):
    if len(lunchbox) == 0:
      print("my lunchbox is empty!")
      else:
        print("First I eat", lunchbox[0])
        for food in lunchbox[1:]:
          print("Next I eat", food)

          my_lunchbox = ["sansdwich", "chips", "apple"]
            eat_lunch(my_lunchbox)
