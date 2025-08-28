# python3

# from collections import namedtuple
import heapq

# AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    result = []
    # Min-heap to track the next available time for each worker
    heap = [(0, i) for i in range(n_workers)]  # (next_free_time, worker_index)
    heapq.heapify(heap)

    for job in jobs:
        # Pop the worker with the earliest available time
        free_time, worker = heapq.heappop(heap)
        # The worker starts the job at the current free time
        result.append((worker, free_time))
        # The worker will be free after processing this job
        heapq.heappush(heap, (free_time + job, worker))

    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for worker, start_time in assigned_jobs:
        print(worker, start_time)


if __name__ == "__main__":
    main()