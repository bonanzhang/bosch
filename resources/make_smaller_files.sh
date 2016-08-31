fullname=$1
filename=$(basename "$fullname")
extension="${filename##*.}"
filename="${filename%.*}"
prefix="split_${filename}_"
cat $fullname | tail -n +2 | split -l 50000 - $prefix --additional-suffix=.csv --suffix-length=1
for file in $prefix*
do
    head -n 1 $fullname > tmp_file
    cat $file >> tmp_file
    mv -f tmp_file $file
done

