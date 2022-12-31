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
alc_store = pd.read_csv(
    './data/org/서울시 강동구 유흥주점영업 인허가 정보.csv', encoding='cp949')
alc_store = alc_store[alc_store['영업상태명'] == '영업/정상']
find_xy(alc_store, '도로명주소', '사업장명').to_csv("./data/alc_store.csv", index=False)

# 일반음식점 (norm_store)
norm_store = pd.read_csv(
    './data/org/서울시 강동구 일반음식점 인허가 정보.csv', encoding='cp949')
norm_store = norm_store[norm_store['영업상태명'] == '영업/정상']
find_xy(norm_store, '도로명주소', '사업장명').to_csv(
    "./data/norm_store.csv", index=False)
    
# 학원 (academy)
academy = pd.read_csv(
    './data/org/서울시 강동구 일반음식점 인허가 정보.csv', encoding='cp949')
find_xy(academy, '도로명주소', '학원명').to_csv("./data/academy.csv", index=False)
