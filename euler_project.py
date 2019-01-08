import timeit


def problem1(num):

    sum = 0

    for i in range(1,num):
        if i%3 == 0 or i%5 == 0:
            sum += i
    print(sum)


def problem2(upperBound):

    fib = [1, 2]
    i = 1
    sum = 2

    while True:
        fibNum = fib[i] + fib[i-1]
        if fibNum < upperBound:
            fib.append(fibNum)
            if fibNum%2 == 0:
                sum += fibNum
        else:
            break
        i += 1
    print(sum)


def problem3(number):
    primes = [2,3,5,7,11]
    primeFactors = []

    if number > 1000000:
        bound = 10000
    else:
        bound = 1000

    #generate primes
    for i in range(12,bound):

        if i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0 or i%11 == 0:
            pass
        else:
            primes.append(i)

    #prime factorization
    i = 0
    while True:
        if number % primes[i] == 0:
            primeFactors.append(primes[i])
            number /= primes[i]
            i = 0
        else:
            i += 1
            if i == len(primes):
                break

    print(primeFactors[-1])


def problem4():
    start = timeit.default_timer()
    largest = 0

    for i in range(999,100,-1):
        for j in range(999,100,-1):
            result = i * j
            s = str(result)
            sr = s[::-1]

            if s == sr:
                if result > largest:
                    largest = result

    print(largest)
    stop = timeit.default_timer()
    print('Time:',stop - start)







