# ai_replay
使用nlp和jieba来分析问题，并在qa库中查询相关的问题
可用于智能客服系统

## Install
```
git clone https://github.com/vissssa/ai_replay.git
```
[Tencent_AILab_ChineseEmbedding.txt](https://ai.tencent.com/ailab/nlp/embedding.html)
从这里下载，如果内存不够(我)，可以裁剪一下，我只选取了前1w

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