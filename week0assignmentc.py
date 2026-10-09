def main():
    text=input("Say anything but include ; :) or :( ")
    print(convert(text))


def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")


main()