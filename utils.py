def isXorO_Time(whichPlayer: int):
    if whichPlayer % 2 == 0:
        return "x"
    if not whichPlayer % 2 == 0:
        return "o"


def isButtonEmpty(buttontext: str):
    if buttontext == " ":
        return True
    return False
