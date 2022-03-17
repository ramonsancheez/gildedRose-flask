import pytest
import api
import json

@pytest.mark.get_name
def test_get_name():
    app = api.app.test_client()
    resp = app.get("/inventario/sell_in/03")

    assert resp.status_code == 200

    resp_dict = json.loads(resp.data.decode())[0]

    assert resp_dict.get("name") == "Conjured"
    assert resp_dict.get("quality") == "32"
    assert resp_dict.get("sell_in") == "03"