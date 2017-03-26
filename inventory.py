#!/usr/bin/env python

import json
import yaml


with open("env.yml") as f:
    data = yaml.load(f)

inventory = {role: {"hosts": hosts} for role, hosts in data["roledefs"].items()}
inventory["all"] = {
    "vars": {
        "ansible_ssh_user": data["user"],
        "ansible_ssh_private_key_file": data["key_filename"]
    }
}

print(json.dumps(inventory))
