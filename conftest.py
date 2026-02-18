import pytest


@pytest.hookimpl(hookwrapper=True)
@pytest.fixture(autouse=True)
def setup():
    print("\nBrowser setup")
    yield
    print("\nBrowser teardown")

def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path="failure.png")
