import pytest
import api
import json

@pytest.mark.get_OneItem
def test_get_OneItem():
    app = api.app.test_client()
    resp = app.get("/inventario/Conjured/12/09")

    assert resp.status_code == 200

    resp_dict = json.loads(resp.data.decode())[0]

    assert resp_dict.get("name") == "Conjured"
    assert resp_dict.get("quality") == "12"
    assert resp_dict.get("sell_in") == "09"
