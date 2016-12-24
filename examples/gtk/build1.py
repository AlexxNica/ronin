#!/usr/bin/env python

#
# GTK+ Hello World
#
# build1.py
#
# Source: https://developer.gnome.org/gtk3/stable/gtk-getting-started.html
#
# Requirements: sudo apt install libgtk-3-dev
#
# This is the simplest possible version, using all the sensible defaults.
#

from ronin.cli import cli
from ronin.contexts import new_build_context
from ronin.gcc import GccBuild
from ronin.pkg_config import Package
from ronin.projects import Project
from ronin.rules import Rule
from ronin.utils.paths import glob

with new_build_context() as ctx:
    p = Project('example_1')
    
    c = GccBuild()
    c.add_libraries(Package('gtk+-3.0'))
    
    r = Rule(c)
    r.inputs = glob('src/*.c')
    r.output = 'example_1'
    
    p.rules['executable'] = r
    
    cli(p)
