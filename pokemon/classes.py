"""
21/09/2023 00:17
Author : Omar Bounawara

Pokemon OOP Game

Description:
This script serves as an educational tool to showcase the implementation of object-oriented programming (OOP)
concepts in Python. It simulates a simplified Pokemon system with classes for Person, Pokemon, and PokemonInstance.

Educational Purpose and Key Concepts:
1. **Class Definition:** Demonstrates the creation of classes (Person, Pokemon, PokemonInstance) to model entities.
2. **Object Instantiation:** Illustrates the instantiation of objects (instances of classes) representing individuals and Pokemon.
3. **Inheritance:** Utilizes inheritance where the `PokemonInstance` class inherits from the `Pokemon` class, showcasing the reuse of attributes and methods.
4. **Encapsulation:** Encapsulates data within classes, making it private to the class and accessed through public methods.
5. **Polymorphism:** Implements polymorphism in the `__repr__` method, providing different representations for Person, Pokemon, and PokemonInstance instances.
6. **Recursion:** Demonstrates a recursive aspect in the `__init__` method of the `PokemonInstance` class, allowing the creation of an instance from another Pokemon object.
7. **Error Handling:** Includes basic error handling for instance creation, notifying when essential information is missing.

Example Usage:
- Initializes a Pokemon with specified attributes.
- Displays Pokemon information using the __repr__ method.
- Applies experience gain to the Pokemon, triggering evolution when reaching the evolution level.
- Creates a PokemonInstance from the Pokemon, showcasing class instantiation and polymorphism.
- Simulates damage, healing, and status changes in the PokemonInstance.

Note: The script aims to demonstrate OOP principles, and the accuracy of Pokemon status and rules may not fully align with the official Pokemon games.

Disclaimer:
In the context of this script, I view it as a fundamental exercise rather than a full-fledged project.
The creation of classes like Person, Pokemon, and PokemonInstance has provided me with a strong
introduction to key object-oriented programming (OOP) concepts. Moving forward in my educational
journey, I'm considering the possibility of expanding this simulation by incorporating additional
features like items, combat mechanics, or even enhancing existing classes.I acknowledge that this script is a crucial step in my learning
process, and the act of further developing it presents an excellent opportunity to deepen my
understanding of Python and OOP principles.
This script is created for educational purposes and is not affiliated with or endorsed by any official Pokemon entities.
The names, trademarks, and rights associated with Pokemon are the property of the respective company.

"""

import csv

def get_line_from_csv(path, line_number):
    """
    Retrieve a specific line from a CSV file.

    Args:
        path (str): The path to the CSV file.
        line_number (int): The line number to retrieve.

    Returns:
        list or None: The list of values in the specified line, or None if the line number is out of bounds.
    """
    with open(path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

        if 1 <= line_number <= len(data):
            return data[line_number - 1]
        else:
            return None

class Person:
    """
    A class representing a person.

    Attributes:
        persons (dict): A dictionary to store person IDs and their corresponding roles.
    """
    persons = {"1": "player"}

    def __init__(self, id: int, name: str, gender, pokemon_list: list):
        """
        Initialize a Person instance.

        Args:
            id (int): The person's ID.
            name (str): The person's name.
            gender: The person's gender.
            pokemon_list (list): A list of Pokemon associated with the person.
        """
        self.id = id
        self.name = name
        self.pokemon_list = pokemon_list


class Pokemon:
    """
    A class representing a Pokemon.

    Attributes:
        session_pokemons (dict): A dictionary to store active Pokemon instances.
    """
    session_pokemons = {}

    def __init__(self, id, owner_id: int, nickname: str, species_id: int, level: int, exp: int):
        """
        Initialize a Pokemon instance.

        Args:
            id: The Pokemon's ID.
            owner_id (int): The ID of the owner (person) of the Pokemon.
            nickname (str): The nickname of the Pokemon.
            species_id (int): The ID representing the species of the Pokemon.
            level (int): The level of the Pokemon.
            exp (int): The experience points of the Pokemon.
        """
        data = get_line_from_csv("pokemons.csv", species_id + 1)
        self.pokemon_id = id
        self.owner_id = owner_id
        self.species_id = int(data[0])
        self.species_name = data[1]
        self.nickname = nickname
        self.type = data[2]
        self.level = level
        self.exp = exp
        self.evo_level = int(data[3])
        self.atk = int(data[4]) + (2 * level)
        self.deff = int(data[5]) + (2 * level)
        self.hp = int(data[6]) + (2 * level)
        self.stamina = 50 + level * 2
        self.sp_atk = int(data[7]) + (2 * level)
        self.sp_def = int(data[8]) + (2 * level)
        self.speed = int(data[9]) + (2 * level)
        Pokemon.session_pokemons[str(id)] = self

    def __repr__(self):
        """
        Return a string representation of the Pokemon instance.
        """
        str_to_print = (f"""
        Owner : {Person.persons[str(self.owner_id)]}
        Owner ID: {self.owner_id} 
        Pokemon ID : {self.pokemon_id}
        Species : {self.species_name} 
        Nickname : {self.nickname} 
        Type : {self.type}
        Level : {self.level} 
        EXP : {self.exp}
        """)
        return str_to_print

    def evolve(self):
        """
        Evolve the Pokemon to the next species.
        """
        Pokemon(self.pokemon_id, self.owner_id, self.nickname, self.species_id + 1, self.level, self.exp)
        del self

    def gain_exp(self, exp):
        """
        Increase the Pokemon's experience points and handle level-up and evolution.

        Args:
            exp (int): The experience points to be gained.
        """
        new_exp = self.exp - exp
        if new_exp < 0:
            if self.level != 98:
                self.level += 1
            self.exp = self.level * 100 + new_exp
            if self.level == self.evo_level:
                self.evolve()
        else:
            self.exp = new_exp


class PokemonInstance(Pokemon):
    """
    A class representing an instance of a Pokemon.

    Attributes:
        active_pokemons (dict): A dictionary to store active Pokemon instances.
    """
    active_pokemons = {}

    def __init__(self, id=0, owner_id=0, nickname="", species_id=0, level=0, exp=0, pokemon="",
                 active_hp=-1, active_stamina=-1, status="", status_counter=0, alive=True):
        """
        Initialize a PokemonInstance.

        Args:
            id: The Pokemon's ID.
            owner_id (int): The ID of the owner (person) of the Pokemon.
            nickname (str): The nickname of the Pokemon.
            species_id (int): The ID representing the species of the Pokemon.
            level (int): The level of the Pokemon.
            exp (int): The experience points of the Pokemon.
            pokemon: A Pokemon object to create an instance from.
            active_hp (int): The current HP of the Pokemon instance.
            active_stamina (int): The current stamina of the Pokemon instance.
            status (str): The status of the Pokemon instance.
            status_counter (int): The counter for the Pokemon's status.
            alive (bool): Indicates whether the Pokemon instance is alive.
        """
        if pokemon == "" and (id == 0 or owner_id == 0 or nickname == "" or species_id == 0 or level == 0 or exp == 0):
            print("CAN'T CREATE INSTANCE WITHOUT PROVIDING INFO, AT LEAST PROVIDE POKEMON OBJECT")
            return False
        elif pokemon == "":
            super().__init__(id, owner_id, nickname, species_id, level, exp)
            if active_hp == -1 and active_stamina == -1:
                self.active_hp = Pokemon.session_pokemons[str(id)].hp
                self.active_stamina = Pokemon.session_pokemons[str(id)].stamina
            self.status = status
            self.status_count = status_counter
            self.alive = alive
            PokemonInstance.active_pokemons[str(id)] = self
        else:
            id = pokemon.pokemon_id
            owner_id = pokemon.owner_id
            nickname = pokemon.nickname
            species_id = pokemon.species_id
            level = pokemon.level
            exp = pokemon.exp
            PokemonInstance(id, owner_id, nickname, species_id, level, exp)

    def __repr__(self):
        """
        Return a string representation of the PokemonInstance.
        """
        str_to_print = super().__repr__() + f"""Current HP : {self.active_hp}
        Current Stamina : {self.active_stamina}
        Alive : {self.alive}"""

        return str_to_print

    def take_damage(self, amount):
        """
        Reduce the PokemonInstance's HP by the specified amount.

        Args:
            amount (int): The amount of damage to be taken.
        """
        self.active_hp -= amount
        if self.active_hp <= 0:
            self.alive = False
            self.active_hp = 0

    def heal(self, amount):
        """
        Heal the PokemonInstance by the specified amount, up to its maximum HP.

        Args:
            amount (int): The amount of healing to be applied.
        """
        max_hp = Pokemon.session_pokemons[str(self.pokemon_id)].hp
        if self.alive:
            if self.active_hp + amount > max_hp:
                self.active_hp = max_hp
            else:
                self.active_hp += amount

    def recover_stamina(self, amount):
        """
        Increase the PokemonInstance's stamina by the specified amount.

        Args:
            amount (int): The amount of stamina to be recovered.
        """
        self.active_stamina += amount

    def remove_stamina(self, amount):
        """
        Decrease the PokemonInstance's stamina by the specified amount.

        Args:
            amount (int): The amount of stamina to be removed.
        """
        self.active_stamina -= amount


# Example usage
print("Initializing new Pokemon...")
id = 1
owner_id = 1
nickname = "frog"
species_id = 2
level = 31
exp = 100
myPokemon = Pokemon(id, owner_id, nickname, species_id, level, exp)
print("Displaying Pokemon info")
print(Pokemon.session_pokemons[str(id)])
print("Applying exp gain...")
(myPokemon.gain_exp(150))
print("Pokemon evolves after reaching evolve level")
print(Pokemon.session_pokemons[str(id)])
print("Initializing new Pokemon instance...")
PokemonInstance(pokemon=Pokemon.session_pokemons["1"])
print(PokemonInstance.active_pokemons[str(id)])
print("Taking damage: 50")
(PokemonInstance.active_pokemons[str(id)]).take_damage(50)
print(PokemonInstance.active_pokemons[str(id)])
print("Healing: 100")
(PokemonInstance.active_pokemons[str(id)]).heal(100)
print("After Healing")
print(PokemonInstance.active_pokemons[str(id)])
print("Taking damage and dying")
(PokemonInstance.active_pokemons[str(id)]).take_damage(2000)
print(PokemonInstance.active_pokemons[str(id)])
print("Trying to heal a dead Pokemon...")
(PokemonInstance.active_pokemons[str(id)]).heal(2000)
