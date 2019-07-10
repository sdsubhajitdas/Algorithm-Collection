# For sorted Input - O(n)
# For unsorted Input - O(nlog n)


def activity_selection(activity: list):
    job_order = list()
    activity.sort(key=lambda x: x[1])
    job_order.append(activity[0][-1])
    time = activity[0][1]

    for start, end, jid in activity[1:]:
        if(start >= time):
            job_order.append(jid)
            time = end

    return job_order


def main():
    # [Start Time, End Time, Job ID]
    activity = [
        [0, 6, 1],
        [3, 4, 2],
        [1, 2, 3],
        [5, 9, 4],
        [5, 7, 5],
        [8, 9, 6]
    ]

    print(*activity_selection(activity), sep=' -> ')


if __name__ == "__main__":
    main()
