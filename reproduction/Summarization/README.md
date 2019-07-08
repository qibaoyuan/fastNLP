# Summarization 

## Extractive Summarization


### Models

FastNLP中实现的模型包括：

1. Get To The Point: Summarization with Pointer-Generator Networks (See et al. 2017)
2. Searching for Effective Neural Extractive Summarization  What Works and What's Next (Zhong et al. 2019)




### Dataset

这里提供的摘要任务数据集包括：

- CNN/DailyMail
- Newsroom
- The New York Times Annotated Corpus
    - NYT
    - NYT50
- DUC
    - 2002 Task4
    - 2003/2004 Task1
- arXiv
- PubMed


其中公开数据集(CNN/DailyMail, Newsroom, arXiv, PubMed)预处理之后的下载地址：

- [百度云盘](https://pan.baidu.com/s/11qWnDjK9lb33mFZ9vuYlzA) (提取码：h1px)
- [Google Drive](https://drive.google.com/file/d/1uzeSdcLk5ilHaUTeJRNrf-_j59CQGe6r/view?usp=drivesdk)

未公开数据集(NYT, NYT50, DUC)数据处理部分脚本放置于data文件夹



### Dataset_loader

- SummarizationLoader: 用于读取处理好的jsonl格式数据集，返回以下field
    - text: 文章正文
    - summary: 摘要
    - domain: 可选，文章发布网站
    - tag: 可选，文章内容标签
    - labels: 抽取式句子标签



### Performance and Hyperparameters


| Model | ROUGE-1 | ROUGE-2 | ROUGE-L | Paper |
See 



## Abstractive Summarization
Still in Progress...