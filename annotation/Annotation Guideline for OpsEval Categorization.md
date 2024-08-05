# Annotation Guideline for OpsEval Categorization

## Overview
In the OpsEval project, we aim to categorize operational and maintenance tasks within the industry. This categorization process is pivotal for understanding the spectrum of tasks and the required abilities to address them effectively. The process involves two primary steps: automated screening using GPT-4 for initial topic modeling, followed by a manual review process involving domain experts.

## 1. Task Categorization

### Objective

To categorize questions into one of eight distinct operational tasks based on industry relevance, task frequency, and significance within operational settings.

### Steps

1. **Review Initial Categorization**: Begin with the insights provided by GPT-4's topic modeling. Each question has been preliminarily categorized into one or more operational tasks.
2. **Understand Task Definitions**: Familiarize yourself with the details of the eight distinct tasks outlined in the provided Appendix. Each task has specific criteria and examples to guide your categorization.
3. **Assign Tasks**: For each question, decide which of the eight tasks it belongs to. A question should be categorized based on its core focus and the operational activity it pertains to.
4. **Justification**: Briefly justify your choice, especially if a question seems to fit into more than one category. Use the task definitions as a guide to support your decision.

### Detailed Task Categorizations

1. **General Knowledge**: Questions related to foundational concepts and practices in the Ops domain.
2. **Fault Analysis and Diagnostics**: Questions focusing on identifying and solving discrepancies or faults in systems or networks.
3. **Network Configuration**: Questions about optimal configurations for network devices to ensure efficient and secure operations.
4. **Software Deployment**: Questions dealing with the distribution and management of software applications.
5. **Monitoring and Alerts**: Questions on using monitoring tools to oversee system efficiency and setting up alert mechanisms.
6. **Performance Optimization**: Questions aimed at enhancing network and system performance.
7. **Automation Scripts**: Questions involving the creation of scripts to automate processes and reduce manual intervention.
8. **Miscellaneous**: Questions that do not fit into the above categories or involve elements from multiple categories.

#### Task Categorization Template

```markdown
Question ID: __________
Question: [Insert question text here]

Assigned Task: __________
Justification: [Provide a brief explanation for the task assignment here]
```

#### Example for Task Categorization

```markdown
Question ID: 001
Question: What steps should be taken to configure a firewall to prevent unauthorized access while allowing legitimate traffic?

Assigned Task: Network Configuration
Justification: This question specifically asks for optimal configuration strategies for a key network device (firewall) to ensure security and efficient operation, aligning perfectly with the 'Network Configuration' task.
```

## 2. Ability Categorization

### Objective
To classify questions based on the required cognitive ability to answer them: Knowledge Recall, Analytical Thinking, or Practical Application.

### Steps

1. **Review Definitions**: Read the descriptions of the three abilities in the provided Appendix. Each ability category has distinct characteristics and examples.
2. **Evaluate Questions**: Assess the cognitive demand of each question. Consider what is primarily required to answer the question effectively: recalling information, analyzing data/situations, or applying knowledge in practical scenarios.
3. **Assign Ability Level**: Determine the most appropriate ability category for each question. Some questions may seem to require multiple abilities; choose the one that is most critical for addressing the core challenge of the question.
4. **Justification**: Provide a rationale for your categorization, especially for questions that may not clearly fit into a single category. Refer to the ability definitions to support your categorization.

#### Detailed Ability Categorizations

1. **Knowledge Recall**: Requires recognizing and recalling core concepts and foundational knowledge.
2. **Analytical Thinking**: Demands deeper thought to dissect problems, correlate information, and derive conclusions.
3. **Practical Application**: Involves applying knowledge or analytical insights to provide actionable recommendations.

#### Ability Categorization Template

```markdown
Question ID: __________
Question: [Insert question text here]

Assigned Ability: __________
Justification: [Provide a brief explanation for the ability level assignment here]
```

#### Example for Ability Categorization

```markdown
Question ID: 002
Question: How would you optimize the performance of a network experiencing frequent bottlenecks?

Assigned Ability: Practical Application
Justification: The question requires applying knowledge of network systems and performance optimization techniques to propose specific solutions, hence it falls under 'Practical Application'.
```

## General Guidelines

- **Consistency**: Strive for consistency in your categorization decisions. If similar questions are categorized differently, reassess your choices to ensure they align with the task and ability definitions.
- **Collaboration**: When in doubt, discuss challenging questions with fellow experts. Collaboration can help clarify ambiguities and refine the categorization process.
- **Documentation**: Keep detailed notes on your decisions, especially for questions that required significant deliberation. This documentation will be valuable for future reference and analysis.

By following these guidelines, you will contribute to a comprehensive and nuanced categorization of operational tasks and required abilities. This effort is crucial for enhancing our understanding of the operational landscape and the diverse skills professionals need to navigate it effectively.