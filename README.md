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

# Week-by-week Documentation
## Week 1-2
* Stack Overflow, Software Engineering and Program Management 7z files were downloaded from the Stack Exchange [Data Dump](https://archive.org/details/stackexchange). We used the data dump from 2024-04-02. For SE & PM we downloaded them as single files whereas for SO we downloaded the separate files for Posts, Comments & PostHistory. This is because that is how the files are presented in the data dump.
* My second supervisor supplied a base set of scripts for the data extraction, previously used and authored by the first supervisor in a previous project. We extended the code to sift through tags, titles & bodies. The code was also extended to not only look through SO but SE & PM as well such that the resulting questions were placed in their respective origin sites. The keywords used were technical debt and tech debt. These keywords were chosen because they were highlighted in a previous paper(to be linked) as popular keywords that referenced technical debt in SO.
* The files are really huge, this led to errors in the parsing process, these were remedied by getting a hold of the root element in extract_posts_section in helper.py and clearing this root element. Not clearing the root element leads to a single element with a lot of empty child elements.
* Due to the new addition of code that looked through titles and bodies as well, some duplicate results were produced therefore we added a new functionality to remove the duplicate json files as this would simplify the process that was to come ahead.
* We perused through the resulting questions to get an idea of how they were structured and how to move forward.

## Week 3-5
* A Github repository containing the scripts and their documentation was created to serve as documentation.
* We went through the results and classified the questionS according to the TD types described in this paper(to be linked), questions that were methodology affiliated and those that are not directly related to TD but rather that the word TD was just used for context.
* The second supervisor provided a requirements template (to be linked) that acts as a guideline on how to search for requirements.
* A small sample of questions was taken from the results to get an idea on how to use the requirements template.