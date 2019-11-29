#!/bin/bash
conan install . --install-folder cmake-build-debug
conan build . --build-folder cmake-build-debug