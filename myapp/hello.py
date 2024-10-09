import fire

def hello(name="World"):
  return "aHello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
