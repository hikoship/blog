+++
categories = "Tech"
date = "2015-10-11T00:00:00Z"
tags = "Deduplication Linux Ubuntu"
title = "Install Destor on Ubuntu 14.04"
summary = "Destor is a platform for data deduplication evaluation developed by Min Fu."
+++

[*Destor*](https://github.com/fomy/destor) is a platform for data deduplication evaluation developed by [Min Fu](https://github.com/fomy). It runs on 64-bit Linux. I wanted to use it to compare the performance of existing deduplication schemes and those of my own. However, the installation process is a little bit complicated, which took me two days to make it work. My platform is 64-bit Ubuntu 14.04 with kernel 3.13.

1. Download glib. Extract it to `[PATH_TO_GLIB]`.
2. Run the following commands.

```
sudo apt-get install zlib1g-dev
sudo apt-get install libffi-dev
cd [PATH_TO_GLIB]
./configure
make
sudo make install
cd /usr/local/
sudo cp include/glib-2.0/* include/
sudo cp lib/glib-2.0/include/glibconfig.h include/
cd lib
sudo link libglib-2.0.so libglib.so
sudo apt-get install libssl-dev
sudo apt-get install autotools-dev
sudo apt-get install automake
cd [DIR_OF_DESTOR]
./configure
automake --add-missing
make
sudo make install
```
