def tupleToDict(tuple: tuple, names: list[str]):
  print("start")
  i = 0
  result = dict()
  while( i < len(names)):
    result[names[i]] = tuple[i]
    i += 1
  return result