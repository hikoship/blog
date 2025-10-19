+++
categories = ["technology"]
date = "2015-07-27T00:00:00Z"
draft = true
tags = "rime"
title = "rime 输入法"

+++

`symbols.yaml`

punctuator:
  full_shape:
    " ": {commit: "　"}
    "!": {commit: "！"}
    "\"": {pair: ["“", "”"]}
    "#": ["＃", "⌘"]
    "$": ["$", "+"]

`symbols.custom.yaml`

patch:
    "punctuator/full_shape/$": ['$', +]

custom 文件中作出的改变会在重新部署后反映到原配置文件中

加了 commit 不出现选单
