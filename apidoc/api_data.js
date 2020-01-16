define({ "api": [
  {
    "type": "delete",
    "url": "/v1/qa/{qa_id}",
    "title": "删除qa",
    "name": "DeleteQa",
    "group": "智能回复",
    "description": "<p>通过id删除Qa</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": " HTTP/1.1 200 OK\n{\n  \"code\": 0,\n  \"data\": [],\n  \"message\": \"ok\",\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./views/qa.py",
    "groupTitle": "智能回复"
  },
  {
    "type": "get",
    "url": "/v1/qa/",
    "title": "获取 qa数据",
    "name": "GetQa",
    "group": "智能回复",
    "description": "<p>获取qa数据（分页）</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page_size",
            "description": "<p>page_size</p>"
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "page_index",
            "description": "<p>page_index</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": " HTTP/1.1 200 OK\n{\n  \"code\": 0,\n  \"data\": [\n    {\n      \"answer\": \"每年 8 月启动晋升评估，9 月 1 日生效\",\n      \"id\": 1,\n      \"keywords\": [],\n      \"nlp_keywords\": [],\n      \"question\": \"晋升窗口期\"\n    }\n  ],\n  \"message\": \"ok\",\n  \"page_index\": \"1\",\n  \"page_size\": \"10\",\n  \"total\": 1\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./views/qa.py",
    "groupTitle": "智能回复"
  },
  {
    "type": "get",
    "url": "/v1/qa/{qa_id}",
    "title": "获取 qa数据通过qa id",
    "name": "GetQaById",
    "group": "智能回复",
    "description": "<p>通过qa id获取qa数据</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": " HTTP/1.1 200 OK\n{\n  \"code\": 0,\n  \"data\": [\n    {\n      \"answer\": \"每年 8 月启动晋升评估，9 月 1 日生效\",\n      \"id\": 1,\n      \"keywords\": [],\n      \"nlp_keywords\": [],\n      \"question\": \"晋升窗口期\"\n    }\n  ],\n  \"message\": \"ok\",\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./views/qa.py",
    "groupTitle": "智能回复"
  },
  {
    "type": "post",
    "url": "/v1/qa/",
    "title": "新增和修改qa数据",
    "name": "ModifyQa",
    "group": "智能回复",
    "description": "<p>新增和修改qa数据, 通过是否携带id</p>",
    "parameter": {
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"id\": 1,  # 当不携带id时就是新增，反之就是修改\n    \"question\": \"晋升窗口期\",\n    \"answer\": \"每年 8 月启动晋升评估，9 月 1 日生效\",\n    \"keywords\": [\"晋升\"]\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": " HTTP/1.1 200 OK\n{\n  \"code\": 0,\n  \"data\": [],\n  \"message\": \"ok\",\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./views/qa.py",
    "groupTitle": "智能回复"
  }
] });
