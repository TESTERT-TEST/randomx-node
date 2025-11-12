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
        "-O2"
      ],
      "cflags_c": [
        "-std=c99",
        "-fPIC",
        "-O2"
      ],
      "ldflags": [
        "-L<(module_root_dir)/randomx/build",
        "-lrandomx",
        "-lpthread"
      ],
      "conditions": [
        ["OS=='linux'", {
          "cflags_cc+": ["-Wno-narrowing"]
        }]
      ]
    }
  ]
}
