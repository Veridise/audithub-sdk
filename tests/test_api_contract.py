from audithub_sdk import Configuration


def test_default_host_is_absolute():
    assert Configuration().host == "https://audithub.dev.veridise.tools/api/v1"
