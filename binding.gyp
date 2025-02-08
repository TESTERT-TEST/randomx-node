{
    "targets": [
        {
            "target_name": "randomxhash",
            "dependencies": [],
            "sources": [
                "randomx.cc",
                "randomx/src/aes_hash.cpp",
                "randomx/src/allocator.cpp",
                "randomx/src/blake2_generator.cpp",
                "randomx/src/dataset.cpp",
                "randomx/src/instruction.cpp",
                "randomx/src/randomx.cpp",
                "randomx/src/reciprocal.cpp",
                "randomx/src/superscalar.cpp",
                "randomx/src/virtual_machine.cpp"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "<(module_root_dir)/randomx/src"
            ],
            "libraries": [
                "<(module_root_dir)/randomx/build/librandomx.a"
            ],
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
