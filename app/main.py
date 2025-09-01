import sys
import random


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    try:
        # Wait for user input
        while True:
            command: str = input()
            
            if command.strip() == "exit":
                print("$ exit 0")
                exit(0)
            else:
                print(f"{command}: command not found")
                sys.stdout.write("$ ")
            
    except KeyboardInterrupt as e:
        print("\nExiting...")
        sys.exit(0)
    finally:
        sys.stdout.flush()
        exit(0)

if __name__ == "__main__":
    main()
