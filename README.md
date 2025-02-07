# unitest_song

## 목적 : restapi_song 프로젝트의 단위 테스트를 위한 테스트 케이스 설계 과정 정리
테스트 범위 : 기능 테스트 기법 중 동등 분할, 경계값 분석을 통한 valid, invalid Case 설계
- type, boundary, Null

## 요구사항
- db_requirements : https://github.com/dnrwn/restapi_song/blob/dev/doc/db_requirements.md
  - Category 2개, 메서드 8개
- server_requirements : https://github.com/dnrwn/restapi_song/blob/dev/doc/server_requirements.md
  - Category 3개, 메서드 13개

## 테스트 도구
- 수행 : pytest 모듈 이용
- 결과 : pytest-html 모듈 이용
- 커버리지 측정 : coverage 모듈 이용 (report, html)
  - coverage run -m pytest test_mymodule.py
  - coverage run -m pytest tests/
  - coverage run -m pytest -v -m "my_marker" tests/

## 테스트 케이스 설계 규칙
- 페어와이즈 기법 (2-way)을 통해 동등 분할, 경계값 분석로 Case 추출
  - Mandatory일 경우 Null 값은 Invalid
  - Optional일 경우 Null 값은 Valid
- https://pairwise.yuuniworks.com/
1. 동등등 분할
a. Int
  - Valid : 1
  - Invalid : 'a', Null
b. String
  - Valid = 'a'
  - Invalid = Null, 1
c. Boolean
  - Valid = True, False
  - Invlaid = 'a', Null
2. 경계값 분석
a. Int
  - valid : 1
b. String
  - Valid : ''(Min lengh), 'aaaaa'(Max lengh)
  - Invalid : 'aaaaab'(Max lengh + 1)
c. Boolean
  - Valid : 0, 1, 5

3. dict 형태로 전달하지 않은 Type Case (invalid)
  - list : [1, 'a', '3', 1]

## 요구사항 분석
1. Query의 경우 동등분할, Type(일부) Csae 사용 가능
2. Main > logic의 경우 동등분할, Type Case 사용 가능 (query Case 재활용)
3. Main > route_... 의 경우 통합 테스트로 대응
   - 사유 : 테스트 케이스 관리 및 테스트 운영 효율을 위함
   - Main > route, API 요구사항을 통합으로 분석하여 TC 설계
   - 동등 분할, 경계값 분석, Type Case 사용 가능
4. UI > 동등 분할, 경계값 분석 사용 가능 (통합 테스트 TC 활용)

## TC 설계 현황
- 단위 테스트 : 동등분할 완료, Type Csae 완료
- 통합 테스트 : 동등분할 진행 중, 경계값 분석 미진행, Type Case 미진, 단위 테스트 미진
- 시나리오 테스트 : 미진행
