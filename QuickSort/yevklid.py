# Qoldiq usuli

def ekub_q(a: int, b: int):
    a = int(a)
    b = int(b)

    # a yoki b nol yoki manfiy emasligini tekshiramiz
    if a <= 0 or b <= 0:
        raise ValueError("Miqdor manfiy yoki 0 bo'lishi mumkin emas. Iltimos 0 dan katta qiymat kiriting.")
    
    if a % b == 0:
        return b

    else:
        j = a % b
        a = b
        b = j
    return ekub_q(a, b)


# Ayirish usuli

def ekub_m(a: int, b: int):
    a = int(a)
    b = int(b)

    # a yoki b nol yoki manfiy emasligini tekshiramiz
    if a <= 0 or b <= 0:
        raise ValueError("Miqdor manfiy yoki 0 bo'lishi mumkin emas. Iltimos 0 dan katta qiymat kiriting.")
    
    if a - b == 0:
        return b
    else:
        if a > b:
            j = a - b
            a = j
        elif b > a:
            j = b - a
            b = j
        return ekub_m(a, b)
