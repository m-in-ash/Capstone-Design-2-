#%%
import pandas as pd
import folium
import json
import geopandas as gpd

def load_data():
    # 흡연시설 좌표 데이터 불러오기
    # df_facility = pd.read_csv('content/(최종) 서울시 흡연시설 좌표 모음.csv')
    df_facility = pd.read_excel('/Users/jeonghyolim/Desktop/capstone_web/data/흡연구역전체통합본_최종.xlsx')
    df_facility.dropna(subset=['위도','경도'], inplace=True)

    # 행정동 경계를 담고 있는 GeoJSON 파일 읽어오기
    # with open('content/seoul_dong.json', 'r', encoding='utf-8') as f:
    with open('/Users/jeonghyolim/Desktop/capstone_web/data/seoul_municipalities_geo_simple.json', 'r', encoding='utf-8') as f:
        district = json.load(f)

    # 생활인구 데이터 불러오기
    df_pop = pd.read_excel('/Users/jeonghyolim/Desktop/capstone_web/data/생활인구.xlsx') 
    df_pop.dropna(subset=['총생활인구수'], inplace=True)

    return df_facility, district

df_facility, district = load_data()


#%%
df_facility

#%%
def gu_list():
    return [gu['properties']['name'] for gu in district['features']]


#%%
def make_map(region='서울'):
    print(region)
    if region == '서울':
        center = [37.541, 126.986]
        facility = df_facility
        zoom_level = 11
    else: 
        # 자치구별 중심 좌표를 찿는다.
        center = [37.541, 126.986]
        # 흡연시설 중에서 자치구에 해당하는 시설만 찾는다.
        onoff = [f.위치.find(region)>=0 for f in df_facility.itertuples()]
        facility = df_facility[onoff]
        zoom_level = 11

    m = folium.Map(location=center, zoom_start=zoom_level)

    # 흡연시설 위치에 마커 표시
    for f in facility.itertuples():
        folium.Marker(location=[f.위도, f.경도], tooltip=f.위치).add_to(m)

    # 자치구(or 행정동) 경계 표시
    # MouseOver 함수를 사용하여 팝업 생성
    folium.GeoJson(district, show=False,
            style_function=lambda x: {'fillColor':'white','color':'black','weight':2},
            highlight_function=lambda x: {'fillColor':'gray','color':'black','weight':2},
            tooltip=folium.features.GeoJsonTooltip(
                fields=['name'],        #['adm_nm'],
                aliases=['자치구:'],    #['행정동:'],
                style='font-size:12px; background-color:limegreen; color:blue',
                sticky=True, 
                direction='right'
                )
            ).add_to(m)
    return m
# %%
