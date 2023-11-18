# Code Vision - Command Line Interface (CLI)
![](https://img.shields.io/pypi/v/code-vision-cli)
![](https://img.shields.io/pypi/wheel/code-vision-cli)
![](https://img.shields.io/pypi/pyversions/code-vision-cli)
![](https://img.shields.io/pypi/l/code-vision-cli)
![](https://img.shields.io/github/repo-size/saeedanabtawi/code-vision-cli)
![](https://img.shields.io/github/directory-file-count/saeedanabtawi/code-vision-cli)
![](https://img.shields.io/github/languages/code-size/saeedanabtawi/code-vision-cli)
![](https://img.shields.io/github/actions/workflow/status/saeedanabtawi/code-vision-cli/workflow.yml)

Code Vision CLI is a powerful tool for detecting plagiarism in source code, drawing inspiration from two pivotal research papers in the field. The first paper, titled "A Clustering Approach for Detecting Plagiarism in Source Code Data sets," and the second, "A Hybrid Method for Detecting Source-code Plagiarism in Computer Programming Courses," provide the foundational methodologies for our program. This tool excels in analyzing a collection of source files, identifying instances of plagiarism, and presenting these findings through an intuitive visual format, utilizing a weighted graph clustering algorithm.

This project harnesses the capabilities of well-regarded open-source compilers and parsers, notably [pycparser](https://github.com/eliben/pycparser), which is predominantly used for research and experimental endeavors. Code Vision CLI is particularly adept with the C99 standard, ensuring broad applicability and relevance in various coding environments.

You can check our whitepaper here [CodeVision](https://www.academia.edu/42023173/Source_code_plagiarism_detection_engine_CodeVision_)

### Installation
```
pip install code-vision-cli
```

### Usage
```
python code-vision-cli -i input -o output -a lcs -t 0.8
```

### Manual 

```
  -h, --help            show this help message and exit
  -i IN_DIR, --in_dir IN_DIR
                        Input directory must be in the project folder
  -o OUT_DIR, --out_dir OUT_DIR
                        Output directory must be in the project folder
  -a {jaccard,lcs}, --algorithm {jaccard,lcs}
                        Algorithm to use: "jaccard" or "lcs"
  -t THRESHOLD, --threshold THRESHOLD
                        Threshold value between 0.00 and 1.00

```

### Contributions

We openly welcome pull requests! If you're interested in contributing to the development of Code Vision CLI, your input and code contributions would be greatly appreciated.

### License

This project is released under the [MIT License](https://github.com/saeedanabtawi/CodeVisionCommandline/blob/master/LICENSE). Feel free to utilize, modify, and distribute this tool in accordance with the license specifications.

---
