seats = set()
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
        seats.add(seat_id)

all_seats = set(range(min(seats), max(seats) + 1))
print(all_seats - seats)
