# Stratified Random Sampling for Parallel Coprus
## Description
While developing a corpus, data from different domains and sources is used and it is very rare that you find exact propostion of data from these different domains/sources. So instead of just collecting and dumping data, it is better to use sampling technique to adequately split the data into train, test and dev set. This python script can be used to split your data (collected from different sources) into train, test and dev/validation set using stratified random sampling. 

## Author:
- Moodser Hussain
- COMSATS University Islamabad, Lahore Campus
- Email: moodser.hussain@gmail.com

## Usage
1. This script support both type of splits (1) Percentage and (2) Number 
2. Place all parallel files of English/Lang1 in 'en' directory and Urdu/Lang2 in 'ur' directory.
3. Place this script in the root directory of 'en' and 'ur' folder.
4. Name of files should end with language extention (e.g. all files should have extenstion .en that are placed in 'en' directory).
5. During execution program will ask for split type (percentage/number) and values so provide these values according according to your requirements.
6. It will automatically fetch files from both directories to generate parallel files for train, test and validation set.

## Acknowledgements
- Dr. Rao Muhammad Adeel Nawab
- Dr. Muhammad Sharjeel

## Note
This script was used for English-Urdu langauge pair. If you are intending to use it any other language pair, you can change the extensions accordingly.
