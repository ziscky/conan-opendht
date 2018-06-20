#!/usr/bin/env python3

from conans import ConanFile, CMake, tools

class OpenDHTConan(ConanFile):
    name = "opendht"
    version = "master"
    description = """A C++11 Distributed Hash Table implementation"""
    url = "https://github.com/savoirfairelinux/opendht"
    license = "GNU GPLv3"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    sources = "https://github.com/matlo607/opendht.git"
    source_dir = "{name}-{version}".format(name=name, version=version)

    def requirements(self):
        self.requires("argon2/master@matthieu/testing")

    def source(self):
        self.run("git clone {} {}".format(self.sources, self.source_dir))
        with tools.chdir(self.source_dir):
            #self.run("git checkout {branch}".format(branch=self.version))
            self.run("git checkout {branch}".format(branch="conan-fix-build-cmake"))

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.definitions["OPENDHT_PYTHON"] = "ON"
        cmake.definitions["OPENDHT_BUILD_TOOLS"] = "ON"
        cmake.definitions["OPENDHT_PROXY_SERVER"] = "OFF"
        cmake.definitions["OPENDHT_PROXY_SERVER_IDENTITY"] = "ON"
        cmake.definitions["OPENDHT_PROXY_CLIENT"] = "OFF"
        cmake.definitions["OPENDHT_PUSH_NOTIFICATIONS"] = "OFF"
        cmake.definitions["OPENDHT_ARGON2"] = "OFF"
        #cmake.definitions["OPENDHT_TEST"] = "ON"
        cmake.configure(source_folder=self.source_dir)
        cmake.build()
        #cmake.test()
        cmake.install()

    def package(self):
        # already done by 'make install'
        pass

    def package_info(self):
        pass
        #self.cpp_info.includedirs = ['include']
        #self.cpp_info.libdirs = ['lib']
        #self.cpp_info.bindirs = ['bin']
        #self.env_info.path.append(path.join(self.package_folder, "bin"))
