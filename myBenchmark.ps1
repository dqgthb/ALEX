$alexPath = "$home\Documents\Github\Alex"

$bench = "$alexPath\out\build\x64-Debug\benchmark.exe"
# how to run exe
# & $bench

# Ordinary longitudes
.\out\build\x64-Debug\benchmark.exe `
--keys_file=resources/longitudes-200M.bin.data `
--keys_file_type=binary `
--sorted=false `
--init_num_keys=10000000 `
--total_num_keys=20000000 `
--batch_size=1000000 `
--insert_frac=0.5 `
--lookup_distribution=uniform `
--print_batch_stats `
> results/longitudes/longitudes-ordinary-20M.txt


# longitude 25%
.\out\build\x64-Debug\benchmark.exe `
--keys_file=resources/longitudes/longitudes25%.bin `
--keys_file_type=binary `
--sorted=false `
--init_num_keys=10000000 `
--total_num_keys=20000000 `
--batch_size=1000000 `
--insert_frac=0.5 `
--lookup_distribution=uniform `
--print_batch_stats `
> results/longitudes/longitudes25%.txt

# longitude 50%
.\out\build\x64-Debug\benchmark.exe `
--keys_file=resources/longitudes/longitudes50%.bin `
--keys_file_type=binary `
--sorted=false `
--init_num_keys=10000000 `
--total_num_keys=20000000 `
--batch_size=1000000 `
--insert_frac=0.5 `
--lookup_distribution=uniform `
--print_batch_stats `
> results/longitudes/longitudes50%.txt


# longitude 75%
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
> results/longitudes/longitudes75%.txt


# longitudes increasing%
.\out\build\x64-Debug\benchmark.exe `
--keys_file=resources/longitudes/longitudesIncreasing.bin `
--keys_file_type=binary `
--sorted=false `
--init_num_keys=10000000 `
--total_num_keys=20000000 `
--batch_size=1000000 `
--insert_frac=0.5 `
--lookup_distribution=uniform `
--print_batch_stats `
> results/longitudes/longitudesIncreasing.txt


###############################################################################

# Ordinary longlat
.\out\build\x64-Debug\benchmark.exe `
--keys_file=resources/longlat-200M.bin.data `
--keys_file_type=binary `
--sorted=false `
--init_num_keys=10000000 `
--total_num_keys=20000000 `
--batch_size=1000000 `
--insert_frac=0.5 `
--lookup_distribution=uniform `
--print_batch_stats `
> results/longlat/longlat-ordinary-20M.txt


# longlat 25%
.\out\build\x64-Debug\benchmark.exe `
--keys_file=resources/longlat/longlat25%.bin `
--keys_file_type=binary `
--sorted=false `
--init_num_keys=10000000 `
--total_num_keys=20000000 `
--batch_size=1000000 `
--insert_frac=0.5 `
--lookup_distribution=uniform `
--print_batch_stats `
> results/longlat/longlat25%.txt

# longlat 50%
.\out\build\x64-Debug\benchmark.exe `
--keys_file=resources/longlat/longlat50%.bin `
--keys_file_type=binary `
--sorted=false `
--init_num_keys=10000000 `
--total_num_keys=20000000 `
--batch_size=1000000 `
--insert_frac=0.5 `
--lookup_distribution=uniform `
--print_batch_stats `
> results/longlat/longlat50%.txt


# longlat 75%
.\out\build\x64-Debug\benchmark.exe `
--keys_file=resources/longlat/longlat75%.bin `
--keys_file_type=binary `
--sorted=false `
--init_num_keys=10000000 `
--total_num_keys=20000000 `
--batch_size=1000000 `
--insert_frac=0.5 `
--lookup_distribution=uniform `
--print_batch_stats `
> results/longlat/longlat75%.txt


# longlat increasing%
.\out\build\x64-Debug\benchmark.exe `
--keys_file=resources/longlat/longlatIncreasing.bin `
--keys_file_type=binary `
--sorted=false `
--init_num_keys=10000000 `
--total_num_keys=20000000 `
--batch_size=1000000 `
--insert_frac=0.5 `
--lookup_distribution=uniform `
--print_batch_stats `
> results/longlat/longlatIncreasing.txt


###############################################################################

###############################################################################