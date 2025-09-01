import sys
import random


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    try:
        # Wait for user input
        while True:
            command: str = input()
            print(f"{command}: command not found")
            sys.stdout.write("$ exit 0")
            exit(0)
    except KeyboardInterrupt as e:
        print("\nExiting...")
        sys.exit(0)
    finally:
        sys.stdout.flush()

if __name__ == "__main__":
    main()
