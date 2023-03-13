def convert_to_integer(value: str):
    try:
        return int(value)
    except ValueError:
        print("Error while converting the value to integer")
        raise


def separate_line():
    print("=" * 72)
