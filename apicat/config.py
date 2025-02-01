import tomllib

def read(file_name):
    with open(file_name, "rb") as f:
        cfg = tomllib.load(f)
        return cfg