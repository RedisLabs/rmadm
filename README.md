# rmadm

Redis Labs Enterprise Module Management Utility

# About

This tool allows you to use modules in the Redis Labs Enterprise 5.0 cluster. It can install modules, create databases, and upgrade module on databases.

# Installing rmadm

Assuming pip is installed on the machine (if not, it can be installed by `apt-get install python-pip` on Ubuntu)

```sh
pip install git+https://github.com/RedisLabs/rmadm@master
```

# Note on configuration and credentials

You need to provide the commands with Redis Pack (Redis Labs Enterprise Cluster) login credentials. 
You can provide them with command-line arguments or environment variables. If they are not configured, the user 
is prompted to enter them.

## Configuring environment variables

Modify the values according to your cluster's credentials:

```sh
$ export RL_USER="myuser@domain.com"
$ export RL_PASS="mypassword"

# Optional - configure the cluster host if not running locally.
# Not required if you are running rmadm on the cluster's master host.
$ export RL_HOST="https://127.0.0.1:9443"
```

---

# Quick Start: Creating a Database With a Module

The main command is `rmadm cluster create_db {module} [{version}]`:

Example: creating a database with the latest version of rebloom.

```sh
$ rmadm cluster create_db rebloom
Database Name [mydb]: rebloom1231
Number of Redis Shards [5]:
Database Memory Limit (in GB) [4]: 2
Enable Replication [y/N]:
Custom Module Args []:
  
  File rebloom.Linux-x86_64.latest.zip does not exist, downloading it...
  Downloading https://s3.amazonaws.com/redismodules/rebloom/rebloom.Linux-x86_64.latest.zip...
  Deploying module to cluster...
  Module UID: 1e20a0697da9ba95d281f8bf3179bc4c
  Creating db...

OK
```

# Command Reference

## rmadm download MODULE [VERSION]

Download a module from s3 storage (where all module builds are stored) to the local machine. 

### Example:

```sh
rmadm download rscoordinator latest
```

**VERSION** can be omitted if you need the latest version. 

-------


## rmadm cluster create_db [OPTIONS] MODULE

Create a new database with the given module. By default we download the latest version of the module if it does not exist on the current folder.

### Options

```
  --version TEXT      Module Version
  --module_args TEXT  Module Configuration Argument List
  --db TEXT           Database Name
  --shards INTEGER    Number of Redis Shards
  --maxmemory TEXT    Database Memory Limit (in GB)
  --replication       If set, replication is enabled
  --file TEXT         Upload module from a local file
  --help              Show this message and exit.
```

--------

