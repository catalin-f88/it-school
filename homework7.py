from pathlib import Path

result = [0, 1]
def fibonacci(n):
    """ Calculate current Fibonacci value and append it to array <result> """
    if n < 0:
        print("Incorrect input")
    elif n < len(result):
        return result[n]
    else:       
        result.append(fibonacci(n - 1) + fibonacci(n - 2))
        return result[n]
count = 100
fibonacci(count)

script_path = Path(__file__)
result_path = script_path.parent / "fibonacci_result"
result_path.mkdir(exist_ok=True, parents=True)

current = 1

while current < count:
    for i in result:
        filename = str(current) + ".txt"
        with open(result_path / filename, "w") as fout:
            fout.write(f"Current Fibonacci iteration: {current} \n Fibonacci sequence result: {i}")
        current += 1

print("Script ENDED")











# while current <= count:
#     for i in result:
#         filename = str(i) + ".txt"
#         with open(result_path / filename, "w") as fout:
#             fout.write(f"Current Fibonacci iteration:\n {current}")
#         current += 1