import random

random_character_names = [
    "Max",
    "Eleanor",
    "Winston",
    "SpongeBob",
    "Hobbit",
    "Sauron",
    "Buzz",
    "Mulan",
    "Simba",
    "Nemo",
    "Mickey",
    "Bart",
    "Groot",
    "Frodo",
    "Elsa",
    "Sheldon",
    "Moriarty",
    "Hannibal",
    "Tyrion",
    "Gandalf",
    "Ezio",
    "Tifa",
    "Sora",
    "Dovahkiin",
    "Aloy",
    "Morrigan",
    "Teemo",
    "Pika",
    "Tracer",
    "Mercy",
    "Sephiroth",
    "Sub-Zero",
    "Riku",
    "Tidus",
    "Diddy",
    "Cortana",
    "Jak",
    "Sly",
    "Vaas",
    "Lulu",
    "Kassandra",
    "Ratchet",
    "Clank",
    "Joel",
    "Senua",
    "Wolverine",
    "Deadpool",
    "Finn"
]


game_character_names = [
    "Mario",
    "Link",
    "Samus",
    "Sonic",
    "Lara",
    "Kratos",
    "Cloud",
    "Master",
    "Nathan",
    "Ellie",
    "Zelda",
    "Mega",
    "Geralt",
    "Solid",
    "Ezio",
    "Tifa",
    "Donkey",
    "Chun-Li",
    "Luigi",
    "Bowser",
    "Arthas",
    "Leon",
    "Sora",
    "Dovahkiin",
    "Aloy",
    "Morrigan",
    "Teemo",
    "Jaina",
    "Shovel",
    "Garrus",
    "Yuna",
    "Pika",
    "Tracer",
    "Mercy",
    "Sephiroth",
    "Sub-Zero",
    "Riku",
    "Tidus",
    "Diddy",
    "Cortana",
    "Jak",
    "Sly",
    "Vaas",
    "Lulu",
    "Kassandra",
    "Ratchet",
    "Clank",
    "Aloy",
    "Joel",
    "Senua"
]


character_names = [
    "Tony",
    "Harry",
    "Luke",
    "Hermione",
    "James",
    "Katniss",
    "Walter",
    "Elsa",
    "Daenerys",
    "Indiana",
    "Frodo",
    "Sherlock",
    "Ellen",
    "John",
    "Lara",
    "Black",
    "Jack",
    "Dexter",
    "Katara",
    "Michael",
    "Tony",
    "Rick",
    "Aragorn",
    "Sheldon",
    "Don",
    "James",
    "Neo",
    "Sarah",
    "Ron",
    "Jules",
    "Jonny",
    "Arya",
    "Jack",
    "Dexter",
    "Xena",
    "Forrest",
    "Eleven",
    "John",
    "Dr.",
    "Jay",
    "Hannibal",
    "Mr.",
    "Mal",
    "Eric",
    "Hermione",
    "Atticus",
    "Elizabeth",
    "Hagrid"
]


def generate_random_username():
    selected_lists = random.sample([random_character_names, game_character_names, character_names], 2)

    username = ""
    for selected_list in selected_lists:
        if selected_list:
            selected_string = random.choice(selected_list)
            username += selected_string
        
    username += str(random.randint(100000, 999999))

    return username
        