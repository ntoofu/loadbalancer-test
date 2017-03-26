from fabric.api import env, execute, puts, task, run
from fabric.decorators import roles
import pytest
import yaml

@task
def load_config(filepath):
    with open(filepath) as f:
        data = yaml.load(f)
    env.user = data["user"]
    env.key_filename = data["key_filename"]
    env.roledefs.update(
        {
            "server": data["roledefs"]["server"],
            "client": data["roledefs"]["client"]
        }
    )
    env.lb_address = data["lb_address"]

def curl(url):
    result = run("curl -f -k %s" % url, warn_only=True)
    return result

