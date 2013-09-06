def load_temp(f_name):
    d = {}
    f = open(f_name)
    for line in f:
        key = line.split(":")[0].strip('\n')
        value = line.split(":")[1].strip('\n')
        d[key] = value
    return d


def save_temp(f_name, d):
    f = open(f_name, 'w')
    for key, value in d.iteritems():
        f.write(key + ":" + value + "\n")
