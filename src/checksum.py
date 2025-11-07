def modulo_11_checksum(isbn_number: str) -> bool:
    digits_str = "".join(isbn_number.replace("-", " ").split())

    if len(digits_str) != 10:
        raise Exception(
            "Количество значащих символов, то есть не считая пробелов и тире, в ISBN номере должно равняться 10."
        )
    if not digits_str[:9].isdigit() or digits_str[9] not in "0123456789Xx":
        raise Exception(
            "ISBN может содержать только арабские цифры, а также римскую цифру X для контрольной цифры."
        )

    digits = [int(char) for char in digits_str[:9]]

    check_digit = 10 if digits_str[-1] in "Xx" else int(digits_str[-1])

    total = 0
    weight = 10
    for i in range(len(digits_str) - 1):
        digit = digits[i]
        total += digit * weight
        weight -= 1
    checksum = total + (check_digit * weight)
    return checksum % 11 == 0
