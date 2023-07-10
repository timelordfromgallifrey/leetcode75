def reverseWords(s):
    wordstack=s.split()
    wordstack.reverse()
    newstring= " ".join(wordstack)
    print(newstring)

reverseWords("I  Am  THe power")
