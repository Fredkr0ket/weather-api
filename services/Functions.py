def tupleToDict(tuple: tuple, names: list[str]):
    i = 0
    result = dict()
    while( i < len(names)):
        result[names[i]] = tuple[i]
        i += 1
    return result

def checkItems(item1, item2):
    if item1 == None and item2 == None:
        return None
    if item1 and item2 == None:
        return item1
    return {"value1": item1, "value2": item2}
    