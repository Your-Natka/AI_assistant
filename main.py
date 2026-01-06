from interfaces.cli import run_cli
from interfaces.telegram import run_telegram

def main():
    mode = input("Choose mode: cli / telegram / exit: ").lower()

    if mode == "cli":
        run_cli()
    elif mode == "telegram":
        run_telegram()
    else:
        print("Bye!")

if __name__ == "__main__":
    main()