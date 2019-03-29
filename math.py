import math
def maths(number):
    if number % 2 == 0 and number > 2: 
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))

def main():
    print(maths(37))
    print(maths(100))
    print(maths(77))

if __name__ == '__main__':
	main()
