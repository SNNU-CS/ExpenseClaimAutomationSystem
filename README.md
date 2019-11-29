# ExpenseClaimAutomationSystem Monorepo
---
[![Build Status](https://www.travis-ci.com/snnucs/ExpenseClaimAutomationSystem.svg?branch=master)](https://www.travis-ci.com/snnucs/ExpenseClaimAutomationSystem)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/919045824a9b4c4681756b0a46664e9b)](https://app.codacy.com/app/ZhaoQi99/ExpenseClaimAutomationSystem?utm_source=github.com&utm_medium=referral&utm_content=snnucs/ExpenseClaimAutomationSystem&utm_campaign=Badge_Grade_Dashboard)
[![GitHub license](https://img.shields.io/github/license/snnucs/ExpenseClaimAutomationSystem.svg)](https://github.com/snnucs/ExpenseClaimAutomationSystem/blob/master/LICENSE)
![GitHub release](https://img.shields.io/github/release/snnucs/ExpenseClaimAutomationSystem.svg?style=plastic)

## 简介

大数据时代下的财务自动化报销系统,2019年国家大学生创新创业训练计划创新训练子计划项目

- [wangwang](./wangwang) - back-end 
- [miaomiao](./miaomiao) - front-end

## 生产地址

* 前端镜像 https://hub.docker.com/r/zhaoqi99/miaomiao
* 后端镜像 https://hub.docker.com/r/zhaoqi99/wangwang
* 数据库:http://139.9.236.103:5432/
* 数据库Admin: http://139.9.236.103:8080/
* 前端web:http://139.9.236.103/
* 后端API:http://139.9.236.103:8000/api/
* 后端Admin:http://139.9.236.103:8000/admin/
* API文档:http://139.9.236.103:8000/docs/

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
ENV=dev python manage.py makemigrations
ENV=dev python manage.py migrate
✨🍰✨
```

### 测试
```bash
ENV=test python manage.py test
isort *.py -c -vb
```
### 启动服务
```bash
ENV=dev python manage.py runserver(make debv)
```
## 快速开始(前端)

使用[yarn](https://yarnpkg.com/zh-Hans/)作为包管理工具,需先在本地安装[yarn](https://yarnpkg.com/zh-Hans/)

```bash
yarn install
yarn serve
```

## 开发规范

### 开发流程

按照[Github-flow](https://guides.github.com/introduction/flow/index.html)进行开发，即:

1. 从master分支上checkout出一条新分支 
2. 新分支开发完成后，向master发起一个[pull requessst](https://help.github.com/articles/using-pull-requests/)
3. 大家一起review你的代码，不断修改和提交代码
4. pull request被接受，合并进master

### 代码提交

发起pull request前，务必通过下述命令将其rebase至最新的master分支上:

```bash
git fetch origin
git rebase origin/master
git push origin
```
**后端**:使用flake8,yapf,isort进行风格检查，commit代码前，务必使用下述指令对代码进行格式化

```bash
	isort --recursive -c -df .
	yapf --recursive --diff .
	flake8 .
```

**前端**: #Todo

### 代码风格
* 后端:
  * [Django编码风格](<https://docs.djangoproject.com/zh-hans/2.2/internals/contributing/writing-code/coding-style/>)
  * [PEP8](<https://www.python.org/dev/peps/pep-0008/>)
* 前端:
  * #Todo

### 分支命名

存在一个长期分支master，其余分支命名规则如下，多个单词之间以`-`风格，如无对应issue可省略issue id:

* **feature/{issue id}/***(例:feature/1/add-teacher或feature/add-teacher)
* **fix/{issue id}/***  (例:fix/2/fix-travis-ci或fix/fix-travis-ci)
* **patch/***

### Commit Message

```
<type>(<scope>): <subject>
<空行>
<body>
<空行>
<footer>
```

推荐使用[commitizen](<https://github.com/commitizen/cz-cli>)来格式化commit message

## 开源协议 & 作者
* 作者: 
  * Qi Zhao([zhaoqi99@outlook.com](mailto:zhaoqi99@outlook.com))
  * Xiangrong Feng
  * Xuying Meng
  * Yali Chen
* 开源协议:[GNU General Public License v3.0](https://github.com/snnucs/ExpenseClaimAutomationSystem/blob/master/LICENSE)
