{
    "targets": [
        {
            "target_name": "randomxhash",
            "sources": [
                "randomx.cc",
                "randomx/src/aes_hash.cpp",
                "randomx/src/allocator.cpp",
                "randomx/src/blake2_generator.cpp",
                "randomx/src/dataset.cpp",
                "randomx/src/instruction.cpp",
                "randomx/src/randomx.cpp",
                "randomx/src/reciprocal.c",
                "randomx/src/superscalar.cpp",
                "randomx/src/virtual_machine.cpp"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "randomx/src",
                "randomx/src/blake2"
            ],
            "defines": [
                "RANDOMX_STATIC",
                "RANDOMX_INTERNAL_AES=0"
            ],
            "cflags_cc": [
                "-std=c++11",
                "-fPIC",
                "-O2",
                "-Wall",
                "-Wextra"
            ],
            "cflags_c": [
                "-std=c99",
                "-fPIC",
                "-O2"
            ],
            "ldflags": [
                "-lpthread"
            ],
            "conditions": [
                ["OS=='linux'", {
                    "cflags_cc+": [
                        "-march=x86-64"
                    ],
                    "ldflags+": [
                        "-Wl,-rpath,'$$ORIGIN'"
                    ]
                }],
                ["OS=='mac'", {
                    "xcode_settings": {
                        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                        "CLANG_CXX_LANGUAGE_STANDARD": "c++11",
                        "CLANG_CXX_LIBRARY": "libc++",
                        "MACOSX_DEPLOYMENT_TARGET": "10.13"
                    },
                    "cflags_cc+": [
                        "-mmacosx-version-min=10.13"
                    ]
                }],
                ["OS=='win'", {
                    "defines+": [
                        "NOMINMAX",
                        "WIN32_LEAN_AND_MEAN"
                    ]
                }]
            ]
        }
    ]
}
