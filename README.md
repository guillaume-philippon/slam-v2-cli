# slam-v2-cli

Installation
============

slam-v2-cli has been tested with python 3.6+ and mainly needs requests Python module.

    username@box$ git clone https://github.com/guillaume-philippon/slam-v2-cli.git
    username@box$ cd slam-v2-cli
    username@box$ python3 -m venv .venv
    username@box$ source slam-env

You must check if your are in your virtualenv. Normally, your prompt has been updated and start
with (.venv) to indicate that your in a python virtualenv

    (.venv) username@box$ python --version
    Python 3.7.2
    (.venv) username@box$ pip install -r requirements.txt
    
Configuration
=============

After installation, you need to edit the slam-env file to modify SLAM_LOCATION and SLAM_USERNAME to
match your SLAM installation.

    username@box$ cat slam-env
    [...]
    export SLAM_LOCATION=https://slam.example.com
    export SLAM_USERNAME=slamadmin
    [...]

If dirname command is not available on your machine, you can also define SLAM_PATH to match your slam-cli
installation directory

    username@box$ cat slam-env
    [...]
    export SLAM_PATH=$HOME/slam-v2-cli
    [...] 

Usage
=====

To use SLAM, you just need to load your env with command

    username@box$ source slam-env
    (.venv) username@box$ slam -h
    usage: slam [-h] {domains,networks,hardware,hosts,producer} ...

    positional arguments:
      {domains,networks,hardware,hosts,producer}
                            Plugins
    
    optional arguments:
      -h, --help            show this help message and exit
      
Quick start
===========

SLAM is composed of several plugins, each one managing part of the SLAM information:

- domains: access to DNS domain (like example.com)
- networks: access to IP network (like 192.168.0.0/24)
- hardware: access to hardware inventory (physical machine)
- hosts: a host is a combination of domains / networks and hardware.

Each plugin have a standard set of actions:

- create: to create a new item (domain, network, hardware, host)
- delete: to delete a item
- update: to update a item
- add: add a new element in a item (like a fqdn, a IP in a network, a interface in a hardware)
- remove: remove a element in a item

some plugins have additional actions:

- include: to include a new field in a element (like a reference for a CNAME)
- exclude: to suppress a field in a element

Some basic examples
===================

Help
----
    slam -h
    slam domains -h
    slam domains create -h
    slam domains update -h

Create
------

    slam domains create example.com --dns-master 127.0.0.1
    slam networks create --address 192.168.0.0 --prefix 24 my-network

Change information
------------------

    slam networks update my-network --vlan 2
    slam domains update example.com --description 'This is a example'

Add a host
----------
    slam hosts create box.example.com --network my-network --interface 00:11:22:33:44:55

Add a IP on a host
------------------
    slam hosts add --ip-address 192.168.0.2 box.example.com

Modify a IP on host
-------------------
You can't modify or rename an IP address, but you can add a IP on a host and remove the old IP
address

    slam hosts show box.example.com # to display the host config
    https://slam.example.com/hosts/box.example.com
         name: box.example.com
         dhcp: True
    creation date: 2021-01-28T13:57:24.006Z
         hardware:
          network: (my-network)
                - 192.168.0.1
    slam hosts add --ip-address 192.168.0.2 box.example.com
    slam hosts show box.example.com # to display the host config
    https://slam.example.com/hosts/box.example.com
         name: box.example.com
         dhcp: True
    creation date: 2021-01-28T13:57:24.006Z
         hardware:
          network: (my-network)
                - 192.168.0.1
                - 192.168.0.2
    slam networks remove --ip-address 192.168.0.1 my-network
    slam hosts show box.example.com # to display the host config
    https://slam.example.com/hosts/box.example.com
         name: box.example.com
         dhcp: True
    creation date: 2021-01-28T13:57:24.006Z
         hardware:
          network: (my-network)
                - 192.168.0.2

    
Using SLAM CLI on Windows with Git Bash
---------------------------------------
On Windows, when using Git Bash (on Bash shell as provided by MinGW), there is a know issue with
the password prompt, because the `pty` emulation is incomplete. There are several possible
workarounds:

- Run SLAM CLI in a Windows shell or PowerShell
- Use `winpty` (installed as part of Git Bash) to execute it with a command like:

  ```bash
  winpty python slam ...
  ```
- Define the variable `SLAM_PASSOWRD`

