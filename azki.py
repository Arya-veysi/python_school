while (True):  
    def azki(text):
        list1 = []
        for x in text:
            list1.append(str(ord(x) * 5))
        result = "-".join(list1)
        print("Encoded Text:", result)
        return result

    def unlock(text):
        parts = text.split('-')
        decoded_text = ''
        for part in parts:
            decoded_text += chr(int(part) // 5)
        print("Decoded Text:", decoded_text)
        return decoded_text

    a = int(input("Enter your choice (1 for encoding, 2 for decoding): "))

    if a == 1:
        text = input("Enter text: ")
        azki(text)
    elif a == 2:
        text = input("Enter encoded text: ")
        unlock(text)
    else:
        print("incorrect choise")
