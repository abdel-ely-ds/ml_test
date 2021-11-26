# Test Data Science
## Before starting

- Fork the project in your namespace and **make it private**.
- Go To `Repository settings` then `User and group access` then `Add members` (Top right).
- Add the following emails `samer.azar@dataimpact.io`, `bibiana.martinez@dataimpact.io`, `raphael.person@dataimpact.io`, `ahmad.nadar@dataimpact.io`, `sina.akhavan@dataimpact.io`, `taleb.ahmed@dataimpact.io`


Some really important tips:

- Comments and automated tests are a big plus.
- To find examples of inputs and outputs, look at the unit tests.
- You might need pytest (and you can use any other packages).
- There are two main sections (Python & Data Science).
- Your answers for the Python section should be in the provided source files (in the `Python` folder).
- The Deep learning 2 is only dedicated to those applying for a CDI position.
- **Answering questions with a 🔴 are considered mandatory for CDI.**
- You are allowed to use the internet, however, you should fully understand the code you've written.
- If you have any questions, don't hesitate to send an email to `samer.azar@dataimpact.io`, `bibiana.martinez@dataimpact.io`,  `raphael.person@dataimpact.io`, `ahmad.nadar@dataimpact.io`, `sina.akhavan@dataimpact.io` and `taleb.ahmed@dataimpact.io` (all six)
 
# Python

Even though unit tests are already provided for some questions, extra points are given for adding more **(10 points)**

## Simple Python **(30 points)**

In this section we expect efficient code, meaning the time complexity should be at most linear O(n).

### 🔴 Exercise 1 **(10 points)**

Complete the function `remove_null` that takes as input a string of comma separated substrings (of the form **"2076,3B,19C,138D,NULL,NULL"**) and remove the NULLs (they are not necessarily located at the end).

### 🔴 Exercise 2 **(10 points)**

Complete the function `reverse_substrings` that takes as input a string, in the same format as in Exercise 1, and reverses the order of its substrings.

### 🔴 Exercise 3 **(10 points)**

##### Find the Missing Number
Given a list of n-1 integers, all of which are in the range of 1 to n, find the missing number. The list has no duplicated values. Complete the function `find_missing_number` with the most **efficient** way to find the missing integer.

## Advanced Python **(40 points)**

### Exercise 1 **(10 points)**

Write the generator `random_gen` that generates random numbers (use random module) between 10 and 20 and stops once it has generated the number 15.

### Exercise 2 **(10 points)**

Rewrite `decorator_to_str` to force the functions `add` and `get_info` to return string values.

### Exercise 3 **(10 points)**

Rewrite `ignore_exception` so that it ignores the exception in its argument and returns None if this exception is raised.

### Exercise 4 **(10 points)**

Write the tests for the class `CacheDecorator` without modifying it.

Hint: note that some of your tests should not pass as this class is a bit buggy. 

## Pandas **(20 points)**

### 🔴 Exercise 1 **(10 points)**

+    **The files are located in Python/pandas/data**

1) Import raw data from the files `17-10-2018.3880.gz` and `18-10-2018.3880.gz` into dataframes `df1_1` and `df1_2`, these files contain the following columns:

+ **categorieenseigne -- Category assigned to product by retailer**
+ **prixproduit -- Product price in the shop**
+ **identifiantproduit -- Product's id in the shops**
+ **ean -- Product's EAN** - Useless in the test
+ **disponible -- Product's availability** - Useless in the test

2) For each row of the column `categorieenseigne` replace "Promotions" by "promo".

3) Import the file `back_office.csv.gz` into dataframe `df2` , this file contains the following columns:

+ **pe_ref_in_enseigne -- Products id in the shops**
+ **pe_id -- Data Impact's products id**
+ **p_id_cat -- Category assigned to product by Data Impact**

4) Merge the data of the dataframes `df1_1` and `df1_2` with `df2` into `df_merged_1` and `df_merged_2`

### Exercise 2 **(10 points)**

- Get the average price by Data Impact product from the two dataframes `df_merged_1` and `df_merged_2`. (write the `average_prices` function)

The function should ouput a dict: data impact product --> price

- For each dataframe (`df_merged_1`, `df_merged_2`), get the list of unique Data Impact products per category

The function should output two dicts:
- dict1 : category --> list of data impact product for df_merged_1
- dict2 : category --> list of data impact product for df_merged_2

## API **(15 points)**

### Exercise 1 **(10 points)**

For this exercise you will be using the functions `remove_null` and `reverse_substring` developed on the Simple Python section.

In `api.py`, write a web service that listens on port `12345` and has a POST route `clean_string`.

This route should take a `raw_string` parameter and return a clean version of it as a response.

+ **raw_string**: string in the same format as expected for functions `remove_null` and `reverse_substring`
+ **response**: string, result of having applied both `remove_null` and `reverse_substring` to the input

Hint: you can use the flask library (or any library that suits you) to build the web service.

### Exercise 2 **(5 points)**

Write the `Dockerfile` so your web service can run in a Docker container and still work properly

The commands to build the image and run the container should be in `run.sh`

# Data Science

For this section you will be working on notebooks that will use GPU for the training of a neural network. 

Here's is the link for the notebook [Machine Learning & Deep Learning 1](https://colab.research.google.com/drive/1PoczRgvn_rZJFNpUmUw9aBFeaNA5aMZW), you will need to make your own copy of the notebook under the menu `File->Save a copy in Drive`.

The notebook contains the necessary commands and instructions to enable GPU and upload the files found in  `Data_science/` that will be used in the exercises. 

Mandatory questions will be indicated with a 🔴 within the notebooks

**Don't forget share the link of your colab notebook with your answers**

## Machine Learning

### Exercise 1 **(10 points)**

Using sklearn library, find the fitting algorithm to classify whether someone has diabetes or not according to the dataset found in  `Data_science/machine_learning/diabetes.csv`. The column containing the target is 'Outcome'. An accuracy of around 0.7 is considered acceptable

## Deep Learning 1

### Exercise 1 -- General Questions **(20 points)**

### Exercise 2 --  Overfit and underfit **(8 points)**

### Exercise 3 -- Recommender Systems **(22 points)**

### Exercise 4 -- Computer Vision **(35 points)**

## Deep Learning 2
**This part is only for people who are applying for a CDI**

This is the link for the notebook [Deep Learning 2](https://colab.research.google.com/drive/1H6QXjrYHrNFR9WcfKLM3joLiwERlMMpn), you will need to make your own copy of the notebook under the menu `File->Save a copy in Drive`.

The notebook contains the necessary commands and instructions to enable GPU and upload the files found in  `Data_science/` that will be used in the exercises.

### Exercise 1 -- Some more questions about Deep Learning **(7 points)**

### Exercise 2 -- Gradient Descent and momentum in numpy **(10 points)**

### Exercise 3 -- Natural Language Classifier **(25 points)**

### Exercise 4 -- Captioning **(15 points)**
