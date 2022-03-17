import pytest
import api
import json

@pytest.mark.get_name
def test_get_name():
    app = api.app.test_client()
    resp = app.get("/inventario/quality/12")

    assert resp.status_code == 200

    resp_dict = json.loads(resp.data.decode())[0]

    assert resp_dict.get("name") == "Aged_brie"
    assert resp_dict.get("quality") == "12"
    assert resp_dict.get("sell_in") == "21"