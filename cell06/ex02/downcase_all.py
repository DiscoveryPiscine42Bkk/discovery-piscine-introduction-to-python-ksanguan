import sys


def downcase_it(text):
    return text.lower()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            print(downcase_it(arg))
    else:
        print("none")