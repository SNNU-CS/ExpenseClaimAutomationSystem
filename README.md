# ExpenseClaimAutomationSystem Monorepo

---

[![Build Status](https://www.travis-ci.com/snnucs/ExpenseClaimAutomationSystem.svg?branch=master)](https://www.travis-ci.com/snnucs/ExpenseClaimAutomationSystem)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/919045824a9b4c4681756b0a46664e9b)](https://app.codacy.com/app/ZhaoQi99/ExpenseClaimAutomationSystem?utm_source=github.com&utm_medium=referral&utm_content=snnucs/ExpenseClaimAutomationSystem&utm_campaign=Badge_Grade_Dashboard)
[![GitHub license](https://img.shields.io/github/license/snnucs/ExpenseClaimAutomationSystem.svg)](https://github.com/snnucs/ExpenseClaimAutomationSystem/blob/master/LICENSE)
![GitHub release](https://img.shields.io/github/release/snnucs/ExpenseClaimAutomationSystem.svg?style=plastic)

## 简介

大数据时代下的财务自动化报销系统,2019 年国家大学生创新创业训练计划创新训练子计划项目

- [wangwang](./wangwang) - back-end
- [miaomiao](./miaomiao) - front-end

## 生产地址

- 前端镜像 https://hub.docker.com/r/zhaoqi99/miaomiao
- 后端镜像 https://hub.docker.com/r/zhaoqi99/wangwang
- 数据库:http://139.9.236.103:5432/
- 数据库 Admin: http://139.9.236.103:8080/
- 前端 web:http://139.9.236.103/
- 后端 API:http://139.9.236.103:8000/api/
- 后端 Admin:http://139.9.236.103:8000/admin/
- API 文档:http://139.9.236.103:8000/docs/

## 快速开始(后端)

### 开发环境

- Python>=3.5
- PostgreSQL>=10
- Django>=2.0

```bash
pip3 install virtualenv
virtualenv env
source env/bin/activate # source env/Scipts/activate
pip install -r requirements.txt
pip install -r dev-requirements.txt
ENV=dev python manage.py makemigrations
ENV=dev python manage.py migrate
✨🍰✨
```

### 测试

```bash
ENV=test python manage.py test(make test)
isort --recursive -c -df .(make check)
yapf --recursive --diff .(make check)
```

### 启动服务

```bash
ENV=dev python manage.py runserver(make dev)
```

## 快速开始(前端)

_使用[yarn](https://yarnpkg.com/zh-Hans/)作为包管理工具的,需先在本地安装[yarn](https://yarnpkg.com/zh-Hans/)_

```bash
npm install
npm run serve
```

or

```bash
yarn install
yarn serve
```

## 开发规范

### 开发流程

按照[Github-flow](https://guides.github.com/introduction/flow/index.html)进行开发，即:

1. 从[master](https://github.com/snnucs/ExpenseClaimAutomationSystem/tree/master)分支上 checkout 出一条新分支
2. 新分支开发完成后，向 master 发起一个[pull request](https://help.github.com/articles/using-pull-requests/)
3. 大家一起 review 你的代码，不断修改和提交代码
4. [pull request](https://help.github.com/articles/using-pull-requests/)被接受，合并进 master

### 代码提交

发起 pull request 前，务必通过下述命令将其 rebase 至最新的 master 分支上:

```bash
git fetch origin
git rebase origin/master
git push origin
```

**后端**:使用 flake8,yapf,isort 进行风格检查，commit 代码前，务必使用下述指令对代码进行格式化(`make format`)

```bash
isort -rc .
yapf --recursive -i .
```

**前端**: #Todo

### 代码风格

- 后端:

  - [Django 编码风格](https://docs.djangoproject.com/zh-hans/2.2/internals/contributing/writing-code/coding-style/)
  - [PEP8](https://www.python.org/dev/peps/pep-0008/)

- 前端:
  - #Todo

### 分支命名

存在一个长期分支 master，其余分支命名规则如下，多个单词之间以`-`风格，如无对应 issue 可省略 issue id:

- **feature/{issue id}/\***(例:feature/1/add-teacher 或 feature/add-teacher)
- **fix/{issue id}/\*** (例:fix/2/fix-travis-ci 或 fix/fix-travis-ci)
- **patch/\***
- **issues/{issue id}/\***

### Commit Message

```
<type>(<scope>): <subject>
<空行>
<body>
<空行>
<footer>
```

推荐使用[commitizen](https://github.com/commitizen/cz-cli)来格式化 commit message

## 开源协议 & 作者

- 作者:

  - Qi Zhao([zhaoqi99@outlook.com](mailto:zhaoqi99@outlook.com))
  - Xiangrong Feng
  - Xuying Meng
  - Yali Chen

- 开源协议:[GNU General Public License v3.0](https://github.com/snnucs/ExpenseClaimAutomationSystem/blob/master/LICENSE)
