from collections import defaultdict
from math import ceil

def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees
    entrance_exit_infos = defaultdict(list)
    fee_infos = {}

    for record in records:
        curr_time = (int(record[:2]) * 60) + int(record[3:5]) # hour * 60 + min
        number_plate = record[6:10]
        entrance_exit_infos[number_plate] += [curr_time]

    for car_number in entrance_exit_infos.keys():
        # 출차 기록이 없는 경우
        if len(entrance_exit_infos[car_number]) % 2 == 1:
            entrance_exit_infos[car_number] += [23 * 60 + 59]
        used_time = 0
        for i in range(0, len(entrance_exit_infos[car_number]), 2):
            used_time += entrance_exit_infos[car_number][i + 1] - entrance_exit_infos[car_number][i]
        # 요금 계산
        if used_time <= basic_time:
            fee_infos[car_number] = basic_fee
        else:
            total_fee = basic_fee
            total_fee += ceil((used_time - basic_time) / unit_time) * unit_fee
            fee_infos[car_number] = total_fee

    return [i[1] for i in list(sorted(fee_infos.items()))]
    

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))