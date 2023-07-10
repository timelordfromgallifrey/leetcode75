def compress(chars):
        s=""
        a=chars[0]
        count=1
        s+=a
        for i in range(1,len(chars)):
            if chars[i]==a:
                count+=1
                print(f"count value= {count}")
            else:
                s+=str(count) if count>1 else ""
                print(f"value of s after adding count={s}")
                a=chars[i]
                s+=a
                print(f"value of s aftering entering next character={s}")
                count=1
                
        s+=str(count)
        print(f"value of s in the end={s}")

        print(chars)

        l=len(chars)-len(s)


        for i in range(0,len(s)):
            chars[i]=s[i]

        print(chars)

        return len(chars)-l

print(compress(["a","b","c"]))