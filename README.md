# unitest_song

목적 : restapi_song 프로젝트의 단위 테스트를 위한 테스트 케이스 설계 과정 정리
테스트 범위 : 기능 테스트 기법 중 동등 분할, 경계값 분석을 통한 valid, invalid Case 설계
- type, boundary, Null

요구사항
- db_requirements : https://github.com/dnrwn/restapi_song/blob/dev/doc/db_requirements.md
  - Category 2개, 메서드 8개
- server_requirements : https://github.com/dnrwn/restapi_song/blob/dev/doc/server_requirements.md
  - Category 3개, 메서드 13개

테스트 도구
- 수행 : pytest 모듈 이용
- 결과 : pytest-html 모듈 이용
- 커버리지 측정 : coverage 모듈 이용 (report, html)
  - coverage run -m pytest test_mymodule.py
  - coverage run -m pytest tests/
  - coverage run -m pytest -v -m "my_marker" tests/

테스트 케이스
1. dbrequirements
2. server_requirements
