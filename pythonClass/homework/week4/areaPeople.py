# 행정동명 행정동코드 위도 경도
# 압구정동 11680545 37.530734 127.028461
# 혜화동 11110650 37.587817 127.001745
# 평창동 11110560 37.613029 126.974485
# 이태원1동 11170650 37.532612 126.990182
# 한남동 11170685 37.537541 127.005165
# 능동 11215780 37.550578 127.081722
# 성북동 11290525 37.597248 126.992899
# 신사동 11680510 37.523807 127.026492
# 청담동 11680565 37.524399 127.050457
# 삼성1동 11680580 37.514315 127.062824

# 1. 위의 10개 동의 시간대별 총생활인구의 평균을 구하여 꺽은 선 그래프에 10개 동의 그래프를 그립니다.
#
# 그래프의 경우 친절한 정보가 많이 포함되어야 합니다. ^^

# 2. 위의 정보와 서울시 생활인구 데이터를 이용하여 지도에 결과를 표시합니다.
# 마커를 표시하되, 오후 6시 기준 가장 평균이 높은 동의 경우 아이콘의 색상이 Red, 평균이 높은 쪽에 속할 수록 아이콘의 색상이 Red에 가까운 색으로 표시하고, 가장 평균이 가장 낮은 동의 경우 아이콘 색상이 Blue, 평균이 낮은 쪽에 속할 수록 Blue에 가까운 색으로 표시하도록 합니다.
#
# 아이콘은 10개 동이 모두 서로 다른 모양이어야 합니다.
#
# 마커에 마우스가 올라가면 해당동 이름이 뜨면 됩니다.
#
# --------- 해당 과제에 대해 궁금한 점이 있으면 즉시 문의하시기 바랍니다.

import csv

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

f1 = open('C:\csv\dong_code.csv', encoding='UTF-8')
f2 = open('C:\csv\LOCAL_PEOPLE_DONG_202208.csv', encoding='UTF-8')

data1 = csv.reader(f1)
people = csv.reader(f2)
next(data1)
next(people)
data1 = list(data1)
people = list(people)

map_data = {
    11680545: [37.530734, 127.028461], # 압구정동
    11110650: [37.587817, 127.001745], # 혜화동
    11110560: [37.613029, 126.974485], # 평창동
    11170650: [37.532612, 126.990182], # 이태원1동
    11170685: [37.537541, 127.005165], # 한남동
    11215780: [37.530734, 127.028461], # 능동
    11290525: [37.550578, 127.081722], # 성북동
    11680510: [37.530734, 127.028461], # 신사동
    11680565: [37.523807, 127.026492], # 청담동
    11680580: [37.514315, 127.062824] # 삼성1동
}
month = ["0시", "1시", "2시", "3시", "4시", "5시", "6시", "7시", "8시", "9시", "10시", "11시", "12시", "13시", "14시", "15시", "16시", "17시", "18시", "19시", "20시", "21시", "22시", "23시"]

name = {
    11680545: "압구정동",
    11110650: "혜화동",
    11110560: "평창동",
    11170650: "이태원1동",
    11170685: "한남동",
    11215780: "능동",
    11290525: "성북동",
    11680510: "신사동",
    11680565: "청담동",
    11680580: "삼성1동"
}

result = {
    11680545: [0 for i in range(24)], # 압구정동
    11110650: [0 for i in range(24)], # 혜화동
    11110560: [0 for i in range(24)], # 평창동
    11170650: [0 for i in range(24)], # 이태원1동
    11170685: [0 for i in range(24)], # 한남동
    11215780: [0 for i in range(24)], # 능동
    11290525: [0 for i in range(24)], # 성북동
    11680510: [0 for i in range(24)], # 신사동
    11680565: [0 for i in range(24)], # 청담동
    11680580: [0 for i in range(24)] # 삼성1동
}

for key in map_data.keys():
    for row in people:
        time = int(row[1]) # 0, 1, 2 ... 23
        dong = int(row[2]) # 123213123, 1232321123, 12312313...
        total = float(row[3]) # 23.2222222, 34.333333...
        if key == dong:
            result[dong][time] += total

for row in result.values():
    for data in row:
        data /= 31

for key, value in result.items():
    plt.plot(month, value, label=name[key])

plt.title("10개 동의 시간대별 총생활인구의 평균")

plt.xlabel("시간대")
plt.ylabel("인구수")

plt.legend()

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])

plt.show()