# seed_topics.py
from django.core.management.base import BaseCommand
from content.models import LevelZone, Topic


class Command(BaseCommand):
    help = "Seeds LevelZones and Topics"

    def handle(self, *args, **kwargs):
        seed_data = [
            {
                "zone": "Zone 1: Python Basics (Intro Gameplay Zone)",
                "topics": [
                    {
                        "name": "Introduction to Python & IDE Setup",
                        "description": "Setting up Python and the development environment.",
                        "tags": "python, ide, installation, setup, hello world"
                    },
                    {
                        "name": "Variables & Data Types",
                        "description": "Storing and managing data using Python's basic types.",
                        "tags": "variables, data types, int, float, str, bool"
                    },
                    {
                        "name": "Basic Input and Output",
                        "description": "Interacting with users using input() and print().",
                        "tags": "input, output, print, user input, console"
                    },
                    {
                        "name": "Operators",
                        "description": "Performing arithmetic, logical, and comparison operations.",
                        "tags": "operators, arithmetic, logical, comparison, boolean"
                    },
                    {
                        "name": "Comments & Code Readability",
                        "description": "Writing clear, maintainable Python code.",
                        "tags": "comments, readability, style, indentation, pep8"
                    }
                ]
            },
            {
                "zone": "Zone 2: Control Structures (Logic Decision Zone)",
                "topics": [
                    {
                        "name": "Conditional Statements",
                        "description": "Controlling the program flow using if, else, and elif.",
                        "tags": "if, else, elif, condition, branching"
                    },
                    {
                        "name": "Error Handling",
                        "description": "Handling unexpected errors using try-except blocks.",
                        "tags": "try, except, error, exception, bug"
                    }
                ]
            },
            {
                "zone": "Zone 3: Loops & Iteration (Cognitive Repetition Zone)",
                "topics": [
                    {
                        "name": "Loops",
                        "description": "Understanding and using for and while loops.",
                        "tags": "loop, iteration, for, while, repeat"
                    },
                    {
                        "name": "Nested Loops",
                        "description": "Using loops inside other loops for pattern generation and matrix handling.",
                        "tags": "nested loop, inner loop, pattern, matrix"
                    },
                    {
                        "name": "Strings & String Methods",
                        "description": "Working with strings and their built-in methods.",
                        "tags": "strings, string methods, text, manipulation"
                    }
                ]
            },
            {
                "zone": "Zone 4: Data Structures & Modularity (System Design Zone)",
                "topics": [
                    {
                        "name": "Lists & Tuples",
                        "description": "Storing collections of items using lists and tuples.",
                        "tags": "lists, tuples, sequences, indexing, slicing"
                    },
                    {
                        "name": "Sets",
                        "description": "Working with unordered collections using sets.",
                        "tags": "sets, unique, membership, set operations"
                    },
                    {
                        "name": "Functions",
                        "description": "Writing reusable code using functions with parameters and return values.",
                        "tags": "functions, parameters, return, def, scope"
                    },
                    {
                        "name": "Dictionaries",
                        "description": "Managing key-value pairs with dictionaries.",
                        "tags": "dictionaries, dict, keys, values, mapping"
                    }
                ]
            }
        ]


        for zone_data in seed_data:
            zone_obj, _ = LevelZone.objects.get_or_create(
                title=zone_data["zone"],
                defaults={"description": zone_data["zone"]}
            )
            for topic_data in zone_data["topics"]:
                topic_obj, created = Topic.objects.get_or_create(
                    zone=zone_obj,  # ✅ renamed from level to zone
                    name=topic_data["name"],
                    defaults={
                        "description": topic_data["description"],
                        "tags": topic_data["tags"]
                    }
                )
                if created:
                    print(f"Created topic: {topic_data['name']} under {zone_data['zone']}")
                else:
                    print(f"Topic already exists: {topic_data['name']}")

