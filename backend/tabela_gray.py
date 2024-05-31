def gray_code(n):
    gray = ['0', '1']
    for i in range(2, n + 1):
        gray = gray + gray[::-1]
        for j in range(len(gray) // 2):
            gray[j] = '0' + gray[j]
        for j in range(len(gray) // 2, len(gray)):
            gray[j] = '1' + gray[j]
    return gray
