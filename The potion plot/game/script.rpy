# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Things are in debug mode for now, so we don't have to play through everything to access a given chapter"

    e "Just select the chapter you want to access"

    menu:

        "Intro":
            jump intro

        "First monologue":
            jump first_monologue

        "Friendly argument":
            jump friendly_argument

        "Enthusiastic friend":
            jump enthusiastic_friend

        "Shy costumer":
            jump shy_costumer

        "Epilogue":
            jump epilogue

        "Potion minigame":
            jump potions

        "None":
            return


    return

label intro:

    scene bg room

    "This is the intro chapter"

    jump start

label first_monologue:

    scene bg room

    "This is the first monologue chapter"

    jump start

label friendly_argument:

    scene bg room

    "This is the friendly argument chapter"

    jump start

label enthusiastic_friend:

    scene bg room

    "This is the enthusiastic friend chapter"

    jump start

label shy_costumer:

    scene bg room

    "This is the shy costumer chapter"

    jump start

label epilogue:

    scene bg room

    "This is the epilogue chapter"

    jump start

label potions:

    $ inventory_list = [Ingredient(), Ingredient(name="Blob"), Ingredient(description="Another potion ingredient")]
    $ cauldron_content = []
    show screen inventory(inventory_list)
    show screen cauldron(cauldron_content)

    "This is the potion minigame"

    # This should be done via "ToggleScreen" in the action to close the minigame
    hide screen inventory
    hide screen cauldron

    jump start
