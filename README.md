# slam-v2-cli

Installation
============

slam-v2-cli has been tested w/ python 3.6 and mainly need requests module from python.

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

After installation, you need to edit slam-env file to modify SLAM_LOCATION and SLAM_USERNAME to
match your SLAM installation.

Usage
=====

To use SLAM, you just need to load your env w/ command

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

SLAM use composed by plugin, each one provide access to some configuration part

- domains: access to DNS domain (like example.com)
- networks: access to IP network (like 192.168.0.0/24)
- hardware: access to hardware inventory (physical machine)
- hosts: a host is a combo of domains / networks and hardware.

each plugin have a standard set of actions

- create: to create a new item (domain, network, hardware, host)
- delete: to delete a item
- update: to update a item
- add: add a new element in a item (like a fqdn, a IP in a network, a interface in a hardware)
- remove: remove a element in a item

some plugins have additional actions 

- include: to include a new field in a element (like a reference for a CNAME)
- exclude: to suppress a field in a element

Some basic example
==================

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
    