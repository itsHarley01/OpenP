import os
import subprocess

CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'configs.txt')

def load_configs():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    configs = {}
    current = None
    for line in lines:
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1]
            configs[current] = []
        elif current:
            configs[current].append(line)
    return configs

def save_configs(configs):
    with open(CONFIG_FILE, 'w') as f:
        for name, paths in configs.items():
            f.write(f"[{name}]\n")
            for p in paths:
                f.write(p + "\n")

def add_config():
    name = input("Enter config name: ").strip()
    count = int(input("Number of paths to open: "))
    paths = [input(f"Enter path {i+1}: ").strip() for i in range(count)]

    configs = load_configs()
    configs[name] = paths
    save_configs(configs)
    print(f"Config '{name}' added.")

def edit_config():
    configs = load_configs()
    if not configs:
        print("⚠ No configs to edit.")
        return

    print("Existing configs:")
    for i, (name, paths) in enumerate(configs.items(), start=1):
        print(f"{i}. {name} - paths [{len(paths)}]")

    choice = input("Enter config name to edit: ").strip()
    if choice not in configs:
        print("Config not found.")
        return

    print("\n1. Edit existing paths")
    print("2. Add new paths")
    option = input("Choose option [1/2]: ").strip()

    if option == "1":
        new_paths = []
        for i, path in enumerate(configs[choice]):
            print(f"\nPath {i+1} (current): {path}")
            updated = input(f"Path {i+1} (new, leave blank to keep): ").strip()
            new_paths.append(updated if updated else path)
        configs[choice] = new_paths
        print(f"Paths for '{choice}' updated.")
        
    elif option == "2":
        count = int(input("How many new paths to add? "))
        for i in range(count):
            new_path = input(f"Enter new path {i+1}: ").strip()
            configs[choice].append(new_path)
        print(f"{count} new path(s) added to '{choice}'.")

    else:
        print("Invalid option.")
        return

    save_configs(configs)

def run_config(name):
    configs = load_configs()
    if name not in configs:
        print(f"Config '{name}' not found.")
        return

    print(f"Opening paths for '{name}'...")
    for path in configs[name]:
        full_path = os.path.abspath(path)
        subprocess.Popen(["code", full_path], shell=True)

def main():
    import sys
    if len(sys.argv) > 1:
        run_config(sys.argv[1].replace("-",""))
        return

    while True:
        ascii_art = r"""
████▄ █ ▄▄  ▄███▄      ▄   █ ▄▄  
█   █ █   █ █▀   ▀      █  █   █ 
█   █ █▀▀▀  ██▄▄    ██   █ █▀▀▀  
▀████ █     █▄   ▄▀ █ █  █ █     
       █    ▀███▀   █  █ █  █    
        ▀           █   ██   ▀   
"""
        print(ascii_art)
        configs = load_configs()
        if configs:
            print("Configs:")
            for name, paths in configs.items():
                print(f"{name} - paths [{len(paths)}]")
        else:
            print("No configs yet.")

        print("\nOptions:")
        print("Add config [x]")
        print("Edit config [y]")
        print("Exit       [z]")
        choice = input("Select an option: ").strip().lower()

        if choice == 'x':
            add_config()
        elif choice == 'y':
            edit_config()
        elif choice == 'z':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
