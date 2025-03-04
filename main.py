import argparse
import random

# List of Dice Types

dice_collection = {
    "D00": {
        "name": "Percentile Die",
        "value": 100,
        "type": "Specialised Die"
    },
    "d2": {
        "name": "Double-Sided Die (Coin)",
        "value": 2,
        "type": "Specialised Die"
    },
    "d3": {
        "name": "Three-Sided",
        "value": 3,
        "type": "Specialised Die"
    },
    "d4": {
        "name": "Four-Sided Pyramid Die",
        "value": 4,
        "type": "Standard Die"
    },
    "d5": {
        "name": "Five-Sided Die (Pentagonal)",
        "value": 5,
        "type": "Specialised Die"
    },
    "d6": {
        "name": "Six-Sided Cube Die",
        "value": 6,
        "type": "Standard Die"
    },
    "d7": {
        "name": "Seven-Sided Die (Heptagonal)",
        "value": 7,
        "type": "Specialised Die"
    },
    "d8": {
        "name": "Eight-Sided Die (Octahedral)",
        "value": 8,
        "type": "Standard Die"
    },
    "d10": {
        "name": "Ten-Sided Die ()",
        "value": 10,
        "type": "Standard Die"
    },
    "d12": {
        "name": "Twelve-Sided Die (Dodecahedron)",
        "value": 12,
        "type": "Standard Die"
    },
    "d20": {
        "name": "Twenty-Sided Die ()",
        "value": 20,
        "type": "Primary Die"
    }
}

def main():

    # Command-Line Arguments

    parser = argparse.ArgumentParser(description = "DieCLI: A Digital Dice Roller Command-Line Tool")

    parser.add_argument("-v", "--verbose", help = "Provides Extra Details for Each Dice Roll")
    parser.add_argument("dice_number", type = int, help = "Amount of Dice")
    parser.add_argument("dice_type", type = str, help = "Type of Dice")

    args = parser.parse_args()

    if args.dice_type in dice_collection.keys():
        roll = args.dice_number * random.randrange(1, dice_collection[args.dice_type]["value"] + 1)
        if roll == 20:
            print("NATURAL", roll)
        else:
            print("Roll:", roll)

if __name__ == "__main__":
    main()