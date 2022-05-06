# $alexPath = "$home\Documents\Github\Alex"
# $bench = "$alexPath\out\build\x64-Debug\benchmark.exe"
# how to run exe
# & $bench

# $exePath = ".\out\build\x64-Debug\benchmark.exe"
$num = $args[0]
$num2 = $args[1]
$name = "min$num" + "max$num2"
$exePath = ".\benchmarks\$name.exe"

write-output $exePath

###############################################################################
write-output "LONGITUDES #####################################################"
###############################################################################

$outputFile

# Ordinary longitudes
$file = "results/$name/longitudes/longitudes-ordinary-20M.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}

# longitude 25%
$file = "results/$name/longitudes/longitudes25%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}

# longitudes 50%
$file = "results/$name/longitudes/longitudes50%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}

# longitudes 75%
$file = "results/$name/longitudes/longitudes75%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
    & $exePath `
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
}
else {
    write-output "$file already exists."
}

# longitudes increasing%
$file = "results/$name/longitudes/longitudesIncreasing.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}

# longitudes decreasing
$file = "results/$name/longitudes/longitudesDecreasing.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
    & $exePath `
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
}
else {
    write-output "$file already exists."
}

# longitudes sorted
$file = "results/$name/longitudes/sorted.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}

# longitudes increase by 1
$file = "results/$name/longitudes/increaseBy1.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}




###############################################################################
write-output "LONGLAT#########################################################"
###############################################################################

# Ordinary longlat
$file = "results/$name/longlat/longlat-ordinary-20M.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}

# longlat 25%
$file = "results/$name/longlat/longlat25%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}

# longlat 50%
$file = "results/$name/longlat/longlat50%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}

# longlat 75%
$file = "results/$name/longlat/longlat75%.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}

# longlat increasing%
$file = "results/$name/longlat/longlatIncreasing.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}

# longlat decreasing
$file = "results/$name/longlat/longlatDecreasing.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
    & $exePath `
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
}
else {
    write-output "$file already exists."
}

# longlat sorted
$file = "results/$name/longlat/sorted.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}

# longlat increase by 1
$file = "results/$name/longlat/increaseBy1.txt"
if ( -not (test-path -path $file -pathtype leaf)) {
    write-output "writing $file ..."
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
}
else {
    write-output "$file already exists."
}



###############################################################################
# end
###############################################################################