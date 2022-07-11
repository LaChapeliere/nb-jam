## Potion minigame #############################################################
##
## Classes and screen for the potion minigame
##

init python:
    import renpy.store as store

    class Ingredient(store.object):
        def __init__(self, name="Ingredient", description="A potion ingredient", icon="add_ingredient_%s.png"):
            self.name = name
            self.description = description
            self.icon = icon
            self.available = True

        def add_to_cauldron(self, cauldron_content):
            cauldron_content.append(self)

## Ingredient inventory screens #################################################
##
## Those screens are used to display the ingredients for the potion minigame.
##

screen inventory_item(ingredient):
    hbox:
        spacing 10

        text ingredient.name
        text ingredient.description
        imagebutton auto ingredient.icon action Function(ingredient.add_to_cauldron, cauldron_content)

screen inventory(inventory_list):
    vpgrid:
        cols 1
        spacing 10
        draggable True
        mousewheel True

        scrollbars "vertical"

        # Since we have scrollbars, this positions the side, rather than
        # the vpgrid.
        xalign 0.1 yalign 0.1

        for item in inventory_list:
            use inventory_item(item)

## Cauldron screens #################################################
##
## Those screens are used to display the progress of the potion minigame.
##

screen cauldron_item(ingredient):
    hbox:
        spacing 10

        text ingredient.name
        text ingredient.description
        imagebutton auto ingredient.icon action NullAction


screen cauldron(cauldron_content):
    vbox:
        xalign 0.7 yalign 0.1

        for item in cauldron_content:
            use cauldron_item(item)
