def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def menu():
    print("\n--- ALGORİTMA MENÜSÜ ---")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Linear Search")
    print("5. Binary Search")
    print("6. Factorial")
    print("7. Fibonacci")
    print("8. Prime Check")
    print("0. Çıkış")


while True:
    menu()
    choice = int(input("Seçimin: "))

    if choice == 0:
        print("Çıkılıyor...")
        break

    elif choice in [1,2,3]:
        arr = list(map(int, input("Sayıları gir (boşluklu): ").split()))

        if choice == 1:
            print("Sonuç:", bubble_sort(arr))
        elif choice == 2:
            print("Sonuç:", selection_sort(arr))
        elif choice == 3:
            print("Sonuç:", insertion_sort(arr))

    elif choice in [4,5]:
        arr = list(map(int, input("Sayıları gir (boşluklu): ").split()))
        target = int(input("Aranan sayı: "))

        if choice == 4:
            print("Index:", linear_search(arr, target))
        else:
            arr.sort()
            print("Sıralı liste:", arr)
            print("Index:", binary_search(arr, target))

    elif choice == 6:
        n = int(input("Sayı: "))
        print("Sonuç:", factorial(n))

    elif choice == 7:
        n = int(input("Kaç terim: "))
        print("Fibonacci:", fibonacci(n))

    elif choice == 8:
        n = int(input("Sayı: "))
        print("Asal mı?:", is_prime(n))

    else:
        print("Geçersiz seçim!")
