
import os

from conan import ConanFile
from conan import tools
from conan.errors import ConanInvalidConfiguration
from conan.tools.cmake import CMake, cmake_layout, CMakeToolchain, CMakeDeps
from conan.tools.scm import Version


class XStudio(ConanFile):
    name = "xstudio"
    version = "2.0.1"

    settings = "os", "compiler", "build_type", "arch"
    package_type = "application"

    generators = "VirtualRunEnv"

    def requirements(self):
        self.requires("nlohmann_json/3.11.3")
        self.requires("imath/3.1.9")
        self.requires("openexr/3.2.3")
        self.requires("ffmpeg/6.1")
        self.requires("glew/2.2.0")
        #self.requires("caf/1.0.0")
        self.requires("caf/0.19.4")
        self.requires("spdlog/1.14.1")
        self.requires("freetype/2.13.2")
        self.requires("fmt/10.2.1")
        self.requires("stduuid/1.2.3")
        self.requires("pybind11/2.13.1")
        self.requires("opencolorio/2.3.1")

    def layout(self):
        cmake_layout(self)

    def generate(self):

        ct = CMakeToolchain(self)
        #ct.variables["Python_DIR"] = self.dependencies["cpython"].package_folder
        #ct.variables["Python_EXECUTABLE"] = self.dependencies["cpython"].package_folder + '/bin/python3.11'
        ct.variables["BUILD_DOCS"] = False
        ct.generate()

        cd = CMakeDeps(self)
        #deps.set_property("caf", "cmake_target_name", "JBIG::JBIG")
        cd.set_property("caf", "cmake_file_name", "caf")
        cd.set_property("caf::caf_core", "cmake_target_name", "caf::core")
        cd.set_property("caf::caf_io", "cmake_target_name", "caf::io")
        cd.set_property("ffmpeg::avcodec", "cmake_target_name", "FFMPEG::avcodec")
        cd.set_property("ffmpeg::avformat", "cmake_target_name", "FFMPEG::avformat")
        cd.set_property("ffmpeg::avutil", "cmake_target_name", "FFMPEG::avutil")
        cd.set_property("ffmpeg::swresample", "cmake_target_name", "FFMPEG::swresample")
        cd.set_property("ffmpeg::swscale", "cmake_target_name", "FFMPEG::swscale")
        #    deps.set_property("xz_utils", "cmake_target_name", "liblzma::liblzma")
        #    deps.set_property("libdeflate", "cmake_file_name", "Deflate")
        #    deps.set_property("libdeflate", "cmake_target_name", "Deflate::Deflate")
        cd.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()


    def package_info(self):
        self.cpp_info.includedirs = []
        self.cpp_info.libdirs = []

        bin_path = os.path.join(self.package_folder, "bin")
        self.output.info("Appending PATH environment variable: {}".format(bin_path))
        self.env_info.PATH.append(bin_path)


