import sys, os, logging, pytest
from datetime import *
from unittest.mock import patch

# 다른 프로젝트에 있는 모듈을 가져오기 위한 code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'restapi_song', 'server')))
import main

# Test에 필요한 모듈 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
date = datetime.now().strftime('%y-%m-%d %H:%M:%S')


# main.py Test Case
def test_DB_query_date_1():
    actual_result = main.date()
    expected_result = date
    logger.info(actual_result)
    assert expected_result in actual_result

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
        main.post_insert(parameter)


@pytest.mark.parametrize("parameter_1, parameter_2, parameter_3", [
    (0, None, None),
    (0, 1, 'a'),
    (5, None, 1),
    (1, None, 'a'),
    (5, 'a', None),
    (1, 'a', 1),
    (0, 'a', 'a'),
    (1, 1, None),
    (0, 1, 1),
])
@patch('main.flask', autospec=True)
def test_Main_Common_Response_1(parameter_1, parameter_2, parameter_3):
    actual_result = main.response(parameter_1, parameter_2, parameter_3)
    expected_result = 1
    logging.info(actual_result)
    assert expected_result in actual_result


def test_Main_Common_Response_3():
    pass

def test_Main_Common_Response_5():
    pass

def test_Main_Logic_logic_default_1():
    pass

def test_Main_Logic_logic_default_3():
    pass

def test_Main_Logic_logic_default_5():
    pass

def test_Main_Logic_logic_ui_1():
    pass

def test_Main_Logic_logic_ui_3():
    pass

def test_Main_Logic_logic_ui_5():
    pass

def test_Main_Logic_logic_select_1():
    pass

def test_Main_Logic_logic_select_3():
    pass

def test_Main_Logic_logic_select_5():
    pass

def test_Main_Logic_logic_update_1():
    pass

def test_Main_Logic_logic_update_2():
    pass

def test_Main_Logic_logic_update_4():
    pass

def test_Main_Logic_logic_update_5():
    pass

def test_Main_Logic_logic_update_7():
    pass

def test_Main_Logic_logic_insert_1():
    pass

def test_Main_Logic_logic_insert_2():
    pass

def test_Main_Logic_logic_insert_4():
    pass

def test_Main_Logic_logic_insert_5():
    pass

def test_Main_Logic_logic_insert_7():
    pass

def test_Main_Logic_logic_delete_1():
    pass

def test_Main_Logic_logic_delete_2():
    pass

def test_Main_Logic_logic_delete_4():
    pass

def test_Main_Logic_logic_delete_5():
    pass

def test_Main_Logic_logic_delete_7():
    pass
