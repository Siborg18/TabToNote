# TODO 1a Make note relationship algorithm e.g. A + 1 = A#/b♭ ... G + 2 = A, except E + 1 = F, B + 1 = C
# TODO 1b Make list of notes and respective point on tab i.e E0 = E, A3 = C
# To avoid confusion and to keep strings consistent they will be known as
# E_string(low E string), a_string, d_string, g_string, b_String, e_string(high e string)
# TODO 2 Make GUI
# TODO 3 Make list of common chords using notes


NOTES_A_TO_G_SHARP = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]
NOTES_A_TO_A_FLAT = ["a", "b♭", "b", "c" "d♭", "d", "e♭", "e", "f", "g♭", "g", "a♭"]

def print_open_string(string):
    try:
        if string == "e" or string == "E":
            string_E_open = f"{NOTES_A_TO_G_SHARP[7]}/{NOTES_A_TO_A_FLAT[6]}"
            return string_E_open
        if string == "a":
            string_a_open = f"{NOTES_A_TO_G_SHARP[0]}/{NOTES_A_TO_A_FLAT[0]}"
            return string_a_open
        if string == "d":
            string_d_open = f"{NOTES_A_TO_G_SHARP[5]}/{NOTES_A_TO_A_FLAT[4]}"
            return string_d_open
        if string == "g":
            string_g_open = f"{NOTES_A_TO_G_SHARP[-2]}/{NOTES_A_TO_A_FLAT[-2]}"
            return string_g_open
        if string == "b":
            string_b_open = f"{NOTES_A_TO_G_SHARP[2]}/{NOTES_A_TO_A_FLAT[2]}"
            return string_b_open
    except ValueError:
        print("Something went wrong")
        return 0

print(print_open_string("a"))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
