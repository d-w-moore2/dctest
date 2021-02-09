import json
import sys

def run (CI):

    final_config = CI.store_config(
        {
            "yaml_substitutions": {         # -> written to ".env"
                "python_version" : "3",
                "os_generic":"ubuntu",
                "os_image":"ubuntu:18.04"
            },
            "container_environments": {
                # "client-runner" : {       # -> written to "client-runner.env"
                # }

            }
        }
    )

    print ('----------\nconfig after CI modify pass\n----------',file=sys.stderr)
    print(json.dumps(final_config,indent=4),file=sys.stderr)

    return CI.run_and_wait_on_client_exit ()

