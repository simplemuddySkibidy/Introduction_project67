s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")
def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if sorted(s1) == sorted(s2):
        print("Строки являются анаграммами.")
    else:
        print("Строки не являются анаграммами.")
