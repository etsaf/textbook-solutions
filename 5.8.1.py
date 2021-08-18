def drawLine(screen, width, x1, x2, y):
    work = byte[len(byte) - y - 1]
    head = x1 % 8
    tail = x2 % 8
    first_full = x1 // 8 + 1
    if not head:
        firts_full -= 1
    last_full = x2 // 8 - 1
    if tail == 7:
        last_full -= 1
    for i in range(first_full, last_full + 1):
        screen[(width // 8) * y + i] = 0xff
    head_mask = 0xff >> head
    tail_mask = ~ (0xff >> (tail + 1))
    if x1 // 8 == x2 // 8:
        mask = head_mask & tail_mask
        screen[(width // 8) * y + x1 / 8] |= mask
    else:
        if head != 0:
            ind = (width // 8) * y + first_full - 1
            screen[ind] |= head_mask
        if tail != 7:
            ind = (width // 8) * y + last_full + 1
            screen[ind] |= tail_mask