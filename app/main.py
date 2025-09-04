import sys
import os
import shutil

def main():
    # Uncomment this block to pass the first stage
    builtin_cmds = ["echo", "exit","type"]
   
    # Wait for user input
    while True:
        output = ""
        try:
            sys.stdout.write("$ ")
            sys.stdout.flush()

            line: str = input()
            parts = line.strip().split()

            if not parts:
                continue

            command = parts[0]
            args = parts[1:] if len(parts) > 1 else []

            if command in builtin_cmds:
                if command == "type":
                    if args:
                        try:
                            arg_cmd = str(args[0])
                            if arg_cmd in builtin_cmds:
                                output = f"{arg_cmd} is a shell builtin"
                            elif p := shutil.which(arg_cmd):
                                output = f"{arg_cmd} is {p}"
                            else:
                                output = f"{arg_cmd}: not found"
                        except IndexError:
                            output = "Please enter a command to check its type."
                        except Exception:
                            output = f"{arg_cmd}: unable to read argument to type command"
                    else:
                        output = "type: not enough arguments"
                        
                elif command == "echo":
                    output = " ".join(args)

                elif command == "exit":
                    try:
                        exit_code = int(args[0]) if args else 0
                        exit(exit_code)
                    except ValueError:
                        output = "exit: numeric argument required"
                        

            else:
                output = f"{command}: command not found"

            print(output)
        
        except KeyboardInterrupt or EOFError as e:
            print("\nExiting...")
            sys.exit(0)
        

            # exit(0)

if __name__ == "__main__":
    main()
