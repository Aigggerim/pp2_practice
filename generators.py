#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even_numbers_generator(N):
    for i in range(N+1):
        if i%2 == 0:
            yield i


N = int(input("Enter a number: "))
even_numbers = even_numbers_generator(N)
print(','.join(map(str, even_numbers)))

#Create a generator that generates the squares of numbers up to some number N.

def generate_square(N):
    for i in range(N):
        yield i ** 2

N = int(input("Enter a number (N): "))
square_generator = generate_square(N)

for square in square_generator:
    print(square)
