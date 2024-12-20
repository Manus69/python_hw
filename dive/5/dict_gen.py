
def _dict_gen(names, salary, bonus):
    return {names[k]: salary[k] * float(bonus[k].strip('%')) / 100 for k in range(len(names))}

def test():
    print(_dict_gen(['a', 'b', 'c'], [1, 2, 3], ["1%", "2%", "3%"]))

test()