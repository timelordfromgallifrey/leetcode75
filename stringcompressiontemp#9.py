def compress(chars):
    answer = ""
    count = 1
    i = 0

    for i in range(1, len(chars)):
        if chars[i] != chars[i - 1]:
            answer += chars[i - 1]
            if count != 1:
                answer += str(count)
            count = 1
        else:
            count += 1

    answer += chars[len(chars) - 1]

    if count != 1:
        answer += str(count)

    for i in range(len(answer)):
        chars[i] = answer[i]

    print(chars)
    return len(answer)

print(compress(["a", "b", "c"]))