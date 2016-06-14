def hello(who):
  """Print "Hi to" who and return None"""
  if who == None:
    who = "UNIVERSE!"

  print("Hi to you, " + who)


hello("foo")
hello("moo")
hello("goo")
hello("poo")
hello("too")
hello("yoo")
hello(None)
