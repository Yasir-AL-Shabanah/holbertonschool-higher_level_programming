#!/usr/bin/python3
"""Print command-line arguments without the program name."""


def main():
    """Print number of arguments and list them."""
    import sys

    args = sys.argv[1:]
    count = len(args)

    if count == 0:
        print("0 arguments.")
        return

    print(f"{count} argument{'' if count == 1 else 's'}:")
    for index, arg in enumerate(args, start=1):
        print(f"{index}: {arg}")


if __name__ == "__main__":
    main()
