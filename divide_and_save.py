
from colorama import Fore, Style, init

# Initialize colorama for Windows support
init(autoreset=True)

def get_number(prompt):
    while True:
        value = input(prompt)
        if value.lower() == 'q':  # Allow quitting mid-entry
            return None
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")

def main():
    results = []

    print("Enter your datasets. Type 'q' at any prompt to finish and see results.\n")

    while True:
        name = input("Dataset name (or 'q' to quit): ").strip()
        if name.lower() == 'q':
            break

        num1 = get_number("First number (Yearly Earnings): ")
        if num1 is None:
            break

        num2 = get_number("Second number (Owners): ")
        if num2 is None:
            break

        if num2 == 0:
            result = None
        else:
            result = num1 / num2

        results.append({
            "Name": name,
            "Dividend": num1,
            "Divisor": num2,
            "Result": result
        })

    # Sort by result (highest first, None at bottom)
    sorted_results = sorted(results, key=lambda x: (x["Result"] is not None, x["Result"]), reverse=True)

    print("\nFINAL RANKINGS")
    print(f"{'Rank':<5}{'Name':<15}{'Dividend':<12}{'Divisor':<12}{'Result':<12}")
    print("-" * 60)

    for i, entry in enumerate(sorted_results, start=1):
        if entry["Result"] is None:
            color = Fore.YELLOW
            res_str = "undefined"
        elif i == 1:
            color = Fore.GREEN
            res_str = f"{entry['Result']:.2f}"
        elif i == len(sorted_results):
            color = Fore.RED
            res_str = f"{entry['Result']:.2f}"
        else:
            color = Fore.CYAN
            res_str = f"{entry['Result']:.2f}"

        print(f"{i:<5}{entry['Name']:<15}{entry['Dividend']:<12}{entry['Divisor']:<12}{color}{res_str}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
