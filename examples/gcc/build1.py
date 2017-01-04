#!/usr/bin/env python

#
# gcc GTK+ Hello World
#
# build1.py
#
# Source: https://developer.gnome.org/gtk3/stable/gtk-getting-started.html
#
# Requirements:
#
#   Ubuntu: sudo apt install gcc ccache libgtk-3-dev
#
# This is the simplest possible version, using a single build phase and all the defaults.
#
# A single build phase works fine, and may be the best solution for small projects. However, it does
# not make use of Ninja's ability to parallelize builds, and to track changes to individual files
# ("incremental" builds). Larger projects would generally build faster will a two-phase
# (compile/link) build. See build2.py for an example.
#

from ronin.cli import cli
from ronin.contexts import new_build_context
from ronin.gcc import GccBuild
from ronin.phases import Phase
from ronin.pkg_config import Package
from ronin.projects import Project
from ronin.utils.paths import glob

with new_build_context(output_path_relative='build1') as ctx:

    project = Project('gcc GTK+ Hello World')
    
    build = Phase(GccBuild(),
                  inputs=glob('src/**/*.c'),
                  extensions=[Package('gtk+-3.0')],
                  output='example_1')

    project.phases['build'] = build
    
    cli(project)
