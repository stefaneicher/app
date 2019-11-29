#!/bin/bash
#conan remove "*" -f
#conan search "*"
conan create . user/testing
#conan search "*"


mkdir mypkg && cd mypkg
conan new Hello/0.1 -t