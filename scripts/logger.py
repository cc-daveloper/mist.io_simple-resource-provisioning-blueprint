import subprocess
from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

# This logs the configure lifecycle script params.
# These are passed from the script_params input.
args = inputs['process']['args']
ctx.logger.info("The script args are: {0}".format(args))

# This line retrieves the machine tags
tags = ctx.instance.runtime_properties['info']['tags']
ctx.logger.info("tags are: {0}".format(tags))

# Iterate over all machine tags
for tag in tags:
    # get the key of the tag
    if tag['key'] == 'prod':
        ctx.logger.info("This machine is in prod!")
        ctx.logger.info("We have the following argument: {0}".format(args[0]))
        # This is how a shell command would be run
        # command = "runPsScript.sh " + args[0]
        command = "echo  " + args[0]
        response = subprocess.call(command, shell=True)
        ctx.instance.execute_operation(
            'cloudify.interfaces.lifecycle.run',
            kwargs={'params': ''}
        )
        if response != 0:
            ctx.logger.info("There was an error while running the script.")
        else:
            ctx.logger.info("Script has run successfully.")
    else:
        ctx.logger.info("This machine is not production critical!")
        ctx.logger.info("We have the following argument: {0}".format(args[0]))