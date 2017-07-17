#! /bin/sh -e

# will log "current working directory is: /tmp/workdir"
ctx logger info "current working directory is: ${PWD}"

# will log "first arg is: arg1_value"
ctx logger info "first arg is: $1"

# will log "first arg is: arg1_value"
ctx logger info "second arg is: $2"

# will log "my env variable is: MY_ENV_VARIABLE_VALUE"
ctx logger info "my env variable is: ${MY_ENV_VARIABLE}"

# Running a specific script contained on the machine using a parameter passed 
#./runPsScript.sh $1

# This command retrieves the machine tags
# They are returned as a list of dicts
tags=`ctx instance runtime-properties info.tags`
# Then we are logging them.
ctx logger info "tags: $tags"