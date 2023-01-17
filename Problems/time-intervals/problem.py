def min_rooms(intervals):
    intervals = sorted(intervals)
    end_times = []
    min_rooms = 0
    for interval in intervals:
        room_avaliable = False
        for i, end_time in enumerate(end_times):
            if end_time <= interval[0]:
                end_times[i] = interval[1]
                room_avaliable = True
                break
        if not room_avaliable:
            end_times.append(interval[1])
            min_rooms += 1
    return min_rooms