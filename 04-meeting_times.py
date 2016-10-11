#!/usr/bin/python2


def condence_meeting_times(n):
    n_sorted = sorted(n)
    n_merged = []
    curr_start = n_sorted[0][0]
    curr_finish = n_sorted[0][1]
    for mtg in range(1, len(n_sorted)):
        new_start = n_sorted[mtg][0]
        new_finish = n_sorted[mtg][1]
        if curr_finish >= new_start:
            curr_finish = new_finish
            # Throw values for last meeting
            if mtg == len(n_sorted)-1:
                n_merged.append((curr_start, curr_finish))
            continue
        n_merged.append((curr_start, curr_finish))
        curr_start = new_start
        curr_finish = new_finish

    return n_merged


if __name__ == "__main__":
    n = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    print condence_meeting_times(n)
