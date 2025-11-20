def MFT(mem_size, part_size, processes):
    partitions = mem_size // part_size
    result = []
    for i, p in enumerate(processes, start=1):
        ok = p <= part_size
        result.append((i, p, ok))
    return partitions, result


def MVT(mem_size, processes):
    remain = mem_size
    alloc = []
    for i, p in enumerate(processes, start=1):
        if p <= remain:
            alloc.append((i, p, True, remain - p))
            remain -= p
        else:
            alloc.append((i, p, False, remain))
    return alloc, remain


if __name__ == "__main__":
    mem = int(input("Enter memory size for MFT: "))
    ps = int(input("Enter partition size: "))
    n = int(input("Number of processes: "))
    procs = [int(input(f"Process {i+1}: ")) for i in range(n)]

    parts, res = MFT(mem, ps, procs)
    print("\nMFT Results:")
    for r in res:
        print(r)

    mem2 = int(input("\nEnter memory size for MVT: "))
    m = int(input("Number of processes: "))
    pro2 = [int(input(f"Process {i+1}: ")) for i in range(m)]

    alloc, remain = MVT(mem2, pro2)
    print("\nMVT Results:")
    for a in alloc:
        print(a)

    print("Remaining:", remain)
