def print_gameboard(gameboard, block_size=3):
    row_line = (block_size ** 2) * 4 + 1
    print(row_line * "=")

    for row_idx, row in enumerate(gameboard):

        print("║", end="")
        for col_idx, n in enumerate(row):
            print("",n if n else " ", "|" if (col_idx + 1) % block_size else "║", end="")

        print()
        print(row_line * ("-" if (row_idx + 1) % block_size else "="))

default_gameboard = [
  [None, None, None, 2, 6, None, 7, None, 1],
  [6, 8, None, None, 7, None, None, 9, None],
  [1, 9, None, None, None, 4, 5, None, None],
  [8, 2, None, 1, None, None, None, 4, None],
  [None, None, 4, 6, None, 2, 9, None, None],
  [None, 5, None, None, None, 3, None, 2, 8],
  [None, None, 9, 3, None, None, None, 7, 4],
  [None, 4, None, None, 5, None, None, 3, 6],
  [7, None, 3, None, 1, 8, None, None, None]
]
