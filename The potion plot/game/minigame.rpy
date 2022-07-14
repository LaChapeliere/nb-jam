## Potion minigame #############################################################
##
## Classes and screen for the potion minigame
##

init python:
    import renpy.store as store

    class Ingredient(store.object):
        def __init__(self, name="Ingredient", description="A potion ingredient", icon="add_ingredient_%s.png", effect=[]):
            self.name = name
            self.description = description
            self.icon = icon
            self.effect = []

        def add_to_cauldron(self, workshop):
            workshop.add_to_cauldron(self)

    class Workshop(store.object):
        # Class attributes
        inventory = [
            Ingredient(),
            Ingredient(name="Blob"),
            Ingredient(description="Another potion ingredient")]
        capacity = 5

        def __init__(self, goal="", goal_description="", cauldron=[], potion_description=""):
            self.goal = goal
            self.goal_description = goal_description
            self.cauldron = cauldron
            self.potion_description = potion_description

        def add_to_cauldron(self, ingredient):
            self.cauldron.append(ingredient)


screen workshop(workshop):
    use inventory(workshop.inventory)
    use cauldron(workshop.cauldron)

    # If the cauldron is full
    if len(workshop.cauldron) == workshop.capacity:
        #$ active_inventory = False
        #$ renpy.restart_interaction()
        timer 1.0 action Jump("potions_end")

## Ingredient inventory screens #################################################
##
## Those screens are used to display the ingredients for the potion minigame.
##

screen inventory_item(ingredient):
    hbox:
        spacing 10

        text ingredient.name
        text ingredient.description
        imagebutton:
            auto ingredient.icon
            # The ingredient icons are made inactive when the cauldron is full
            action If(len(workshop.cauldron)<workshop.capacity-1, true=Function(ingredient.add_to_cauldron, workshop), false=[Function(ingredient.add_to_cauldron, workshop), SetVariable("active_inventory", False)])
            sensitive active_inventory

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
