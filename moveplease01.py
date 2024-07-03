#!/usr/bin/env/python3

# These commands import the needed utilites for this project
import shutil
import os

# The following line moves us into the working directory
os.chdir('/home/student/mycode1/')

# The following line moves "raynor.obj" into the "ceph_storage" directory
shutil.move('raynor.obj', 'ceph_storage/')

# The following line collects a string input from the user
xname = input('what is the new name for the kerrigan.obj?\n')

# The following line moves kerrigan.obj into the ceph_storage directory with a new name
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


