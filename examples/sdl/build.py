#!/usr/bin/env python

#
# SDL Hello World
#
# build.py
#
# Source: https://github.com/Twinklebear/TwinklebearDev-Lessons/blob/master/Lesson1/src/main.cpp
#
# Requirements: sudo apt install gcc ccache libsdl2-dev
#
# Simple example of using SDL. Note that instead of using sdl_config.SDL() we could also have used
# pkg_config.Package('sdl2'). The difference is that sdl_config.SDL() uses the sdl2-config utility,
# which is more specialized than pkg-config.
#
# The script also supports linking SDL as a static library if you specify "--context static true"
# in the command line.
#

from ronin.cli import cli
from ronin.copy import Copy
from ronin.contexts import new_build_context
from ronin.gcc import GccBuild
from ronin.phases import Phase
from ronin.projects import Project
from ronin.sdl_config import SDL
from ronin.utils.paths import glob

with new_build_context() as ctx:
    ctx.static = False
    
    project = Project('SDL Hello World')
    
    build = Phase(GccBuild('g++'), inputs=glob('src/*.cpp'), output='hello')
    build.executor.standard('c++0x')
    build.executor.libraries.append(SDL(static=lambda ctx: ctx.static))
    project.phases['build'] = build
    
    resource = Phase(Copy(), inputs=glob('res/*'))
    project.phases['resource'] = resource
    
    cli(project)
