def allocate_memory(partitions, processes, strategy):
    parts = partitions[:]
    allocation = [-1] * len(processes)

    for i, p in enumerate(processes):

        idx = -1
        if strategy == "first":
            for j, part in enumerate(parts):
                if part >= p:
                    idx = j
                    break

        elif strategy == "best":
            best_idx = -1
            best_size = None
            for j, part in enumerate(parts):
                if part >= p and (best_size is None or part < best_size):
                    best_size = part
                    best_idx = j
            idx = best_idx

        elif strategy == "worst":
            worst_idx = -1
            worst_size = -1
            for j, part in enumerate(parts):
                if part >= p and part > worst_size:
                    worst_size = part
                    worst_idx = j
            idx = worst_idx

        if idx != -1:
            allocation[i] = idx
            parts[idx] -= p

    return allocation, parts


if __name__ == "__main__":
    parts = list(map(int, input("Enter partition sizes: ").split()))
    processes = list(map(int, input("Enter process sizes: ").split()))

    for s in ("first", "best", "worst"):
        alloc, remain = allocate_memory(parts, processes, s)
        print(f"\n{s.title()} Fit Allocation: {alloc}")
        print("Remaining:", remain)
