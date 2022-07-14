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
            Ingredient(name="Essence of man", description="Make a very manly man. Whatever that means.", effect=["man"]),
            Ingredient(name="Essence of woman", description="Make a truly womanly woman. Whatever that means.", effect=["woman"]),
            Ingredient(description="Make the drinker identifies with a gender outside the man/woman continuum. Whatever that means.", effect=["enby"]),
            Ingredient(name="Moon shard", description="Like the moon or the ocean, gender will gently ebb and flow.", effect=["fluidity"]),
            Ingredient(name="A remnant of something to be", description="Nothing endures but change, Heraclitus said, so best have an ever-transforming gender...", effect=["fluidity", "fluidity", "fluidity"]),
            Ingredient(name="Taboo bag", description="Create an rejection reaction to specific words. Primed for the 'it' pronoun set.", effect=["lang"]),
            Ingredient(name="Taboo bag", description="Create an rejection reaction to specific words. Primed for the 'he' pronoun set.", effect=["lang"]),
            Ingredient(name="Taboo bag", description="Create an rejection reaction to specific words. Primed for the 'she' pronoun set.", effect=["lang"]),
            Ingredient(name="Taboo bag", description="Create an rejection reaction to specific words. Primed for the 'they' pronoun set.", effect=["lang"]),
            Ingredient(name="Taboo bag", description="Create an rejection reaction to specific words. Primed for the 'ze' pronoun set.", effect=["lang"]),
            Ingredient(name="Taboo bag", description="Create an rejection reaction to specific words. Primed for the 'fae' pronoun set.", effect=["lang"]),
            Ingredient(name="Taboo bag", description="Create an rejection reaction to specific words. Primed for 'enby' and associated gender-neutral terms.", effect=["lang"]),
            Ingredient(name="Taboo bag", description="Create an rejection reaction to specific words. Primed for 'woman' and associated gender-neutral terms.", effect=["lang"]),
            Ingredient(name="Taboo bag", description="Create an rejection reaction to specific words. Primed for 'man' and associated gender-neutral terms.", effect=["lang"]),
            Ingredient(name="Language mint", description="Create an identifying reaction to specific words. Primed for the 'it' pronoun set", effect=["lang"]),
            Ingredient(name="Language mint", description="Create an identifying reaction to specific words. Primed for the 'he' pronoun set", effect=["lang"]),
            Ingredient(name="Language mint", description="Create an identifying reaction to specific words. Primed for the 'she' pronoun set", effect=["lang"]),
            Ingredient(name="Language mint", description="Create an identifying reaction to specific words. Primed for the 'they' pronoun set", effect=["lang"]),
            Ingredient(name="Language mint", description="Create an identifying reaction to specific words. Primed for the 'ze' pronoun set", effect=["lang"]),
            Ingredient(name="Language mint", description="Create an identifying reaction to specific words. Primed for the 'fae' pronoun set", effect=["lang"]),
            Ingredient(name="Language mint", description="Create an identifying reaction to specific words. Primed for the 'xe' pronoun set", effect=["lang"]),
            Ingredient(name="Language mint", description="Create an identifying reaction to specific words. Primed for 'enby' and associated gender-neutral terms.", effect=["lang"]),
            Ingredient(name="Language mint", description="Create an identifying reaction to specific words. Primed for 'woman' and associated gender-neutral terms.", effect=["lang"]),
            Ingredient(name="Language mint", description="Create an identifying reaction to specific words. Primed for 'man' and associated gender-neutral terms.", effect=["lang"]),
            Ingredient(description="Having breasts is gender affirming.", effect=["body"]),
            Ingredient(description="Having abundant body hair is gender affirming.", effect=["body"]),
            Ingredient(description="Having limited body hair is gender affirming.", effect=["body"]),
            Ingredient(description="Having a penis is gender affirming.", effect=["body"]),
            Ingredient(description="Having a vagina is gender affirming.", effect=["body"]),
            Ingredient(description="Menstruating creates gender euphoria.", effect=["body"]),
            Ingredient(description="Tie gender to a brawny body image.", effect=["body"]),
            Ingredient(description="Tie gender to a soft and curvy body image.", effect=["body"]),
            Ingredient(description="Imagining one's body with no genitals is gender affirming.", effect=["body"]),
            Ingredient(description="Having breasts (or thinking about them) triggers gender dysphoria.", effect=["body"]),
            Ingredient(description="Having body hair (or thinking about it) triggers gender dysphoria.", effect=["body"]),
            Ingredient(description="Having little to no body hair (or thinking about it) triggers gender dysphoria.", effect=["body"]),
            Ingredient(description="Having a penis (or thinking about it) triggers gender dysphoria.", effect=["body"]),
            Ingredient(description="Having a vagina (or thinking about it) triggers gender dysphoria.", effect=["body"]),
            Ingredient(description="Menstruating (or thinking about it) triggers gender dysphoria.", effect=["body"]),
            Ingredient(description="The drinker will feel at ease wearing any clothes they like, no matter how they are traditionally gendered.", effect=["express"]),
            Ingredient(description="The drinker will develop a love for traditionally feminine clothing.", effect=["express"]),
            Ingredient(description="The drinker will develop a love for traditionally masculine clothing.", effect=["express"]),
            Ingredient(description="The drinker will reject all traditionally gendered clothing.", effect=["express"]),
            Ingredient(description="The drinker will particularly enjoy traditionally feminine activities.", effect=["express"]),
            Ingredient(description="The drinker will particularly enjoy traditionally masculine activities.", effect=["express"]),
            Ingredient(description="The drinker will feel at home with traditionally feminine behaviours and mannerisms.", effect=["express"]),
            Ingredient(description="The drinker will feel at home with traditionally masculine behaviours and mannerisms.", effect=["express"]),
            Ingredient(description="Social perception is important. The drinker will need people to see them first as a woman.", effect=["social", "social"]),
            Ingredient(description="Social perception is important. The drinker will need people to see them first as a man.", effect=["social", "social"]),
            Ingredient(description="Social perception is important. The drinker will need people to see them first as a person.", effect=["social", "social"]),
            Ingredient(description="Social perception is important. The drinker will need people to see them first as a enby.", effect=["social", "social"])
            ]
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
        ysize 60
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
        xalign 0.05 yalign 0.1

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
