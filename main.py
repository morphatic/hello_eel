"""
Hello Eel backend code
"""

# import required libraries
import eel


@eel.expose
def sayHello(name):
    return f"Hello, {name}!"


# initialize and start eel app
eel.init("web")
eel.start("index.html")
