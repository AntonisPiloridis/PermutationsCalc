# pcomp 1.1.0 - https://pypi.org/project/pcomp/1.1.0/
# modified
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

def area(iterable,length):
    if iterable and length:
        return pow(len(iterable),length)
    return None


def pc(iterable,length):
    if iterable and length:
        power = area(iterable,length)
        temp_list = [[None]*length for i in range(power)]
        for i in range(-1,length*-1-1,-1): # negative i
            change = len(iterable)**abs(i+1)
            counter = 0
            index = 0
            for j in range(power):
                if counter != change:
                    temp_list[j][i] = iterable[index]
                    counter += 1
                else:
                    counter = 0
                    if index<len(iterable)-1:
                        index += 1
                    else:
                        index = 0
                    temp_list[j][i] = iterable[index]
                    counter += 1
            result = temp_list
        return result
    return None

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑