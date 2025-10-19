+++
categories = "Tech"
date = "2015-10-06T00:00:00Z"
title = "在 Android 6.0 Marshmallow 上开启 Google Now"
summary = "总体步骤和之前 5.1 类似，只是有些选项的位置发生了改变，需要稍加寻找。Nexus 5 刷原厂镜像（MRA58K）测试通过。"
+++

**Note:**

感谢 [Tiany](https://disqus.com/by/disqus_6awjvNqfHQ/) 提醒，使用此法将导致 Google Play Store 不能使用。目前我通过登录另一个 Google 帐号解决该问题，参考了 [Cham Maxium](https://disqus.com/by/chammaxium/) 的方法：

> 在 Account 里删除原有 Google 账号，再重新登入后，方可解决该问题。

以及 V2EX 上 [ssenkrad](http://www.v2ex.com/member/ssenkrad) 的方法:

> @lonelinsky 5.0 时候发现的， 6.0 是否还适用不得而知，手机上登陆两个 google 账号，开启 google now 之后退出重新登录任意一个，两个账号就都能用 play 了。

感谢二位。

---

总体步骤和之前 5.1 类似，只是有些选项的位置发生了改变，需要稍加寻找。Nexus 5 刷原厂镜像（MRA58K）测试通过。

1. 更改系统语言为英语；
2. 关闭 `Location`，开启飞行模式，打开 Wi-Fi；
3. 进入 `Settings -> Apps`，**点击右上角三个点，选择 `Show System`**；
4. 在列表中找到 `Google App`，点击 `Storage`，点击 `MANAGE SPACE`，点击`CLEAR ALL DATA`；
5. 对 `Google Play services`、`Google Play Store`、`Google Services Framework` 进行同样操作；
6. 回到`Settings`，选择 `Google`，点击 `Search & Now`，点击 `Accounts & privacy`，点击 `Google Account`，选择 `Sign out`；
7. 回到刚才的界面，再次点击 `Google Account`，选择之前登录过的帐号。
