# A Gender-Classifying Neural Network

Built for our *Topics in Computer Science: Brain Inspired Computing* class taught by Professor Konstantinos Michmizos.

## Usage

1. Clone this repository: `git clone git@github.com:davidchen/gender_matcher.git`
2. Change into the newly cloned repo: `cd gender_matcher`
3. Create a Python virtual environment: `python -m venv myvenv`
4. Source the venv:
    * Windows: `myvenv\Scripts\activate.bat`
    * Linux: `source myvenv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run: `python classifier.py`


## Results

By default, all the images inside the `faces` directory will be classified. The program will return a list of image names, a gender, and a percentage. Each percentage is the confidence level of the classifier as to the gender of the subject in the image. For example, in this list:

```python
"Face 1.png"  |   Male    | 43.22%
"Face 2.png"  |   Male    | 72.14%
"Face 3.png"  |   Female  | 7.02%
"Face 4.png"  |   Female  | 99.12%
"Face 5.png"  |   Male    | 33.21%
```

The subject in `"Face 2.png"` is determined to be a male with around 72% confidence.
