# app.py
def greet(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    return f"Hello, {name}!"

def farewell(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    try:
        print(greet("DevOps"))
        print(farewell("DevOps"))
    except TypeError as e:
        print(f"Error: {e}")
