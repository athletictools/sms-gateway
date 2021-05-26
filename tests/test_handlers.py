from fastapi import status
from fastapi.testclient import TestClient


def test_send_sms(http_client: TestClient):
    # arrange
    request = {
        'messages': [
            {
                'phone_no': '+79091112233',
                'text': 'hello world',
            }
        ],
    }

    # act
    response = http_client.post('/send', json=request)

    # assert
    assert status.HTTP_200_OK == response.status_code
    assert {} == response.json()
