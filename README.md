# Selected_location_for_smoking_booth
산업시스템공학과 캡스톤디자인 - 강동구 흡연부스 입지선정 프로젝트

## Data update with refactoring date : 2022-12-31 ~

## MCLP

Gurobi Solver를 활용하여 Simple MIP(Mixed Integer Linear Programming)를 통해 Maximum Coverage Location Problem 해결

## Requirements

- `geopandas==0.9.0`
- `branca==0.5.0`
- `folium==0.13.0`
- `gurobipy==9.1.2`
- `mip==1.13.0`
- `numpy==1.19.5`
- `pandas==1.1.5`
- `scipy==1.5.4`
- `shapley==1.0.3`
- `selenium==3.141.0`
- `tqdm==4.64.1`

## Data

### Data list
- [skorea_municipalities_geo_simple.json](https://pinkwink.kr/1003)
- [LOCAL_PEOPLE_GU_2021.csv](https://data.seoul.go.kr/dataList/OA-15439/S/1/datasetView.do)
- [법정동코드_조회자료.csv](https://www.code.go.kr/stdcode/regCodeL.do)
- [서울시 금연구역  정보(표준 데이터).csv](http://data.seoul.go.kr/dataList/OA-20339/S/1/datasetView.do;jsessionid=B427F2F55B46591521889D6526E7B96E.new_portal-svr-11)
- [서울시 강동구 유흥주점영업 인허가 정보](http://data.seoul.go.kr/dataList/OA-18576/S/1/datasetView.do)
- [서울시 강동구 일반음식점 인허가 정보](https://data.seoul.go.kr/dataList/OA-18676/S/1/datasetView.do)
- [서울시 강동구 학원 교습소정보](https://data.seoul.go.kr/dataList/OA-20554/S/1/datasetView.do)

### Problem
- seoul_smoke_point > 강동구 데이터 존재하지 않음
