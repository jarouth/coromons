import random

# File input
file_location = input("Where is the data file:")
if file_location == "":
    file_location = "/home/jarouth/projects/ITSC/1212/coromons/CoromonDataset.csv"

with open(file_location, "r") as filerd:
    lines = filerd.readlines()

# Property Indexes
NAME = 0
TYPE = 1
HEALTH_POINTS = 2
ATTACK = 3
SPECIAL_ATTACK = 4
DEFENSE = 5
SPECIAL_DEFENSE = 6
SPEED = 7
STAMINA_POINTS = 8

# Property dictionary
coromon_properties = {
    "Health_Points": HEALTH_POINTS,
    "Attack": ATTACK,
    "Special_Attack": SPECIAL_ATTACK,
    "Defense": DEFENSE,
    "Special_Defense": SPECIAL_DEFENSE,
    "Speed": SPEED,
    "Stamina_Points": STAMINA_POINTS,
}

coromons_by_type = {}

# Build a dictionary of Coromons by type
for line in lines[1:]:
    data = line.strip().split(",")
    coromon_type = data[TYPE]
    
    if coromon_type not in coromons_by_type:
        coromons_by_type[coromon_type] = []
    
    coromons_by_type[coromon_type].append(data)


# Function to get the total number of Coromons
def coromon_total():
    return len(lines) - 1


# Function to get a random Coromon
def random_coromon():
    return random.choice(lines)


# Function to calculate the average score of a specific property for a given Coromon type
def average_property_score(coromon_type, property_name):
    prop_index = coromon_properties[property_name]
    typed_coromons = coromons_by_type[coromon_type]
    scores = [int(c[prop_index]) for c in typed_coromons if c[prop_index].isdigit()]
    
    return sum(scores) / len(scores) if scores else 0


def display_average_stats():
    types_of_coromon = list(coromons_by_type.keys())
    
    for coromon_type in types_of_coromon:
        print(f"\n{coromon_type}")
        for property_name in coromon_properties:
            avg_score = average_property_score(coromon_type, property_name)
            print(f"The average {property_name} is: {round(avg_score, 2)}")


# Sorting the Coromon types by the given property and finding highest/lowest
def display_highest_and_lowest_stats():
    types_of_coromon = list(coromons_by_type.keys())
    
    for property_name in coromon_properties:
        types_of_coromon.sort(key=lambda x: average_property_score(x, property_name))
        
        highest_type = types_of_coromon[-1]
        lowest_type = types_of_coromon[0]
        
        print(f"\n{property_name} highest average is in {highest_type}")
        print(f"{property_name} lowest average is in {lowest_type}")


def main():
    print(f"There are {coromon_total()} total Coromons.")
    print("Random Coromon sample:", random_coromon())
    
    # Display Coromon types and their average stats
    display_average_stats()

    # Display highest and lowest stats for each property
    display_highest_and_lowest_stats()


if __name__ == "__main__":
    main()
