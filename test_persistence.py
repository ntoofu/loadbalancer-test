from fabric.api import env, execute
import pytest
from fabfile import load_config, curl


execute(load_config, "env.yml")

def test_persistence_srcip():
    first_resp = aggregate_http_response()
    second_resp = aggregate_http_response()
    assert(first_resp == second_resp)
    for response in first_resp.values():
        assert(response != "")

def aggregate_http_response():
    results = execute(curl, "http://{}/hostname".format(env.lb_address), role="client")
    return {client: result.stdout for client, result in results.items()}

