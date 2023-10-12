def main():
    n = int(input("what is n? "))
    for i in range(n):
        print(sheep(i))

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("boz "*i)
    yield flock

if __name__=="__main__":
    main()


