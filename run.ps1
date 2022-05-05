# $alexPath = "$home\Documents\Github\Alex"
# $bench = "$alexPath\out\build\x64-Debug\benchmark.exe"
# how to run exe
# & $bench

# $exePath = ".\out\build\x64-Debug\benchmark.exe"
$num = $args[0]
$exePath = ".\benchmarks\$num.exe"

write-output $exePath

###############################################################################
write-output "LONGITUDES #####################################################"
###############################################################################


# Ordinary longitudes
$file = "results/$num/longitudes/longitudes-ordinary-20M.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
        --keys_file=resources/longitudes-200M.bin.data `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}


# longitude 25%
$file = "results/$num/longitudes/longitudes25%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
        --keys_file=resources/longitudes/longitudes25%.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}

$file = "results/$num/longitudes/longitudes50%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    # longitude 50%
    & $exePath `
        --keys_file=resources/longitudes/longitudes50%.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}


# longitude 75%
$file = "results/$num/longitudes/longitudes75%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
    .\out\build\x64-Debug\benchmark.exe `
        --keys_file=resources/longitudes/longitudes75%.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}


# longitudes increasing%
$file = "results/$num/longitudes/longitudesIncreasing.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
        --keys_file=resources/longitudes/longitudesIncreasing.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}


# longitudes decreasing
$file = "results/$num/longitudes/longitudesDecreasing.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
    .\out\build\x64-Debug\benchmark.exe `
        --keys_file=resources/longitudes/longitudesDecreasing.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}

# longitudes sorted
$file = "results/$num/longitudes/sorted.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
        --keys_file=resources/longitudes/sorted.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}




###############################################################################
write-output "LONGLAT#########################################################"
###############################################################################

# Ordinary longlat
$file = "results/$num/longlat/longlat-ordinary-20M.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
        --keys_file=resources/longlat-200M.bin.data `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}


# longlat 25%
$file = "results/$num/longlat/longlat25%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
        --keys_file=resources/longlat/longlat25%.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}

# longlat 50%
$file = "results/$num/longlat/longlat50%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
        --keys_file=resources/longlat/longlat50%.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}


# longlat 75%
$file = "results/$num/longlat/longlat75%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
        --keys_file=resources/longlat/longlat75%.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}


# longlat increasing%
$file = "results/$num/longlat/longlatIncreasing.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
        --keys_file=resources/longlat/longlatIncreasing.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}


# longlat decreasing
$file = "results/$num/longlat/longlatDecreasing.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
    .\out\build\x64-Debug\benchmark.exe `
        --keys_file=resources/longlat/longlatDecreasing.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}

# longlat sorted
$file = "results/$num/longlat/sorted.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    & $exePath `
        --keys_file=resources/longlat/sorted.bin `
        --keys_file_type=binary `
        --sorted=false `
        --init_num_keys=10000000 `
        --total_num_keys=20000000 `
        --batch_size=1000000 `
        --insert_frac=0.5 `
        --lookup_distribution=uniform `
        --print_batch_stats `
        > $file
} else {
    write-output "$file already exists."
}


###############################################################################
# end
###############################################################################