// Copyright (c) Microsoft Corporation.
// Licensed under the MIT license.

#include "zipf.h"
#include <cassert>

template <class T>
bool load_binary_data(T data[], int length, const std::string& file_path) {
    std::ifstream is(file_path.c_str(), std::ios::binary | std::ios::in);
    if (!is.is_open()) {
        return false;
    }
    is.read(reinterpret_cast<char*>(data), std::streamsize(length * sizeof(T)));
    std::cerr << length * sizeof(T) << " bytes requested." << std::endl;
    if (is) {
        std::cerr << "all " << is.gcount() << " chars read successfully" << std::endl;
    }
    else {
        std::cerr << "error: only " << is.gcount() << " could be read.";
    }
    is.close();
    return true;
}

template <class T>
bool load_text_data(T array[], int length, const std::string& file_path) {
    std::ifstream is(file_path.c_str());
    if (!is.is_open()) {
        return false;
    }
    int i = 0;
    std::string str;
    while (std::getline(is, str) && i < length) {
        std::istringstream ss(str);
        ss >> array[i];
        i++;
    }
    is.close();
    return true;
}

template <class T>
T* get_search_keys(T array[], int num_keys, int num_searches) {
    std::mt19937_64 gen(std::random_device{}());
    std::uniform_int_distribution<int> dis(0, num_keys - 1);
    auto* keys = new T[num_searches];
    for (int i = 0; i < num_searches; i++) {
        int pos = dis(gen);
        keys[i] = array[pos];
    }
    return keys;
}

template <class T>
T* get_search_keys_zipf(T array[], int num_keys, int num_searches) {
    auto* keys = new T[num_searches];
    ScrambledZipfianGenerator zipf_gen(num_keys);
    for (int i = 0; i < num_searches; i++) {
        int pos = zipf_gen.nextValue();
        keys[i] = array[pos];
    }
    return keys;
}


// warning! num_actual_inserts == num_lookups_per_batch for fair comparison
// proof of concept. Might be buggy!
template <class T>
T* get_search_keys_just_inserted(T array[], int num_keys, int num_actual_inserts, int num_searches) {

    assert(num_searches == num_actual_inserts);

    auto* keys = new T[num_searches];
    for (int i = num_keys - num_actual_inserts, j = 0; i < num_keys; i++, ++j) {
        keys[j] = array[i];
    }
    return keys;
}

