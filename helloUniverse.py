def hello(who):
  """Print "Hi to" who and return None"""
  if who == None:
    who = "UNIVERSE!"

  print("Hi to you, " + who)


hello("moo")
hello("foo")
hello("poo")
hello("too")
hello("yoo")
hello(None)
