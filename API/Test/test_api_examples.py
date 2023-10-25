from playwright.sync_api import APIRequestContext,Playwright
from typing import Generator
import pytest
from API.TestData.test_data import TestData


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
)-> Generator[APIRequestContext,None,None]:
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


def test_post_example(api_request_context: APIRequestContext) -> None:
    headers = {"Content-type": "application/json"}
    post_todo = api_request_context.post(
        f"{TestData.BASE_URL}/posts", data=TestData.DATA, headers=headers
    )
    # assert post_todo.ok
    assert post_todo.json()["title"] == "foo2"


def test_get_example(api_request_context: APIRequestContext):
    headers = {"Content-type": "application/json"}
    get_todo = api_request_context.get(
        f"{TestData.BASE_URL}/posts/{TestData.DATA.get('userId')}",  headers=headers
    )
    assert get_todo.ok


def test_put_example(api_request_context: APIRequestContext):
    headers = {"Content-type": "application/json"}
    put_todo = api_request_context.put(
        f"{TestData.BASE_URL}/posts/{TestData.DATA.get('userId')}", data=TestData.DATA, headers=headers
    )
    assert put_todo.ok
    assert put_todo.status == 200
    assert put_todo.json()["title"] == "foo2"


def test_delete_example(api_request_context: APIRequestContext):
    headers = {"Content-type": "application/json"}
    delete_todo = api_request_context.delete(
        f"{TestData.BASE_URL}/posts/{TestData.DATA.get('userId')}", headers=headers)
    assert delete_todo.ok
    assert delete_todo.status == 200