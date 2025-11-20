def sequential_allocation():
    total_blocks = int(input("Enter total no. of blocks: "))
    block_status = [0] * total_blocks
    n = int(input("Enter number of files: "))

    for i in range(1, n + 1):
        print(f"\nFile {i}")
        start = int(input("Starting block: "))
        length = int(input("Length: "))
        valid = True
        for j in range(start, start + length):
            if j >= total_blocks or block_status[j] == 1:
                valid = False
                break
        if valid:
            for j in range(start, start + length):
                block_status[j] = 1
            print("File allocated successfully.")
        else:
            print("Allocation failed.")

    print("\nFinal Block Allocation Map:")
    print(block_status)

if __name__ == "__main__":
    sequential_allocation()
