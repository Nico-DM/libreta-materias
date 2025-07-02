import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <id_materia>")
        sys.exit(1)
    id_materia = sys.argv[1]

if __name__ == "__main__":
    main()