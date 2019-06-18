# ExpenseClaimAutomationSystem
---
[![Build Status](https://www.travis-ci.com/snnucs/ExpenseClaimAutomationSystem.svg?branch=master)](https://www.travis-ci.com/snnucs/ExpenseClaimAutomationSystem)
[![GitHub license](https://img.shields.io/github/license/snnucs/ExpenseClaimAutomationSystem.svg)](https://github.com/snnucs/ExpenseClaimAutomationSystem/blob/master/LICENSE)
![GitHub release](https://img.shields.io/github/release/snnucs/ExpenseClaimAutomationSystem.svg?style=plastic)
大数据时代下的财务自动化报销系统,2019年国家大学生创新创业训练计划创新训练子计划项目


## 快速开始
### 开发环境
```bash
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
✨🍰✨
```

### 测试
```bash
python manage.py test
isort *.py -c -vb
```
### 启动服务
```bash
python manage.py runserver
```

## 代码风格

## 开源协议 & 作者
* 作者: 
  * Qi Zhao([zhaoqi99@outlook.com](mailto:zhaoqi99@outlook.com))
  * Xiangrong Feng
  * Xuying Meng
  * Yali Chen
* 开源协议:[GNU General Public License v3.0](https://github.com/snnucs/ExpenseClaimAutomationSystem/blob/master/LICENSE)