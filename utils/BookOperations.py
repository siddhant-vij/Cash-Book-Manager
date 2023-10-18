import os


def addNewBook(name):
    if not os.path.exists("data/" + name + ".csv"):
        with open("data/" + name + ".csv", "w") as f:
            f.write("")


def deleteBook(name):
    if os.path.exists("data/" + name + ".csv"):
        os.remove("data/" + name + ".csv")


def renameBook(name, newName):
    if os.path.exists("data/" + name + ".csv"):
        os.rename("data/" + name + ".csv", "data/" + newName + ".csv")
