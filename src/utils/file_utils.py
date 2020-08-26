from pathlib import Path


def read_file(path):
    with open(path, "r") as f:
        return f.read()


def read_json(path):
    file = Path(path)
    if file.exists():
        with open(path, "r") as f:
            return f.read()
    return '{}'


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
