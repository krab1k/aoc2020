max_seat_id = -1
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        row_str = line[:7]
        col_str = line[7:]

        row_bin = ''.join('0' if c == 'F' else '1' for c in row_str)
        col_bin = ''.join('0' if c == 'L' else '1' for c in col_str)

        row = int(row_bin, 2)
        col = int(col_bin, 2)
        seat_id = row * 8 + col
        if seat_id > max_seat_id:
            max_seat_id = seat_id

print(max_seat_id)

