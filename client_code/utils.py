

_id = 0
_prefix = "m3-"

def gen_id():
    global _id
    _id += 1
    return f":{_prefix}{_id}:"