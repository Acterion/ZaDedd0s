def read_file(path):
    with open(path, "r") as f:
        return f.read()


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
