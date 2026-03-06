def parse_and_join_items(
    item_string: str, number_of_outputs: int = 0, lowercase: bool = False
) -> str:
    """Parse a string of items separated by commas, and join them with pipes.

    Parameters:
    item_string: A string of items separated by commas.
    number_of_outputs: The maximum number of items to output. If 0, output all
    lowercase: Whether to convert items to lowercase.

    Returns:
    A string of items separated by pipes.

    Examples:
    parse_and_join_items(" A, Bee, bee, , C ")            -> "A|Bee|bee|C"
    parse_and_join_items(" A, Bee, bee, ,  C ", lowercase=True)    -> "a|bee|c"
    """
    if not item_string:
        return ""  # empty
    raw_items = item_string.split(",")
    result = []
    i = 0
    for item in raw_items:
        item = item.strip()
        if item == "":
            continue
        if lowercase:
            item = item.lower()
        # if len(item) < 2:
        #    continue
        if item in result:
            continue
        result.append(item)
        i += 1
        if number_of_outputs and i >= number_of_outputs:
            break
    return "|".join(result)


print(parse_and_join_items(" A, Bee, bee,  , C "))
print(parse_and_join_items(" A, Bee, bee,  , C ", lowercase=True))
print(parse_and_join_items("A,B,C", number_of_outputs=2))

# Examples (use to confirm you didn't change behavior)
# parse_and_join_items(" A, Bee, bee, , C ")            -> "A|Bee|bee|C"
# parse_and_join_items(" A, Bee, bee, ,  C ", lowercase=True)    -> "a|bee|c"
# parse_and_join_items("A,B,C", number_of_outputs=2)     -> "A|B"
