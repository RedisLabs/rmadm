# rmadm

Redis Labs Enterprise Module Management Utility

# About

This tool allows you to use modules in the Redis Labs Enterprise 5.0 cluster. It can install modules, create databases, and upgrade module on databases.

# Installing rmadm

Assuming pip is installed on the machine (if not, it can be installed by `apt-get install python-pip` on Ubuntu)

```sh
$ pip install git+https://github.com/RedisLabs/rmadm@master
```

## Prerequisits for Installing rmadm
If you are on older operating systems like RHEL 6, you may need to get the dependencies updated. Depending on your OS you may need to substitude "apt-get" with "yum"

if you do not have pip with your version of python please install pip
```sh
$ sudo apt-get install python-pip
```
Some older version pythons may, even though they have pip may require update to pip.
```sh
$ sudo pip install --upgrade pip
```

You may also need an update to the remote library for rmadm to work. The error may look like _"TypeError: request() got an unexpected keyword argument 'json'"_
```sh
pip install --upgrade requests 
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

## rmadm cluster list_modules [MODULE]

List available modules and versions, optionally filtering by specific module.

Example:

```
$ rmadm cluster list_modules

--------------------------------------------------------------------------------
| Module          | Version         | UID
--------------------------------------------------------------------------------
| bf              | 2.0             | 1e20a0697da9ba95d281f8bf3179bc4c
| ft              | 9000.0          | b6ab49e747cc4debf70dcc57d799d004
| ft              | 2000.0          | c7f15d6fc15b2d5324d2a5e38f667032
| ft              | 11.0            | ed43dbf2983b69163e6b87376ae4f1cf
| ft              | 9001.0          | 6c4b3dba6df68e8a2a6b271a053128b3
--------------------------------------------------------------------------------
```

##  rmadm cluster upgrade [OPTIONS] MODULE [VERSION]

Upgrade a module on an existing BDB using a new module version

### Options:

```
  --bdb INTEGER  BDB Id to upgrade the module on
  --file TEXT    Upload module from a local file
  --help         Show this message and exit.
```


