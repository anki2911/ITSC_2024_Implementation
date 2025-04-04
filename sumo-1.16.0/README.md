<a href="https://sumo.dlr.de/docs"><p align="center"><img width=50% src="https://raw.githubusercontent.com/eclipse/sumo/main/docs/web/docs/images/sumo-logo.svg"></p></a>

Eclipse SUMO - Simulation of Urban MObility 
===========================================
[![Windows](https://github.com/eclipse/sumo/actions/workflows/build-windows.yml/badge.svg)](https://github.com/eclipse/sumo/actions/workflows/build-windows.yml)
[![Linux](https://github.com/eclipse/sumo/actions/workflows/build-linux.yml/badge.svg)](https://github.com/eclipse/sumo/actions/workflows/build-linux.yml)
[![macOS](https://github.com/eclipse/sumo/actions/workflows/build-macos.yml/badge.svg)](https://github.com/eclipse/sumo/actions/workflows/build-macos.yml)
[![sonarcloud security](https://sonarcloud.io/api/project_badges/measure?project=org.eclipse.sumo&metric=security_rating)](https://sonarcloud.io/summary/overall?id=org.eclipse.sumo)
[![Translation status](https://hosted.weblate.org/widgets/eclipse-sumo/-/svg-badge.svg)](https://hosted.weblate.org/engage/eclipse-sumo/)
![Repo Size](https://img.shields.io/github/repo-size/eclipse/sumo.svg)

What is SUMO
------------

["Simulation of Urban MObility" (SUMO)](https://sumo.dlr.de/) is an open source,
highly portable, microscopic traffic simulation package designed to handle
large road networks and different modes of transport.

It is mainly developed by employees of the [Institute of Transportation Systems
at the German Aerospace Center](https://www.dlr.de/ts).


Where to get it
---------------

You can download SUMO via our [downloads site](https://sumo.dlr.de/docs/Downloads.html).

As the program is still under development and is extended continuously, we advice you to
use the latest sources from our GitHub repository. Using a command line client
the following command should work:

        git clone --recursive https://github.com/eclipse/sumo


Contact
-------

To stay informed, we have a mailing list for SUMO, which 
[you can subscribe](https://dev.eclipse.org/mailman/listinfo/sumo-user) to.
Messages to the list can be sent to sumo-user@eclipse.org.
SUMO announcements will be made through the sumo-announce@eclipse.org list;
[you can subscribe](https://dev.eclipse.org/mailman/listinfo/sumo-announce) to it as well.
For further contact information, have a look at [this page](https://sumo.dlr.de/docs/Contact.html).


Build and Installation
----------------------

For Windows we provide pre-compiled binaries and CMake files to generate Visual Studio projects.
If you want to develop under Windows, please also clone the dependent libraries using

        git clone --recursive https://github.com/DLR-TS/SUMOLibraries

If you're using Linux, you should have a look whether your distribution already contains sumo.
There is also a [ppa for ubuntu users](https://launchpad.net/~sumo) and an
[open build service instance](https://build.opensuse.org/project/show/science:dlr).
If you want to build sumo yourself, the steps for ubuntu are:

        sudo apt-get install cmake python g++ libxerces-c-dev libfox-1.6-dev libgdal-dev libproj-dev libgl2ps-dev swig
        cd <SUMO_DIR> # please insert the correct directory name here
        export SUMO_HOME="$PWD"
        mkdir build/cmake-build && cd build/cmake-build
        cmake ../..
        make -j$(nproc)

For [detailed build instructions, have a look at our Documentation](https://sumo.dlr.de/docs/Developer/Main.html#build_instructions).


Getting started
---------------

To get started with SUMO, take a look at the docs/tutorial and examples directories,
which contain some example networks with routing data and configuration files.
There is also user documentation provided in the docs/ directory and on the
homepage.


Improving SUMO
--------------

Please use the [GitHub bug tracking tool](https://github.com/eclipse/sumo/issues) for bugs and requests, 
or file them to the list sumo-user@eclipse.org. Before
filing a bug, please consider to check with a current repository checkout
whether the problem has already been fixed.

We welcome patches, pull requests and other contributions! For details see [our contribution guidelines](CONTRIBUTING.md).

We use [Weblate for translating SUMO](https://hosted.weblate.org/projects/eclipse-sumo/). If you
want to add translation strings or a language, see [our contribution guidelines](CONTRIBUTING.md#translating).


License
-------

SUMO is licensed under the [Eclipse Public License Version 2](https://eclipse.org/legal/epl-v20.html).
For the licenses of the different libraries and supplementary code information is in the
subdirectories and the [Documentation](https://sumo.dlr.de/docs/Libraries_Licenses.html).
