"""
Task 1: Priority (non-preemptive) and Round Robin scheduling simulation.
Outputs WT, TAT and average times. Also prints a simple Gantt timeline.
"""
from collections import deque

def priority_scheduling(processes):
    # processes: list of tuples (pid, burst, priority)
    procs = sorted(processes, key=lambda x: x[2])  # sort by priority (lower first)
    time = 0
    results = []
    total_wt = 0
    total_tat = 0
    gantt = []
    for pid, bt, pr in procs:
        wt = time
        tat = wt + bt
        results.append((pid, bt, pr, wt, tat))
        total_wt += wt
        total_tat += tat
        gantt.append((pid, time, time + bt))
        time += bt
    n = len(processes)
    avg_wt = total_wt / n
    avg_tat = total_tat / n
    return results, avg_wt, avg_tat, gantt

def round_robin(processes, quantum):
    # processes: list of tuples (pid, burst)
    queue = deque()
    for pid, bt in processes:
        queue.append([pid, bt])
    time = 0
    remaining = {pid: bt for pid, bt in processes}
    completion_time = {}
    gantt = []
    # Keep arrival all at time 0 for simplicity (classical RR).
    while queue:
        pid, rem = queue.popleft()
        exec_time = min(rem, quantum)
        gantt.append((pid, time, time + exec_time))
        time += exec_time
        rem -= exec_time
        if rem == 0:
            completion_time[pid] = time
        else:
            queue.append([pid, rem])
    results = []
    total_wt = 0
    total_tat = 0
    for pid, bt in processes:
        tat = completion_time[pid]  # arrival 0
        wt = tat - bt
        results.append((pid, bt, wt, tat))
        total_wt += wt
        total_tat += tat
    n = len(processes)
    avg_wt = total_wt / n
    avg_tat = total_tat / n
    return results, avg_wt, avg_tat, gantt

def print_priority(results, avg_wt, avg_tat, gantt):
    print("Priority Scheduling (non-preemptive)")
    print("PID\tBT\tPR\tWT\tTAT")
    for pid, bt, pr, wt, tat in results:
        print(f"{pid}\t{bt}\t{pr}\t{wt}\t{tat}")
    print(f"Average WT: {avg_wt:.2f}, Average TAT: {avg_tat:.2f}")
    # simple gantt
    print("Gantt:", " ".join(f"|P{pid}:{start}->{end}" for pid, start, end in gantt))

def print_rr(results, avg_wt, avg_tat, gantt):
    print("Round Robin Scheduling")
    print("PID\tBT\tWT\tTAT")
    for pid, bt, wt, tat in results:
        print(f"{pid}\t{bt}\t{wt}\t{tat}")
    print(f"Average WT: {avg_wt:.2f}, Average TAT: {avg_tat:.2f}")
    print("Gantt:", " ".join(f"|P{pid}:{start}->{end}" for pid, start, end in gantt))

if __name__ == "__main__":
    # Example interactive usage
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        pr = int(input(f"Enter Priority (lower number = higher priority) for P{i+1}: "))
        processes.append((i+1, bt, pr))

    # Priority (non-preemptive)
    pr_results, pr_avg_wt, pr_avg_tat, pr_gantt = priority_scheduling(processes)
    print()
    print_priority(pr_results, pr_avg_wt, pr_avg_tat, pr_gantt)

    # Round Robin - reuse bursts only
    print()
    q = int(input("Enter time quantum for Round Robin: "))
    rr_input = [(pid, bt) for pid, bt, _ in processes]
    rr_results, rr_avg_wt, rr_avg_tat, rr_gantt = round_robin(rr_input, q)
    print()
    print_rr(rr_results, rr_avg_wt, rr_avg_tat, rr_gantt)
