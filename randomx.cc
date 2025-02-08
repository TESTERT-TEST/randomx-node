#include <nan.h>
#include <node.h>
#include <node_buffer.h>
#include <v8.h>
#include <stdint.h>
#include <vector>
#include "randomx/src/randomx.h"

using namespace v8;

randomx_cache* rxCache = nullptr;
randomx_dataset* rxDataset = nullptr;
randomx_vm* rxVM = nullptr;
bool initialized = false;

void initialize() {
    if (!initialized) {
        randomx_flags flags = randomx_get_flags();
        rxCache = randomx_alloc_cache(flags);
        if (!rxCache) {
            Nan::ThrowError("Failed to allocate RandomX cache.");
            return;
        }

        randomx_init_cache(rxCache, "default_key", 12);

        rxDataset = randomx_alloc_dataset(flags);
        if (!rxDataset) {
            Nan::ThrowError("Failed to allocate RandomX dataset.");
            return;
        }

        randomx_init_dataset(rxDataset, rxCache, 0, randomx_dataset_item_count());

        rxVM = randomx_create_vm(flags, rxCache, rxDataset);
        if (!rxVM) {
            Nan::ThrowError("Failed to create RandomX VM.");
            return;
        }

        initialized = true;
    }
}

void randomXInit(const v8::FunctionCallbackInfo<v8::Value>& args) {
    initialize();
    args.GetReturnValue().Set(args.This());
}

void randomXHash(const v8::FunctionCallbackInfo<v8::Value>& args) {
    Isolate* isolate = args.GetIsolate();
    HandleScope scope(isolate);

    if (args.Length() < 1 || !node::Buffer::HasInstance(args[0])) {
        isolate->ThrowException(Exception::TypeError(
            String::NewFromUtf8(isolate, "Expected a buffer as input").ToLocalChecked()
        ));
        return;
    }

    const char* input = node::Buffer::Data(args[0]);
    size_t length = node::Buffer::Length(args[0]);
    char result[32];

    if (!initialized) {
        initialize();
    }

    randomx_calculate_hash(rxVM, input, length, result);
    args.GetReturnValue().Set(Nan::CopyBuffer(result, 32).ToLocalChecked());
}

void cleanup() {
    if (rxVM) randomx_destroy_vm(rxVM);
    if (rxDataset) randomx_release_dataset(rxDataset);
    if (rxCache) randomx_release_cache(rxCache);
    initialized = false;
}

void cleanupModule(const v8::FunctionCallbackInfo<v8::Value>& args) {
    cleanup();
    args.GetReturnValue().Set(Nan::New("RandomX resources cleaned up").ToLocalChecked());
}

void Init(Local<Object> exports) {
    NODE_SET_METHOD(exports, "init", randomXInit);
    NODE_SET_METHOD(exports, "hash", randomXHash);
    NODE_SET_METHOD(exports, "cleanup", cleanupModule);
}

NODE_MODULE(randomxhash, Init)
