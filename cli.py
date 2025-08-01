import datetime

#Define CLI for terminal output for user interaction
def start_cli(package_table, trucks):
    while True:
        print("\n=== WGUPS CLI Menu ===")
        print("1. View total mileage")
        print("2. Check status of all packages at a time")
        print("3. Check status of a specific package")
        print("4. Exit")

        choice = input("Select an option (1–4): ").strip()

#IF/ELSE statements reading from user input of 1-4 and outputing the applicable information
        if choice == "1":
            total = sum(t.mileage for t in trucks)
            print(f"Total mileage by all trucks: {total:.2f} miles")

        elif choice == "2":
            time_input = input("Enter time (HH:MM:SS): ").strip()
            try:
                h, m, s = map(int, time_input.split(":"))
                check_time = datetime.timedelta(hours=h, minutes=m, seconds=s)
                for pid in range(1, 41):
                    pkg = package_table.lookup(pid)
                    pkg.update_status(check_time)
                    print(pkg)
            except Exception:
                print("Invalid time format.")

        elif choice == "3":
            try:
                pid = int(input("Enter Package ID (1–40): ").strip())
                time_input = input("Enter time (HH:MM:SS): ").strip()
                h, m, s = map(int, time_input.split(":"))
                check_time = datetime.timedelta(hours=h, minutes=m, seconds=s)
                pkg = package_table.lookup(pid)
                pkg.update_status(check_time)
                print(pkg)
            except Exception:
                print("Invalid input.")

        elif choice == "4":
            print("Goodbye!")
            break

#Check against invalid inputs that are != 1-4
        else:
            print("Invalid selection.")
