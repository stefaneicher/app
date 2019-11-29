from conans import ConanFile, CMake

class Calculator(ConanFile):
    name = "App"
    version = "0.1"
    url = "App"
    description = "<Description of Hello here>"
    settings = "os", "compiler", "build_type", "arch"
    requires = "Calculator/0.1@user/testing"
    generators = "cmake"
    exports_sources = "src/*", "CmakeLists.txt"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
