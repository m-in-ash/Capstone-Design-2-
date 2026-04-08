# 🚬 서울시 흡연시설 지도 웹 서비스

> 공공데이터를 기반으로 서울시 흡연시설 위치를 시각화하고,  
> 데이터 분석을 통해 지역별 시설 수요를 진단하는 웹 서비스

---

## 📌 프로젝트 개요

- **주제**: 서울시 흡연부스 지도 웹 서비스  
- **기간**: 2022.09 ~ 2023.06  

---

## 🎯 프로젝트 배경

- 서울시 흡연시설 확충 필요성에 대해  
  → **80% 이상이 필요하다고 응답** (2022.07, 흡연자인권연대)

- 공공장소에서 흡연시설 부족으로 인한  
  → **무분별한 흡연 문제 발생**

👉 단순 정보 제공이 아닌, **데이터 기반 수요 분석 + 시각화 서비스 필요**

---

## 🌐 Live Demo

👉 https://m-in-ash.github.io/Capstone-Design-2-/

---

## 🏷️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Folium](https://img.shields.io/badge/Folium-77B829?style=flat)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=flat&logo=html5)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=flat&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript)


---

# 🎨 UI / UX 설계

- Figma를 활용하여 사용자 중심 UI 설계
- 지도 중심 인터페이스 + 직관적인 검색 UX 구성

## 🖥️ 주요 화면

### 1️⃣ 메인 지도 화면
<img width="1919" height="860" alt="image" src="https://github.com/user-attachments/assets/8bfaf551-3fb1-40f3-af9d-3657e09c9b0d" />

- 서울시 흡연시설 위치 시각화
- 사용자 중심 인터페이스 설계

---

### 2️⃣ 검색 기능
![search](./img/search.png)

- 키워드 입력 시 해당 지역 중심 지도 이동
- 사용자 입력 기반 필터링 UX 구현

---

### 3️⃣ 수요 분석 결과
![analysis](./img/analysis.png)

- 자치구별 수요 분석 결과 시각화
- 데이터 기반 의사결정 지원

---

# ⚙️ 주요 기능

## 🗺️ 흡연시설 지도 시각화
- 공공데이터 기반 위치 표시
- Folium 활용 지도 생성

## 🔍 키워드 검색
- 지역명 입력 → 해당 위치 지도 이동
- 클라이언트 측 필터링 방식 구현

## 📊 수요 분석
- 자치구별 데이터 기반 회귀 분석 수행
- 시설 부족/과잉 지역 도출

---

# 🛠️ 시스템 구조

## 🔄 Before (Flask 기반)
Client → Flask Server → Python 처리 → HTML 반환


- 서버 렌더링 구조
- 로컬 실행 필요

---

## 🚀 After (GitHub Pages)
Client → HTML + JS → JSON 데이터 → 지도 렌더링


- 서버 제거
- 정적 웹 구조
- 브라우저 기반 처리

---

# 📂 프로젝트 구조

```bash
Capstone-Design-2-/
├── index.html        # 메인 페이지
├── data.html         # 데이터 페이지
├── contactweb.html   # 웹 문의 페이지
├── contactarea.html  # 지역 문의 페이지
│
├── css/              # 스타일
├── js/               # 클라이언트 로직
├── img/              # 이미지 리소스
├── data/             # JSON 데이터
│
├── app.py            # (기존 Flask 서버)
├── map.py            # 지도 생성 로직
└── README.md
```

---

# 🔄 데이터 흐름 다이어그램

## 🧩 기존 구조 (Flask)
```bash
[Client]
↓ request
[Flask Server]
↓ Python 처리
[데이터 가공]
↓
[HTML 반환]
```

---

## 🌐 현재 구조 (정적 웹)
```bash
[Client Browser]
↓
[index.html]
↓
[JavaScript]
↓
[data.json]
↓
[지도 렌더링]
```

👉 서버 없이 클라이언트 단에서 모든 처리 수행

---

# 📈 기대 효과

- 흡연시설 위치 접근성 향상
- 데이터 기반 정책 의사결정 지원
- 공공시설 확충 방향 제시

---

# 🚧 한계 및 개선 방향

## 한계
- 실시간 데이터 부족
- 일부 데이터 정확도 한계
- 모바일 UX 미흡

## 개선 방향
- API 연동
- 위치 기반 추천
- 반응형 UI 개선

---

# 💡 핵심 성과

" Flask 기반 프로젝트를  👉 **정적 웹 구조로 리팩토링 + 배포 성공** "

---

# 👨‍💻 Contributors

- 재범  
- 민재  
- 태이  
- 성현  
- 효림
