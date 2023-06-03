import requests
import testify

from const import *

def fun_call(url: str, fun):
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 
    
    return fun(url, headers=headers)

def get_count(url: str, fun_ptr):
    
    resp = fun_call(url, fun_ptr)

    return resp.json()['results']['count']

def assert_not_equal_count(url: str, fun_ptr):
    """assert that there has been something added or removed"""
    before = get_count(GET_ALL_URL, requests.get)
    after = get_count(url, fun_ptr)
    testify.assert_not_equal(before, after)
    
    return 0

def assert_equal_count(url: str, fun_ptr):
    """assert that nothing has been added or removed"""
    before = get_count(GET_ALL_URL, requests.get)
    after = get_count(url, fun_ptr)
    testify.assert_equal(before, after)
    
    return 0

def assert_url(url: str, fun_ptr):
    """assert that endpoint is valid"""
    
    resp = fun_call(url, fun_ptr)

    testify.assert_equal(resp.status_code, 200)

    return 0

class TestSmoke(testify.TestCase):
    """docstring for TestSmoke."""

    def test_smoke_url(self):
        return assert_url(SMOKE_URL, requests.get)

    def test_smoke_output(self):
        resp = fun_call(SMOKE_URL, requests.get)
        testify.assert_equal(resp.json(), SMOKE)

class TestGet(testify.TestCase):
    """docstring for TestGet."""

    def test_get_all_url(self):
        return assert_url(GET_ALL_URL, requests.get)
    
    def test_get_all_equal_output(self):
        return assert_equal_count(GET_ALL_URL, requests.get)
    
    def test_get_by_color_url(self):
        return assert_url(GET_BY_COLOR_URL, requests.get)
    
    def test_get_by_color_output(self):
        resp = fun_call(GET_BY_COLOR_URL, requests.get)
        testify.assert_equal(resp.json()['results']['data'][0]['id'], STATIC['results']['data'][1]['id'])
    
    def test_get_by_color_count(self):
        return assert_not_equal_count(GET_BY_COLOR_URL, requests.get)

    def test_get_by_breed_url(self):
        return assert_url(GET_BY_BREED_URL, requests.get)
    
    def test_get_by_breed_output(self):
        resp = fun_call(GET_BY_BREED_URL, requests.get)
        testify.assert_equal(resp.json()['results']['data'][0]['id'], STATIC['results']['data'][2]['id'])
    
    def test_get_by_breed_count(self):
        return assert_not_equal_count(GET_BY_BREED_URL, requests.get)

class TestInsert(testify.TestCase):
    """docstring for TestInsert."""

    def test_insert_count(self):
        return assert_not_equal_count(INSERT_URL, requests.get)

if __name__ == '__main__':
    testify.run()
