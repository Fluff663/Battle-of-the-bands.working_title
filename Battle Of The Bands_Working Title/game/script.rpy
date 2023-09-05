# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define test1 = Character("Power")


# The game starts here.

#say hide after showing an image! oe ti will overlay
label start:
    show evilwoman

    test1 "Hello! This is a renpy test"

    hide evilwoman

    show power

    test1 "This should change image!"

    hide power

    show man

    test1 "Hewwo!"


    return
