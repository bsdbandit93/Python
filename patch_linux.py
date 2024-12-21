#!/usr/bin/python
############################################
#This script automates the process of      #
#of patching either centos or ubuntu linux #
############################################


####################
#Modules           #
####################
import os
import sys
import platform


###########################
#Patching Linux           #
###########################
def patch_linux():
    dist = platform.linux_distribution()
    flavor = dist[0]
    #######################
    #Patch  Ubuntu        #
    #######################
    if flavor == 'Ubuntu':
        import apt
        cache = apt.Cache()
        cache.update()
        cache.open(None)
        cache.upgrade()
        cache.commit()
    #######################
    #Patch Centos/RHEL    #
    #######################
    elif flavor == 'CentOS Linux':
        import yum
        my = yum.YumBase()
        my.update()
        my.resolveDeps()
        my.processTransaction()





patch_linux()

