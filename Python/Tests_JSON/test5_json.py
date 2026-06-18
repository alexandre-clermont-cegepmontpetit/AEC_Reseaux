import random
import json

noms = [
    "Emma", "Noah", "Sophia", "Liam", "Olivia", "Jackson", "Ava", "Lucas", "Isabella", "Mason",
    "Mia", "Ethan", "Charlotte", "Logan", "Amelia", "James", "Harper", "Benjamin", "Evelyn", "Elijah",
    "Abigail", "Alexander", "Emily", "Michael", "Ella", "Daniel", "Avery", "Henry", "Scarlett", "Sebastian",
    "Grace", "Jack", "Chloe", "Owen", "Victoria", "Samuel", "Lily", "Matthew", "Aria", "Joseph",
    "Hannah", "David", "Zoey", "Carter", "Nora", "Wyatt", "Riley", "John", "Layla", "Luke",
    "Aubrey", "Gabriel", "Ellie", "Julian", "Stella", "Levi", "Natalie", "Isaac", "Zoe", "Lincoln",
    "Leah", "Anthony", "Hazel", "Christopher", "Violet", "Joshua", "Aurora", "Andrew", "Savannah", "Nathan",
    "Brooklyn", "Thomas", "Bella", "Charles", "Claire", "Caleb", "Skylar", "Ryan", "Lucy", "Asher",
    "Paisley", "Jonathan", "Anna", "Hunter", "Caroline", "Christian", "Genesis", "Aaron", "Kennedy", "Adrian",
    "Samantha", "Connor", "Maya", "Jeremiah", "Willow", "Eli", "Madelyn", "Cameron", "Serenity", "Jordan"
]

num = random.randint(0, 100)
nom = random.choice(noms)

with open("data5.json", "r", encoding="utf-8") as fichier:
    etudiants = json.load(fichier)

etudiants.append(
    {
        "nom": nom,
        "note": num
    }
)

with open("data5.json", "w", encoding="utf-8") as fichier:
    json.dump(etudiants, fichier, indent=4)