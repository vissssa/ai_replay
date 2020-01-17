# ai_replay
使用nlp和jieba来分析问题，并在qa库中查询相关的问题
可用于智能问答系统

## Install
```
git clone https://github.com/vissssa/ai_replay.git
```
[Tencent_AILab_ChineseEmbedding.txt](https://ai.tencent.com/ailab/nlp/embedding.html)
从这里下载完整版  
如果内存不够(穷)，可以裁剪一下，我就是选取了前10w，也挺好用  
迷你版链接:https://pan.baidu.com/s/14H5tLZWp6V61Umq69kCD8g  密码:j7aw
## Usage
```bash
> cd ai_replay
> pip install -r requirements.txt
# your config(mysql,redis. etc)
> flask db migrate
> flask db upgrade

> celery  -A tasks.celery worker -B --loglevel=info
> python app.py
```

生成[apidoc](https://apidocjs.com/)
```bash
apidoc -i . -o apidoc/
```
## Contributing

PRs accepted.

## License

[MIT © vissssa](./LICENSE)