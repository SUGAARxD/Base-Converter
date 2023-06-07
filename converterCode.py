

def less(number1, number2):
    if len(number1) > len(number2):
        return False
    if len(number1) < len(number2):
        return True
    return number1 < number2


def addingZeros(number, length):
    while len(number) < length:
        number = '0' + number
    return number


def removeZeros(number):
    i = 0
    while i < len(number) and number[i] == '0':
        i += 1
    newnumber = number[i:]
    return newnumber


def swap(number1, number2):
    length1 = len(number1)
    length2 = len(number2)
    if length1 < length2:
        number1, number2 = number2, number1
    return number1, number2


def addition(number1, number2):
    if number1 == "0":
        return number2
    if number2 == "0":
        return number1

    digitsAfterDotNumber1 = 0
    digitsAfterDotNumber2 = 0
    dotFoundNumber1 = False
    dotFoundNumber2 = False
    number1WithoutDecimals = ""
    number2WithoutDecimals = ""

    for i in range(len(number1)):
        if dotFoundNumber1:
            digitsAfterDotNumber1 += 1
        if number1[i] == '.':
            dotFoundNumber1 = True
        else:
            number1WithoutDecimals += number1[i]

    for i in range(len(number2)):
        if dotFoundNumber2:
            digitsAfterDotNumber2 += 1
        if number2[i] == '.':
            dotFoundNumber2 = True
        else:
            number2WithoutDecimals += number2[i]

    digitsDifference = digitsAfterDotNumber1 - digitsAfterDotNumber2

    if digitsDifference < 0:
        number1WithoutDecimals, number2WithoutDecimals = number2WithoutDecimals, number1WithoutDecimals
        digitsDifference *= -1

    while digitsDifference > 0:
        number2WithoutDecimals += '0'
        digitsDifference -= 1

    number1WithoutDecimals, number2WithoutDecimals = swap(number1WithoutDecimals, number2WithoutDecimals)

    if len(number2WithoutDecimals) < len(number1WithoutDecimals):
        number2WithoutDecimals = addingZeros(number2WithoutDecimals, len(number1WithoutDecimals))

    add = ""
    carry = 0

    for i in range(len(number1WithoutDecimals) - 1, -1, -1):
        sum = int(number1WithoutDecimals[i]) + int(number2WithoutDecimals[i])
        if carry:
            sum += 1
        if sum > 9:
            carry = 1
        else:
            carry = 0
        add = str(sum % 10) + add

    if carry:
        add = "1" + add

    add = removeZeros(add)

    maxDecimals = max(digitsAfterDotNumber1, digitsAfterDotNumber2)

    if digitsAfterDotNumber1 or digitsAfterDotNumber2:
        position = len(add) - 1

        if maxDecimals > 20:
            position -= (maxDecimals - 20)

        added = ""

        while maxDecimals > 0:
            if position >= 0:
                added = add[position] + added
                position -= 1
            else:
                added = '0' + added
            maxDecimals -= 1

        added = '.' + added

        if maxDecimals == len(add):
            added = '0' + added
        else:
            while position >= 0:
                added = add[position] + added
                position -= 1

        add = added

    i = len(add) - 1

    while i >= 0 and add[i] == '0' and maxDecimals > 0:
        add = add[:i]
        i -= 1

    if len(add) < 1:
        add += '0'
    else:
        if add[0] == '.':
            add = '0' + add

    return add


def subtraction(number1, number2):
    sub = ""

    if len(number1) < len(number2):
        number1 = addingZeros(number1, len(number2))

    if len(number2) < len(number1):
        number2 = addingZeros(number2, len(number1))

    carry = 0

    for i in range(len(number1) - 1, -1, -1):
        a = int(number1[i])
        b = int(number2[i])
        dif = int(number1[i]) - int(number2[i])
        if dif < 0:
            dif *= -1
            dif = 10 - dif
            carry = 1

        if carry:
            if i > 0:
                if (number1[i - 1] != '0'):
                    number1 = number1[:i - 1] + str(int(number1[i - 1]) - 1) + number1[i:]
                else:
                    j = i
                    nr = number1[i:]
                    while j > 0 and number1[j - 1] == '0':
                        nr = "9" + nr
                        j = j - 1
                    nr = str(int(number1[j - 1]) - 1) + nr
                    nr = number1[:j - 1] + nr 
                    number1 = nr
            carry = 0

        sub = str(dif) + sub

    sub = removeZeros(sub)

    if len(sub) < 1:
        sub += '0'

    return sub


def half(number, begin, end):
    hlf = ""
    for i in range(begin, end):
        hlf += number[i]
    return hlf


def division(number1, number2):
    if number2 == "0":
        return "Undefined"
    if number1 == "0":
        return "0"

    div = "0"
    number1copy = number1

    while not less(number1copy, number2):
        div = addition(div, "1")
        number1copy = subtraction(number1copy, number2)

    if number1copy != "0":
        div += '.'
        precision = 19
        divAfterDot = "0"
        number1copy += '0'

        while number1copy != "0" and precision > 0:
            while less(number1copy, number2):
                number1copy += '0'
                div += '0'
                precision -= 1

            divAfterDot = addition(divAfterDot, "1")
            number1copy = subtraction(number1copy, number2)

            if less(number1copy, number2) and precision > 0:
                precision -= 1
                div += divAfterDot
                divAfterDot = "0"

                if number1copy != "0":
                    number1copy += '0'

    return div


def karatsuba(number1, number2):
    if not number1 or not number2:
        return ""

    number1, number2 = swap(number1, number2)

    if len(number2) == 1:
        if number1 == "0" or number2 == "0":
            return "0"

        multiplied = "0"
        multiplier = int(number2[0])

        while multiplier > 0:
            multiplied = addition(number1, multiplied)
            multiplier -= 1

        return multiplied

    if len(number1) == len(number2) and len(number1) % 2 != 0:
        number1 = '0' + number1

    if len(number2) % 2 != 0:
        number2 = '0' + number2

    n = len(number2)
    nr = len(number1)

    number1FirstHalf = half(number1, 0, nr - (n // 2))
    number1SecondHalf = half(number1, nr - (n // 2), nr)
    number2FirstHalf = half(number2, 0, n // 2)
    number2SecondHalf = half(number2, n // 2, n)

    ac = karatsuba(number1FirstHalf, number2FirstHalf)
    bd = karatsuba(number1SecondHalf, number2SecondHalf)
    ab_cd = subtraction(subtraction(
        karatsuba(addition(number1FirstHalf, number1SecondHalf), addition(number2FirstHalf, number2SecondHalf)), ac),
                        bd)

    for i in range(n):
        ac += '0'

    for i in range(n // 2):
        ab_cd += '0'

    result = addition(addition(ac, ab_cd), bd)

    return result


def multiplication(number1, number2):
    if number1 == "0" or number2 == "0":
        return "0"
    if number1 == "1":
        return number2
    if number2 == "1":
        return number1

    newnumber = ""
    digitsAfterDotNumber1 = 0
    digitsAfterDotNumber2 = 0
    dotFoundNumber1 = False
    dotFoundNumber2 = False
    number1WithoutDecimals = ""
    number2WithoutDecimals = ""

    for i in range(len(number1)):
        if dotFoundNumber1:
            digitsAfterDotNumber1 += 1

        if number1[i] == '.':
            dotFoundNumber1 = True
            i += 1
        else:
            number1WithoutDecimals += number1[i]


    for i in range(len(number2)):
        if dotFoundNumber2:
            digitsAfterDotNumber2 += 1
        if number2[i] == '.':
            dotFoundNumber2 = True
            i += 1
        else:
            number2WithoutDecimals += number2[i]


    number1WithoutDecimals = removeZeros(number1WithoutDecimals)
    number2WithoutDecimals = removeZeros(number2WithoutDecimals)
    newnumber = karatsuba(number1WithoutDecimals, number2WithoutDecimals)

    if digitsAfterDotNumber1 or digitsAfterDotNumber2:
        totalDecimals = digitsAfterDotNumber1 + digitsAfterDotNumber2
        position = len(newnumber) - 1

        if totalDecimals > 20:
            position -= (totalDecimals - 20)

        multiplied = ""

        while totalDecimals > 0:
            if position >= 0:
                multiplied = newnumber[position] + multiplied
                position -= 1
            else:
                multiplied = '0' + multiplied

            totalDecimals -= 1

        multiplied = '.' + multiplied

        if totalDecimals == len(newnumber):
            multiplied = '0' + multiplied
        else:
            while position >= 0:
                multiplied = newnumber[position] + multiplied
                position -= 1

        newnumber = multiplied

    if newnumber[0] == '.':
        newnumber = '0' + newnumber

    i = len(newnumber) - 1
    if '.' in newnumber:
        while i >= 0:
            if newnumber[i] == '0':
                newnumber = newnumber[:i]
            elif newnumber[i] == '.':
                newnumber = newnumber[:i]
                break
            else:
                break

            i -= 1

    return newnumber


def power(base, pwr):
    if pwr == 0:
        return "1"

    pwrNr = base

    pwr -= 1

    while pwr > 0:
        pwrNr = multiplication(pwrNr, base)
        pwr -= 1

    return pwrNr


def modulo(number, baseH):
    baseHString = str(baseH)

    while not less(number, baseHString):
        number = subtraction(number, baseHString)

    return number


def baseBtobase10(number, baseB, steps):
    if baseB == 10:
        return number, steps

    firstHalf = ""
    secondHalf = ""
    position = 0

    steps = steps + "Base " + str(baseB) + " to Base 10 steps: \n\n"

    while position < len(number) and number[position] != '.':
        firstHalf += number[position]
        position += 1

    position += 1

    for i in range(position, len(number)):
        secondHalf += number[i]

    pwr = len(firstHalf) - 1
    newnumber = "0"
    position = 0

    if pwr > 1:
        steps = steps + firstHalf[0] + " * " + str(baseB) + "^" + str(pwr) + " + ... + " + firstHalf[pwr] + " * " + str(baseB) + "^0" 

    if pwr == 1:
        steps = steps + firstHalf[0] + " * " + str(baseB) + "^1 + " + firstHalf[1] + " * " + str(baseB) + "^0"

    if pwr == 0:
        steps = steps + firstHalf[0] + " * " + str(baseB) + "^0"

    while pwr > -1:
        figure = ""

        if number[position] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            figure = str(ord(number[position]) - 55)
        else:
            figure = number[position]

        baseBString = str(baseB)
        multip = multiplication(figure, power(baseBString, pwr))
        newnumber = addition(newnumber, multip)
        pwr -= 1
        position += 1

    position += 1
    pwr = len(secondHalf)
    if pwr == 1:
        steps = steps + " + " + secondHalf[0] + " * " + str(baseB) + "^(-1)"
    if pwr == 2:
        steps = steps + " + " + secondHalf[0] + " * " + str(baseB) + "^(-1)" + " + " + secondHalf[1] + " * " + str(baseB) + "^(-2)"
    if pwr > 2:
        steps = steps + " + " + secondHalf[0] + " * " + str(baseB) + "^(-1)" + " + ... + " + secondHalf[pwr - 1] + " * " + str(baseB) + "^(-" + str(pwr) + ")"
    for i in range(1, pwr + 1):
        figure = ""

        if number[position] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            figure = str(ord(number[position]) - 55)
        else:
            figure = number[position]

        baseBString = str(baseB)
        divis = division("1", power(baseBString, i))
        multip = multiplication(figure, divis)
        newnumber = addition(newnumber, multip)
        position += 1

    i = len(newnumber) - 1

    while i >= 0 and newnumber[i] == '0':
        newnumber = newnumber[:-1]
        i -= 1

    if not newnumber:
        newnumber = "0"
    steps = steps + " = " + newnumber + "\n\n"
    return newnumber, steps


def base10tobaseH(number, baseH, steps):
    if baseH == 10:
        return number, steps

    baseHString = str(baseH)
    justZecimalsOfNumber = ""
    justDecimalsOfNumber = "0"
    i = 0

    steps = steps + "Base 10 to Base " + str(baseH) + " steps: \n\n"

    while i < len(number) and number[i] != '.':
        justZecimalsOfNumber += number[i]
        i += 1

    while i < len(number):
        justDecimalsOfNumber += number[i]
        i += 1

    result = ""
    mod = ""

    check = 1

    while not less(justZecimalsOfNumber, baseHString):
        mod = modulo(justZecimalsOfNumber, baseH)

        if int(mod) > 9:
            str_val = chr(ord('A') + (int(mod) - 10))
            result = str_val + result
        else:
            result = mod + result
        sub = subtraction(justZecimalsOfNumber, mod)
        div = division(sub, baseHString)
        if check < 3:
            steps = steps + justZecimalsOfNumber + " % " + baseHString + " = " + mod + " |<>| " +  justZecimalsOfNumber + " / " + baseHString + " = " + div + "\n"
        elif check == 3:
            steps = steps + ".\n.\n.\n"
        check += 1
        justZecimalsOfNumber = div
    
    mod = modulo(justZecimalsOfNumber, baseH)
    steps = steps + justZecimalsOfNumber + " % " + baseHString + " = " + mod + " |<>| " +  justZecimalsOfNumber + " / " + baseHString + " = 0\n"

    if int(mod) > 9:
        str_val = chr(ord('A') + (int(mod) - 10))
        result = str_val + result
    else:
        result = mod + result

    if justDecimalsOfNumber != "0":
        steps = steps + "\n"
        result += '.'
        precision = 19

        check = 1

        resWOzec = ""
        resWOdec = "0"

        while precision > 0 and justDecimalsOfNumber != "0":
            resWOdec = ""
            resWOzec = "0"
            nr = multiplication(justDecimalsOfNumber, baseHString)
            i = 0

            while i < len(nr) and nr[i] != '.':
                resWOdec += nr[i]
                i += 1

            while i < len(nr):
                resWOzec += nr[i]
                i += 1

            if int(resWOdec) > 9:
                str_val = chr(ord('A') + (int(resWOdec) - 10))
                result = result + str_val
            else:
                result = result + resWOdec

            if check < 3:
                steps = steps + justDecimalsOfNumber + " * " + baseHString + " = " + resWOdec + " + " + resWOzec + "\n"
            elif check == 3:
                steps = steps + ".\n.\n.\n"
            precision -= 1
            if precision == 0:
                steps = steps + justDecimalsOfNumber + " * " + baseHString + " = " + resWOdec + " + " + resWOzec + \
                    " <!> STOP! Max precision reached."
            justDecimalsOfNumber = resWOzec
            check += 1
        if precision != 0:
            steps = steps + justDecimalsOfNumber + " * " + baseHString + " = " + resWOzec
    return result, steps


def converter(number, baseB, baseH):
    if len(number) == 0:
        return "", ""
    if number == "Enter the number":
        return "", ""
    if number[0] == '.' or number[0] == ',':
        return "Incorrect number", ""

    if len(number) > 2:
        if number[0] == '0' and number[1] in "123456789":
            return "Incorrect number", ""

    dotFound = False

    for i in range(len(number)):
        if number[i] in "abcdefghijklmnopqrstuvwxyz":
            number = number[:i] + number[i].upper() + number[i + 1:]

        if number[i] == ',':
            number = number[:i] + '.' + number[i + 1:]

        if number[i] == '.':
            if not dotFound:
                dotFound = True
            else:
                return "Incorrect number", ""

        if number[i] not in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.":
            return "Incorrect number", ""

        if number[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if ord(number[i]) - 55 >= baseB:
                return "Incorrect number", ""

        if number[i] in "0123456789":
            if ord(number[i]) - 48 >= baseB:
                return "Incorrect number", ""

        if i == len(number) - 1 and number[i] == '.':
            return "Incorrect number", ""

    steps = ""
    number, steps = baseBtobase10(number, baseB, steps)
    number, steps = base10tobaseH(number, baseH, steps)
    return number, steps
