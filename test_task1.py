import pytest
@pytest.fixture
def Testsetup():
    print("Browser setup is done")
    yield
    print("Browser teardown")


def test_sample(Testsetup):
    print("Test execution")
    assert True

@pytest.mark.smoke
def test_smoke():
    print("Running smoke tests")
    assert True


@pytest.mark.regression
def test_regression_test():
    print("Regression test run")
    assert True


@pytest.mark.skip(reason="Not required so skipping it")
def test_skip():
    print("This test is skipped")
    assert True
