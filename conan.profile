[settings]
arch=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=gnu17
compiler.libcxx=libstdc++11
compiler.version=11
os=Linux
os.distro=RHEL9

[options]
jasper/*:with_libjpeg=libjpeg-turbo
libtiff/*:jpeg=libjpeg-turbo
libraw/*:with_jpeg=libjpeg-turbo
openimageio/*:with_libjpeg=libjpeg-turbo

cpython/*:shared=True

qt/*:shared=True
qt/*:with_harfbuzz=True
qt/*:with_libjpeg=libjpeg-turbo
qt/*:qtquickcontrols = True
qt/*:qtquickcontrols2 = True

[replace_requires]
libjpeg/*:libjpeg-turbo/3.0.3

[conf]
tools.files.download:retry=1
tools.files.download:retry_wait=5
tools.cmake.cmaketoolchain:generator=Ninja
