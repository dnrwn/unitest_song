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

1. 동등 분할

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

4. 단위 (route 한정)
   - rule 고정, method에 대한 invalid case

## 요구사항 분석
1. Query의 경우 동등분할, Type(일부) Csae 사용 가능
2. Main > logic의 경우 동등분할, Type Case 사용 가능 (query Case 재활용)
3. Main > route_... 의 경우 통합 테스트로 대응
   - 사유 : 테스트 케이스 관리 및 테스트 운영 효율을 위함
   - Main > route, API 요구사항을 통합으로 분석하여 TC 설계
   - 동등 분할, 경계값 분석, Type Case 사용 가능
   - 통합 테스트(route)에는 route에 대한 Case만 작성
   - 통합 테스트(API)에는 동등분할, 경계값 분석, Type Error Case 작성
4. UI > 동등 분할, 경계값 분석 사용 가능 (통합 테스트 TC 활용)
5. Parameter의 경계 값을 산출할 수 없을 경우 경계값 분석 미수행
6. method의 경우 동등분할, type invalid case 미수행
7. rule의 경우에는 예외 Case 미수행 (flask 로직 상 rule을 먼저 체크하기 때문에 rule의 invalid case는 유효할 수 없음)
8. method invalid Case의 경우 get, post, delete로만 범위 한

## TC 설계 현황
- 단위 테스트 : 동등분할 완료, 경계값 분석, Type Csae 완료
- 통합 테스트 : 동등분할 진행 중, 경계값 분석 미진행, Type Case 미진, 단위 테스트 미진
- 시스템 테스트 : 미진행

## TC 관리
- 단위 테스트 : unittest_song.git
- 통합, 시스템 테스트 : testscript_song.git

## 테스트 전략 변경
- main.py, Query.py 를 단위테스트로 수행하려 했으나 main.py은 flask, db 모듈이 연동되는 기능이므로 단순 함수 실행으로 단위 테스트를 할 수 없음
- 통합 테스트로 포괄 운영하는 것으로 전략 변경

## TC Script 설계 현황
- 단위 테스트 : 완료
  - pytest를 통해 Test Script 작성
  - Valid Case의 경우 assert로 수행
  - Invalid Case의 경우 with pytest.raises([error type]) 으로 수행
  - 한 개의 pytest Case에 복수의 Case를 수행하고자 할 경우 @pytest.mark.parametrize() 활용
- 통합 테스트 : 진행 불필요 (postman 변환 완료, excel read에서 TC 문서 변환하여 처리)
- 시스템 테스트 : 미진행 (TC 설계 필요)
