# Technical Debt Questions on the Stack Exchange Network
## Pre-requisites
To be able to run the scripts, you will need to have [Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) installed.
## Extraction
### Download the data dump
Download the following 7z files from the Stack Exchange [Data Dump](https://archive.org/details/stackexchange):
* `stackoverflow.com-Posts.7z`
* `stackoverflow.com-PostHistory.7z`
* `stackoverflow.com-Comments.7z`
* `pm.stackexchange.com.7z`
* `softwareengineering.stackexchange.com.7z`

Once downloaded, the `stackoverflow` files have to be placed into the `soData/` directory, the `pm` file into the `pmData/` directory and the `softwareengineering` file into the `seData/` directory.
**_(These should not be decompressed as the program is already set to do so)_**.

### Technical Debt Question Extraction
1. In the terminal, change to the `scripts/` directory.
2. Create the conda environment. 

```
conda env create -f env.yaml
``` 

3. Activate the conda environment.

```
conda activate se-extraction
```

4. Run the script `main.py`
```
 python main.py
```
5. Once extraction is completed, delete the conda environment.
```
conda deactivate
conda env remove -n se-extraction
```

_Note: There is a p7zip dependency in the yaml file. The name of this dependency may differ in accordance with the OS being used_.
