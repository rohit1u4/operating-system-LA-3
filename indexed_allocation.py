def indexed_allocation():
    total = int(input("Enter total number of blocks: "))
    block_status = [0] * total
    n = int(input("Enter number of files: "))

    for i in range(1, n + 1):
        print(f"\nFile {i}")
        index = int(input("Enter index block: "))
        if block_status[index] == 1:
            print("Index block already used.")
            continue

        count = int(input("Enter number of data blocks: "))
        data = list(map(int, input("Enter data block numbers: ").split()))

        if len(data) != count:
            print("Mismatch in data block count.")
            continue

        flag = False
        for b in data:
            if b >= total or block_status[b] == 1:
                flag = True
                break

        if flag:
            print("Allocation Failed.")
        else:
            block_status[index] = 1
            for b in data:
                block_status[b] = 1
            print("Indexed File Allocated.")

    print("\nFinal Allocation Map:")
    print(block_status)

if __name__ == "__main__":
    indexed_allocation()
