You can launch the Jupyter notebook by doing:
```bash
jupyter notebook src/bosch.ipynb
```

Using the Intel Python distribution for a possible performance (training speed) boost:
```bash
source activate idp
```

if the csv files are too long, you can use the split command like this to make them into smaller files:
```bash
cat train_numeric.csv | tail -n +2 | split -l 50000 - split_train_numeric_ --additional-suffix=.csv --suffix-length=1
for file in split_train_numeric_*
do
    head -n 1 train_numeric.csv > tmp_file
    cat $file >> tmp_file
    mv -f tmp_file $file
done
```
This splits the csv file train_numeric.csv into smaller files with at most 50000 entries each, with the original header replicated in each file.
They are named as split_train_numeric_a.csv, split_train_numeric_b.csv, and so on.
