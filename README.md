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

## Leaderboard

### Wired Network Operations (English)

| |Zero-shot              | | | |3-shot| | | | |
|------|-----------------------|------|------|------|------|------|------|------|-------|
|Models|Naïve                  |SC    |CoT   |CoT+SC|Naïve |SC    |CoT   |CoT+SC|Best Score|
|✨ GPT-4|/                      |/     |/     |/     |/     |/     |88.70 |88.70 |88.70  |
|✨ Yi-34B-Chat|57.75                  |59.14 |65.11 |68.79 |68.16 |68.37 |78.09 |80.06 |80.06  |
|✨ Qwen-72B-Chat|70.41                  |70.50 |72.38 |72.56 |70.32 |70.32 |70.13 |70.22 |72.56  |
|✨ GPT-3.5-turbo|66.60                  |66.80 |69.60 |72.00 |68.30 |68.30 |70.90 |72.50 |72.50  |
|✨ ERNIE-Bot-4.0|61.15                  |61.15 |70.00 |70.00 |60.00 |60.00 |70.00 |70.00 |70.00  |
|✨ Qwen1.5-14B-Chat|54.90                  |56.44 |64.09 |67.10 |52.23 |53.52 |59.54 |64.18 |67.10  |
|✨ Qwen1.5-14B-Base|34.88                  |34.88 |60.82 |60.82 |65.55 |65.55 |47.08 |47.08 |65.55  |
|✨ DevOps-Model-14B-Chat|30.69                  |30.59 |55.77 |63.63 |63.85 |61.96 |41.15 |44.01 |63.85  |
|✨ Qwen-14B-Chat|43.78                  |47.81 |56.58 |59.40 |62.09 |59.70 |49.06 |55.88 |62.09  |
|✨ LLaMA-2-13B|41.80                  |46.50 |53.10 |58.70 |53.30 |53.00 |56.80 |61.00 |61.00  |
|✨ InternLM2-Chat-20B|56.36                  |56.36 |26.18 |26.18 |60.48 |60.48 |45.10 |45.10 |60.48  |
|✨ LLaMA-2-70B-Chat|25.29                  |25.29 |57.97 |58.06 |52.97 |52.97 |58.55 |58.55 |58.55  |
|✨ InternLM2-Chat-7B|49.74                  |49.74 |56.19 |56.19 |48.20 |48.20 |49.74 |49.74 |56.19  |
|✨ LLaMA-2-7B|39.50                  |40.00 |45.40 |49.50 |48.20 |46.80 |52.00 |55.20 |55.20  |
|✨ Qwen-7B-Chat|45.90                  |46.00 |47.30 |50.10 |52.10 |51.00 |48.30 |49.80 |52.10  |
|✨ Gemma_7B|25.09                  |25.09 |50.86 |50.86 |30.24 |30.24 |51.56 |51.56 |51.56  |
|✨ InternLM-7B|38.70                  |38.70 |43.90 |43.90 |45.20 |45.20 |51.40 |51.40 |51.40  |
|✨ Chinese-Alpaca-2-13B|37.70                  |37.70 |49.70 |49.70 |48.60 |48.60 |50.50 |50.50 |50.50  |
|✨ Mistral-7B|29.27                  |29.27 |46.30 |46.30 |47.22 |47.22 |45.58 |45.58 |47.22  |
|✨ AquilaChat2-34B|36.63                  |36.63 |44.83 |44.83 |46.65 |46.65 |NULL  |NULL  |46.65  |
|✨ ChatGLM3-6B|43.38                  |43.38 |44.59 |44.59 |42.10 |42.10 |43.47 |43.47 |44.59  |
|✨ ChatGLM2-6B|24.80                  |24.70 |36.60 |36.50 |37.60 |37.60 |40.50 |40.50 |40.50  |
|✨ Chinese-LLaMA-2-13B|29.40                  |29.40 |37.80 |37.80 |40.40 |40.40 |28.80 |28.80 |40.40  |
|✨ Gemma_2B|26.46                  |26.46 |33.42 |33.42 |26.63 |26.63 |37.54 |37.54 |37.54  |
|✨ Baichuan-13B-Chat|18.30                  |20.40 |28.60 |37.00 |24.10 |26.70 |18.20 |17.80 |37.00  |
|✨ Baichuan2-13B-Chat|14.10                  |15.30 |24.10 |25.80 |32.30 |33.10 |25.60 |27.70 |33.10  |


> For more leaderboard results, please checkout the [leaderboard folder](./leaderboard/) in this repository.

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
| Mobile Communication Network | |

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
