#!/usr/bin/python2

from __future__ import division


class TempTracker(object):
    def __init__(self):
        self.t_max = None
        self.t_min = None
        self.t_mode = None

        self.t_num = 0
        self.t_sum = 0
        self.t_rept = [0] * (110 + 1)

    def insert(self, t):
        # TODO: Validate input

        # Recalculate max and min
        if t > self.t_max:
            self.t_max = t
        if t < self.t_min:
            self.t_min = t

        # Update values for mean
        self.t_sum += self.t_sum + t
        self.t_num += self.t_num + 1

        # Update values for mode
        self.t_rept[t] += 1
        return

    def get_max(self):
        return self.t_max

    def get_min(self):
        return self.t_min

    def get_mean(self):
        return self.t_sum / self.t_num

    def get_mode(self):
        return self.t_rept.index(max(self.t_rept))


if __name__ == "__main__":
    tt = TempTracker()
    for i in xrange(110 + 1):
        tt.insert(i)

    print tt.get_max()
    print tt.get_min()
    print tt.get_mean()
    print tt.get_mode()

    #Returns weird values
