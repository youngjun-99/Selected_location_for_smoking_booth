import pandas as pd

from utils import find_xy, get_api, trans_wtm2wgs84

# 서울 전체 생활인구수 1년치 합치기 / 구 코드
people = pd.read_csv('./data/org/LOCAL_PEOPLE_GU_2021.csv', encoding='euc-kr')
people = people[['시간대구분', '자치구코드', '총생활인구수']]

g_value_data = list()
for gcode in dict.fromkeys(people['자치구코드']).keys():
    value = people[people['자치구코드'] == gcode]['총생활인구수'].sum()
    g_value_data.append([str(gcode), value])

code = pd.read_csv('./data/org/법정동코드_조회자료.csv', encoding='cp949')

dcode_name = list()
for dcode, name in zip(code['법정동코드'], code['법정동명']):
    key = name.split()
    if len(key) == 2:
        key = key[1]
        dcode = str(dcode)[:5]
        dcode_name.append([dcode, key])

g_value_df = pd.DataFrame(g_value_data, columns=['자치구코드', '총생활인구수'])
code_name_df = pd.DataFrame(dcode_name, columns=['자치구코드', '법정구명'])
pd.merge(g_value_df, code_name_df, on='자치구코드', how='inner').to_csv(
    "./data/seoul_people.csv", index=False)

# 유흥주점영업 (alc_store)
bar = pd.read_csv(
    './data/org/서울시 강동구 유흥주점영업 인허가 정보.csv', encoding='cp949')
bar = bar[bar['영업상태명'] == '영업/정상']
find_xy(bar, '도로명주소', '사업장명').to_csv("./data/bar.csv", index=False)

# 일반음식점 (norm_store)
restaurant = pd.read_csv(
    './data/org/서울시 강동구 일반음식점 인허가 정보.csv', encoding='cp949')
restaurant = restaurant[restaurant['영업상태명'] == '영업/정상']
restaurant = find_xy(restaurant, '도로명주소', '사업장명')
restaurant[restaurant['lat'] != 'x좌표없음'].to_csv("./data/smoke_point.csv", index=False)

# 학원 (academy)
academy = pd.read_csv(
    './data/org/서울시 강동구 학원 교습소정보.csv', encoding='cp949')
academy = find_xy(academy, '도로명주소', '학원명')
academy[academy['lat'] != 'x좌표없음'].to_csv("./data/academy.csv", index=False)

# 금연구역 필요한 정보만 (none_smoke_area)
none_smoke_area = pd.read_csv(
    './data/org/서울시 금연구역  정보(표준 데이터).csv', encoding='cp949')
none_smoke_area = none_smoke_area[none_smoke_area['시군구명'] == '강동구']
none_smoke_area = none_smoke_area[['금연구역명', '위도', '경도']].reset_index(drop=True)
none_smoke_area.to_csv("./data/none_smoke_area.csv", index=False)

# 어린이 보호구역 (child_safe)
child_safe = pd.read_csv(
    './data/org/서울특별시_어린이_보호구역_지정현황_20201231.csv', encoding='cp949')
child_safe = child_safe[child_safe['자치구명'] == '강동구']
find_xy(child_safe, '도로명 주소(동명)', '시설명').to_csv("./data/child_safe.csv", index=False)

#흡연구역
smoke_point = pd.read_csv(
    './data/org/seoul_smoke_point.csv', encoding='cp949')
smoke_point = find_xy(smoke_point, '흡연구역', '시설명')
smoke_point[smoke_point['lat'] != 'x좌표없음'].to_csv("./data/smoke_point.csv", index=False)