# import sys

# if sys.version_info.major < 3:
#     print(f"Versiunea {sys.version_info.major} nu este suportata")
#     sys.exit(1)

# try:
#     print(sys.argv[1][::-1] * int(sys.argv[2]))
# except IndexError:
#     print("Argumentul nu exista")
#     sys.exit(1)
# except ValueError:
#     print("Tip argument incorect")
#     sys.exit(1)

import argparse
print("Hello!")

argparser = argparse.ArgumentParser()

argparser.add_argument("symbol", type=str)
argparser.add_argument("multiplier", type=int)
argparser.add_argument("separator", type=str)

args = argparser.parse_args()

print(f"{args.symbol}{args.separator}" * int(args.multiplier))

print("Bye!")