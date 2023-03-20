# list1 = [
#     [1, 2],
#     [3, 4, 2, 4],
#     [2, 3, 3, 4]
# ]
# for i in list1:
#     try:
#         val = i[2]
#     except IndexError:
#         print(f"Nu am gasit indexul 2 in lista {i}.")
#     else:
#         print(val)
#     finally:
#         print("--------------------")

# print("END")
import utils.logger as logger

def circle_area(radius):
    """ Calculate circle area. Radius has to be positive integer.
    
    Args: 
        - radius (float): Circle radius
    
    Raises:
        - ValueError:  if radius is less than 0 """
    

    if radius < 0:
        raise ValueError(f"Raza trebuie sa fie mai mare decat zero. Input {radius}")
    
    return 3.14 * (radius ** 2)

try:
    number = float(input("Raza cerc: "))
except ValueError:
    print("[CRITICAL] Please input a float or integer.")
else:
    try:
        print(circle_area(number))
    except (ValueError, TypeError) as err:
        logger.error(err)

print("END")