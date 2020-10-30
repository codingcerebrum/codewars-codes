# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.


def rot13(message):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result = []
    for each in message:
        if(each.isalpha()):
            if(each in alpha):
                ind = (alpha.index(each) + 13) % 26
                result.append(alpha[ind])
            else:
                ind = (Alpha.index(each) + 13) % 26
                result.append(Alpha[ind])
        else:
            result.append(each)
    result = ''.join(result)
    return result

print(rot13("this323#"))