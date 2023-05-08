from pathlib import Path
import sys

ROOT = Path(__file__).parent

def fib():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b

fib_gen = fib()

try:
    output_path = ROOT / "output"
    output_path.mkdir(exist_ok=True)
except OSError:
    print("Could not create output dir")
    sys.exit(1)

for i in range(1, 101):
    file_path = output_path / f"{i}.txt"
    try:
        with file_path.open("w") as fout:
            fout.write(str(next(fib_gen)))
    except OSError as err:
        print(err)