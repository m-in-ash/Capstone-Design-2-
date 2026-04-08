# 서울시 흡연구역 지도 웹서비스 

GitHub Pages에서 바로 열 수 있도록 정적 사이트 형태로 정리한 버전입니다.

## 왜 404가 났나
기존 프로젝트는 Flask 기반 구조였습니다.

- 진입 페이지가 `templates/index.html`에 있어 루트에 `index.html`이 없었습니다.
- 페이지 내부 링크가 `url_for(...)`와 `/map` 같은 Flask 라우트에 의존했습니다.
- GitHub Pages는 Python 서버를 실행하지 않기 때문에 Flask 라우트를 처리할 수 없습니다.

## 이번에 정리한 내용
- `templates/*.html`을 루트 HTML 파일로 배치
- Flask의 `url_for(...)` 링크를 상대경로 링크로 변경
- 지도 영역을 서버 렌더링 방식 대신 정적 Leaflet 지도 방식으로 변경
- `data/facilities.json` 파일을 추가해 브라우저에서 직접 시설 데이터를 읽도록 변경

## 로컬에서 확인
정적 파일만 있으므로 VS Code Live Server나 간단한 정적 서버로 확인할 수 있습니다.

```bash
python -m http.server 8000
```

브라우저에서 `http://localhost:8000` 접속

## GitHub Pages 배포
1. 변경사항 커밋 후 GitHub에 push
2. GitHub 저장소의 **Settings → Pages**
3. **Deploy from a branch**
4. Branch는 `main`, Folder는 `/ (root)` 선택
5. 저장 후 1~3분 정도 기다렸다가 배포 주소 접속

## 참고
- `app.py`, `map.py`는 원래 Flask 개발용 파일이라 Pages 배포에는 직접 사용되지 않습니다.
- 지도 검색은 자치구/장소명 일부 문자열 기준의 필터링 방식으로 동작합니다.
