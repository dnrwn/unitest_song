import sys, os, logging
from datetime import *

import pytest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
date = datetime.now().strftime('%y-%m-%d %H:%M:%S')
# 현재 파일의 경로를 기준으로 상위 디렉토리와 server 디렉토리 경로를 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'restapi_song', 'server', 'db_f')))

# 이제 db_f.query 모듈을 import 할 수 있음
import Query

def test_DB_query_date_1():
    # 테스트 코드 작성
    actual_result = Query.date()
    expected_result = date
    logger.info(actual_result)
    assert expected_result in actual_result

def test_DB_query_get_select_all_1():
    actual_result = Query.get_select_all()
    expected_result = "SELECT * FROM new_db.item;"
    logger.info(actual_result)
    assert expected_result in actual_result

@pytest.mark.parametrize("parameter", [{'idx':1}])
def test_DB_query_get_select_one_1(parameter):
    actual_result = Query.get_select_one(parameter)
    expected_result = "SELECT * FROM new_db.item where idx = {idx};".format(**parameter)
    logger.info(actual_result)
    assert expected_result in actual_result

@pytest.mark.parametrize("parameter", [{'a'}, {}])
def test_DB_query_get_select_one_2(parameter):
    with pytest.raises(TypeError):
        Query.get_select_one(parameter)

def test_DB_Query_get_select_one_3():
    parameter = {1}
    with pytest.raises(TypeError):
        Query.get_select_one(parameter)

@pytest.mark.parametrize("parameter", [
    {'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'input_4': False, 'create_date': date},
    {'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'input_4': True, 'create_date': date}
])
def test_DB_query_post_insert_1(parameter):
    actual_result = Query.post_insert(parameter)
    expected_result = ("INSERT INTO item (input_1, input_2, input_3, input_4, create_date) "
                       "VALUES('{input_1}', '{input_2}', '{input_3}', '{input_4}', '{create_date}');").format(**parameter)
    logger.info(actual_result)
    assert expected_result in actual_result, f"Expected {expected_result} but got {actual_result}"

@pytest.mark.parametrize("parameter, expected_result", [
    ({'input_1': 'a', 'input_2': 'a', 'input_3': 'a', 'input_4': False, 'create_date': date}, TypeError),
    ({'input_2': 'a', 'input_3': 'a', 'input_4': False, 'create_date': date}, KeyError),
    ({'input_1': 1, 'input_2': 1, 'input_3': 'a', 'input_4': False, 'create_date': date}, TypeError),
    ({'input_1': 1, 'input_3': 'a', 'input_4': False, 'create_date': date}, KeyError),
    ({'input_1': 1, 'input_2': 'a', 'input_3': 1, 'input_4': False, 'create_date': date}, TypeError),
    ({'input_1': 1, 'input_2': 'a', 'input_4': False, 'create_date': date}, KeyError),
    ({'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'create_date': date}, KeyError),
    ({'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'input_4': 'a', 'create_date': date}, TypeError)
    ])
def test_DB_query_post_insert_3(parameter, expected_result):
    with pytest.raises(expected_result):
        Query.post_insert(parameter)

@pytest.mark.parametrize("parameter", [{1, 'a', 'b', 1}])
def test_DB_Query_post_insert_5(parameter):
    with pytest.raises(TypeError):
        Query.post_insert(parameter)

@pytest.mark.parametrize("parameter", [
    {'input_1' : 1, 'input_2' : 'a', 'input_3' : 'a', 'input_4' : False, 'update_date' : date, 'idx': 1},
    {'input_1' : 1, 'input_2' : 'a', 'input_3' : 'a', 'input_4' : True, 'update_date' : date, 'idx' : 1}
])
def test_DB_query_post_update_1(parameter):
    actual_result = Query.post_update(parameter)
    expected_result = (
    "UPDATE item SET input_1={input_1}, input_2='{input_2}', input_3='{input_3}', input_4={input_4}, update_date='{update_date}' "
    "WHERE idx = {idx};"
).format(**parameter)
    logger.info(actual_result)
    assert expected_result in actual_result

@pytest.mark.parametrize("parameter, expected_result", [
    ({'input_1': 'a', 'input_2': 'a', 'input_3': 'a', 'input_4': False, 'update_date': date, 'idx': 1}, TypeError),
    ({'input_2': 'a', 'input_3': 'a', 'input_4': False, 'update_date': date, 'idx': 1}, KeyError),
    ({'input_1': 1, 'input_3': 'a', 'input_4': False, 'update_date': date, 'idx': 1}, KeyError),
    ({'input_1': 1, 'input_2': 1, 'input_3': 'a', 'input_4': False, 'update_date': date, 'idx': 1}, TypeError),
    ({'input_1': 1, 'input_2': 'a', 'input_4': False, 'update_date': date, 'idx': 1}, KeyError),
    ({'input_1': 1, 'input_2': 'a', 'input_3': 1, 'input_4': False, 'update_date': date, 'idx': 1}, TypeError),
    ({'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'input_4': 'a', 'update_date': date, 'idx': 1}, TypeError),
    ({'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'update_date': date, 'idx': 1}, KeyError),
    ({'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'input_4': False, 'update_date': date, 'idx': 'a'}, TypeError),
    ({'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'input_4': False, 'update_date': date}, KeyError),
])
def test_DB_query_post_update_3(parameter, expected_result):
    with pytest.raises(expected_result):
        Query.post_update(parameter)

@pytest.mark.parametrize("parameter", [{1, 'a', 'b', 1, 1}])
def test_DB_Query_post_update_5(parameter):
    with pytest.raises(TypeError):
        Query.post_update(parameter)

@pytest.mark.parametrize("parameter", [{'idx':5}])
def test_DB_query_delete_delete_1(parameter):
    actual_result = Query.delete_delete(parameter)
    expected_result = "DELETE FROM new_db.item where idx={idx};".format(**parameter)
    logger.info(actual_result)
    assert expected_result in actual_result


@pytest.mark.parametrize("parameter", [{'idx':'a'}, {}])
def test_DB_query_delete_delete_3(parameter):
    with pytest.raises(TypeError):
        Query.delete_delete(parameter)

@pytest.mark.parametrize("parameter", [{1}])
def test_DB_Query_delete_delete_5(parameter):
    with pytest.raises(TypeError):
        Query.delete_delete(parameter)

