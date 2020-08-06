if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    a=max(arr)
    while max(arr)==a:
        arr.remove(a)
    print(max(arr))
