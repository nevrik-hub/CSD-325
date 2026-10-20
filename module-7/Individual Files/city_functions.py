"""
Author: Nicholas Zankl
Date: September 20, 2026
Course: CSD-325
Assignment: Module 7.2 - Test Cases (city_functions.py)
Description: Formats city, country, population, and language data into a single string.
"""

def city_country(city, country, population=None, language=None):
    """Return a single string formatted as City, Country - population xxx, Language."""
    result = f"{city.title()}, {country.title()}"

    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"

    return result


if __name__ == "__main__":
    # Call 1: City, Country
    print(city_country("santiago", "chile"))

    # Call 2: City, Country, Population
    print(city_country("santiago", "chile", population=5000000))

    # Call 3: City, Country, Population, Language
    print(city_country("santiago", "chile", population=5000000, language="spanish"))
