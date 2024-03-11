---
language:
- en
- zh
pretty_name: OpsEval
tags:
- AIOps
- LLM
- Operations
- Benchmark
- Dataset
license: apache-2.0
task_categories:
- question-answering
size_categories:
- 1K<n<10K
---

# OpsEval Dataset

[Website](https://opseval.cstcloud.cn/content/home) | [Reporting Issues](https://github.com/NetManAIOps/OpsEval-Datasets/issues/new)

## Introduction

The OpsEval dataset represents a pioneering effort in the evaluation of Artificial Intelligence for IT Operations (AIOps), focusing on the application of Large Language Models (LLMs) within this domain. In an era where IT operations are increasingly reliant on AI technologies for automation and efficiency, understanding the performance of LLMs in operational tasks becomes crucial. OpsEval offers a comprehensive task-oriented benchmark specifically designed for assessing LLMs in various crucial IT Ops scenarios.

This dataset is motivated by the emerging trend of utilizing AI in automated IT operations, as predicted by Gartner, and the remarkable capabilities exhibited by LLMs in NLP-related tasks. OpsEval aims to bridge the gap in evaluating these models' performance in AIOps tasks, including root cause analysis of failures, generation of operations and maintenance scripts, and summarizing alert information.

## Highlights

- **Comprehensive Evaluation**: OpsEval includes 7184 multi-choice questions and 1736 question-answering (QA) formats, available in both English and Chinese, making it one of the most extensive benchmarks in the AIOps domain.
- **Task-Oriented Design**: The benchmark is tailored to assess LLMs' proficiency across different crucial scenarios and ability levels, offering a nuanced view of model performance in operational contexts.
- **Expert-Reviewed**: To ensure the reliability of our evaluation, dozens of domain experts have manually reviewed our questions, providing a solid foundation for the benchmark's credibility.
- **Open-Sourced and Dynamic Leaderboard**: We have open-sourced 20% of the test QA to facilitate preliminary evaluations by researchers. An online leaderboard, updated in real-time, captures the performance of emerging LLMs, ensuring the benchmark remains current and relevant.

## Dataset Structure

Here is a brief overview of the dataset structure:

- `/dev/` - Examples for few-shot in-context learning.
- `/test/` - Test sets of OpsEval.
<!-- - `/metadata/` - Contains metadata related to the dataset. -->

## Dataset Informations

| Dataset Name  | Open-Sourced Size |
| ------------- | ------------- | 
| Wired Network | 1563 |
| Oracle Database | 395 |
| 5G Communication | 349 |
| Log Analysis | 310 | 

<!-- ## Usage

To use the OpsEval dataset in your research or project, please follow these steps:

1. Clone this repository to your local machine or server.
2. [Insert specific steps if needed, like environment setup, dependencies installation].
3. Explore the dataset directories and refer to the `metadata` directory for understanding the dataset schema and organization.
4. [Optional: include example code or scripts for common operations on the dataset]. -->

<!-- ## License

[Specify the license under which the OpsEval dataset is distributed, e.g., MIT, GPL, Apache 2.0]

## Acknowledgments

We would like to thank [Acknowledgments to contributors, institutions, funding bodies, etc.]

For any questions or further information, please contact [Insert contact information]. -->

## Website

For evaluation results on the full OpsEval dataset, please checkout our official website [OpsEval Leaderboard](https://opseval.cstcloud.cn/content/home).

## Paper

For a detailed description of the dataset, its structure, and its applications, please refer to our paper available at: [OpsEval: A Comprehensive IT Operations Benchmark Suite for Large Language Models](https://arxiv.org/abs/2310.07637)

### Citation

Please use the following citation when referencing the OpsEval dataset in your research:

```
@misc{liu2024opseval,
      title={OpsEval: A Comprehensive IT Operations Benchmark Suite for Large Language Models}, 
      author={Yuhe Liu and Changhua Pei and Longlong Xu and Bohan Chen and Mingze Sun and Zhirui Zhang and Yongqian Sun and Shenglin Zhang and Kun Wang and Haiming Zhang and Jianhui Li and Gaogang Xie and Xidao Wen and Xiaohui Nie and Minghua Ma and Dan Pei},
      year={2024},
      eprint={2310.07637},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```