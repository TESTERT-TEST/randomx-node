{
    "targets": [
        {
            "target_name": "randomxhash",
            "dependencies": [],
            "sources": [
                "randomx.cc",
                "randomx/src/randomx.h",
                "randomx/src/dataset.cpp",
                "randomx/src/virtual_machine.cpp",
                "randomx/src/aes_hash.cpp",
                "randomx/src/blake2_generator.cpp",
                "randomx/src/randomx.cpp"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "randomx/src"
            ],
            "defines": [],
            "cflags_cc": [
                "-std=c++17",
                "-fPIC",
                "-fexceptions",
                "-Ofast",
                "-march=native"
            ],
            "cflags": [
                "-fPIC",
                "-fexceptions",
                "-Ofast",
                "-march=native"
            ],
            "link_settings": {
                "libraries": [
                    "-Wl,-rpath,./build/Release/"
                ]
            },
            "conditions": [
                ["OS=='mac'", {
                    "xcode_settings": {
                        "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
                    }
                }]
            ]
        }
    ]
}

