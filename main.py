from Classes import Library


def main():

    library = Library()

    f = open("Data\List.txt", "r")
    t = f.read()
    lines = t.split()
    f.close()

    library.load_files_into_library(lines)
    library.update()
    library.display()
    print(len(library.get_names()))


if __name__ == '__main__':
    main()
