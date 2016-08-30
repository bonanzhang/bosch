import xgboost
import pandas
import time
import io
import zipfile
print('imports complete')
def load_and_unzip(filename):
    print('loading and unzipping large training data file %s' % (filename))
    t0 = time.time()
    df = pandas.read_csv(filename, compression='zip')
    t1 = time.time()
    print('completed in %.3f seconds' % (t1-t0))
    return df

train_numeric_filename = 'resources/train_numeric.csv.zip'
df_train = load_and_unzip(train_numeric_filename)

test_numeric_filename = 'resources/test_numeric.csv.zip'
df_test = load_and_unzip(test_numeric_filename)
