input("Welcome to mad libs! Type any key to begin.\n")

a1 = input("Adjective: ")
a2 = input("Another Adjective: ")
n1 = input("Noun: ")
n2 = input("Another Noun: ")
v1 = input("Verb: ")
v2 = input("Another Verb: ")
v3 = input("Verb (Past Tense): ")
animal = input("Animal: ")
place = input("Place: ")
adv = input("Adverb: ")

story = f"""
Once upon a time, in a {a1} land far far away, there was a {n1} who loved to {v1} every day. One day, it met a {a2} {n2} that could {v2} like a {animal}. Together, they traveled to {place} and {v3} {adv} ever after.
"""

printstory = input("Would you like to see your story? (y/n)")

if printstory == "y":
    print(story)