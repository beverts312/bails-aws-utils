# Bails AWS Utils
A set of scripts for maing life easier when working with AWS.

Setup: `pip install bails-aws-utils`

## Route 53

* `dynamc-dns` - A script to update a Route 53 record with the current public IP address of the machine it is running on. This is useful for setting up a dynamic DNS service for a home network. It also comes with a command to help configure it as a cron job.