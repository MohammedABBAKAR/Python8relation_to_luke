# Luke Skywalker has family and friends. Help him remind them who 
# is who. Given a string with a name, return 
# the relation of that person to Luke.

# Person	Relation
# Darth Vader	father
# Leia	sister
# Han	brother in law
# R2D2	droid


# Examples

# relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

# relation_to_luke("Leia") ➞ "Luke, I am your sister."

# relation_to_luke("Han") ➞ "Luke, I am your brother in law."





def relation_to_luke(name: str) -> str:
    # Dictionary mapping names to their relations with Luke
    relations = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid"
    }
    
    # Get the relation from the dictionary
    relation = relations.get(name)
    
    # Return the formatted string
    if relation:
        return f"Luke, I am your {relation}."
    else:
        return "Relation not found."

# Examples of using the function
print(relation_to_luke("Darth Vader"))  # Output: "Luke, I am your father."
print(relation_to_luke("Leia"))  # Output: "Luke, I am your sister."
print(relation_to_luke("Han"))  # Output: "Luke, I am your brother in law."
print(relation_to_luke("R2D2"))  # Output: "Luke, I am your droid."
