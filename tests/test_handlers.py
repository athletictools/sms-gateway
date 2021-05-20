from aiohttp.test_utils import TestClient


async def test_send_sms(http_client: TestClient):
    # arrange
    request = {
        'numbers': ['+79091112233', '+79092223344', ],
        'text': 'hello world',
    }

    # act
    response = await http_client.post('/send', json=request)

    assert 200 == response.status
