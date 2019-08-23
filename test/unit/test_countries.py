# For testing and assertions
import pytest, json, random
from assertpy import assert_that

# For URL request
import requests

@pytest.mark.status_code
def test_not_found_request(request):
    # Inconsistent parameter
    index = 'abc'
    # Make a request on the invalid URL
    url = 'http://localhost:5000/countries/sw_lifs_gt/{}'.format(index)
    print('[RUNNING] ' + request.node.name + ' using ' + url)
    resp = requests.get(url)
    # Assertions
    assert_that(resp.ok).is_false()
    assert_that(resp.status_code).is_equal_to(404) # Not Found

@pytest.mark.status_code
def test_countries_good_request(request):
    # Randomize the index with an valid range
    index = round(random.uniform(0.1, 10.0), 2)
    # Make a request on the specified URL
    url = 'http://localhost:5000/countries/sw_lifs_gt/{}'.format(index)
    print('[RUNNING] ' + request.node.name + ' using ' + url)
    resp = requests.get(url)
    # Assertions
    assert_that(resp.ok).is_true()
    assert_that(resp.status_code).is_equal_to(200) # OK

@pytest.mark.status_code
def test_countries_bad_request(request):
    # Invalid value for the parameter
    index = 0.0
    # Make a request on the specified URL
    url = 'http://localhost:5000/countries/sw_lifs_gt/{}'.format(index)
    print('[RUNNING] ' + request.node.name + ' using ' + url)
    resp = requests.get(url)
    # Assertions
    assert_that(resp.ok).is_false()
    assert_that(resp.status_code).is_equal_to(400) # Bad Request

@pytest.mark.countries_len
def test_countries_all(request):
    # Specific index
    index = 0.1
    # Make a request on the specified URL
    url = 'http://localhost:5000/countries/sw_lifs_gt/{}'.format(index)
    print('[RUNNING] ' + request.node.name + ' using ' + url)
    resp = requests.get(url)
    # Assertions
    assert_that(resp.ok).is_true()
    assert_that(resp.status_code).is_equal_to(200) # OK
    assert_that(len(resp.json())).is_equal_to(39) # All results

@pytest.mark.countries_len
def test_countries_none(request):
    # Specific index
    index = 7.5
    # Make a request on the specified URL
    url = 'http://localhost:5000/countries/sw_lifs_gt/{}'.format(index)
    print('[RUNNING] ' + request.node.name + ' using ' + url)
    resp = requests.get(url)
    # Assertions
    assert_that(resp.ok).is_true()
    assert_that(resp.status_code).is_equal_to(200) # OK
    assert_that(len(resp.json())).is_equal_to(0) # None results