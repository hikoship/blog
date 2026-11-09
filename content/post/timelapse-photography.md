---
title: "聊聊延时摄影"
date: "2026-10-25T00:00:00-08:00"
categories: "Photography"
summary: "上个月在罗马拍了一段延时素材，昨晚想后期一下，不小心肝到两点多。想到这几年的几次延时拍摄经历，窃以为水平有所精进，把一些小心得发出来抛砖引玉一下。"
draft: false
---

上个月在罗马拍了一段延时素材，昨晚想后期一下，不小心肝到两点多。想到这几年的几次延时拍摄经历，窃以为水平有所精进，把一些小心得发出来抛砖引玉一下。

## 什么是延时摄影

延时摄影（Time-lapse photography）可以近似理解为快进。把一段视频用几十上百倍的速度播放，通过云朵、光线、星空的变化来体现时间的流动，达成戏剧性的效果。

## 入门拍法：直接录视频

iPhone 就自带延时功能，只要选好位置，架好三脚架，切换到 timelapse 模式直接拍就可以了。

🌰：2021 年 Los Cabos 的日转夜，过度平滑，当然夜景画质不能细看。

[https://www.instagram.com/p/Cm2aW2ZIP-h/?hl=en](https://www.instagram.com/p/Cm2aW2ZIP-h/?hl=en)

也可以先用相机/手机录一段正常速度的视频，再导入 Premiere / DaVinci 等工具进行加速处理，Premiere 有手机 app，所以不需电脑就能完成。

🌰：2021 年 Key West 的日落，用 A7iii 录的，画质好很多

[https://www.instagram.com/p/CX7yFGHlAxq/?hl=en](https://www.instagram.com/p/CX7yFGHlAxq/?hl=en)

## 进阶拍法：等间隔拍摄照片，后期调光合成

直接拍视频方便快速，但是画质有妥协，后期空间小，成片效果有限，难以应付光线条件不佳的场景，比如星空，夜景，日转夜。

既然我们追求的效果是倍速播放，那么把一堆等间隔拍摄的照片以每秒 24 帧或 30 帧的速率播放，就能达到 timelapse 的目的。

### 前期准备

**1. 估算时长和间隔。**

根据最终成片的时长和帧率，能推算出需要的照片数量；再根据拍摄场景的真实时长，就能算出每两张照片的拍摄间隔。

比如把半小时的日落浓缩成 10 秒 30 帧的延时视频，需要拍 300 张照片，那么拍摄间隔是 1800 秒 / 300 = 6 秒。

**2. 机位选择**

机位和取景角度非常重要，一旦开拍就尽量不要移动相机，移动就前功尽弃了。如果拍摄日落、星空等场景，提前用 Photopills 等 app 查好各个天体的升起降落时间以及方位，防止拍到一半发现构图和自己预想的不一致。

**3. 用到的工具**

- 三脚架：正常尺寸的最好。如果是外出旅行，可以用考虑带一个便携的小三脚架。实在没有的话就利用周围的石头、平台手搓一个支架吧，可以在镜头下面垫镜头盖、随身小挂件等用于微调角度。
- 快门线：可以设置间隔和拍摄的照片数量，并减少拍摄时的抖动。如果相机内置了相关功能则可以省去。

### 拍摄时

**4. 曝光参数**

如果是纯白天或纯夜晚，整段素材的亮度变化不大，可以固定曝光参数，能省去很多后期的麻烦。

但如果涉及到日夜交替，在交替期间大概率需要盯着直方图，及时随着光线变化手动调节曝光（可能自动调节也行，但我没用过没法评论。并且自动调节大概率没法处理夜景或星空的情况）。

曝光三要素是光圈、快门、ISO。个人习惯是，优先调节快门，如果快门已经很慢但进光量还是不够，再调 ISO，不要碰光圈。

为什么？光圈会改变暗角和景深，会使成片在曝光参数变化的瞬间产生肉眼可察觉的卡顿或闪烁，很难通过后期消除。ISO 会改变画质，影响较小；而改变快门速度造成的变化在延时摄影中最不明显。

记得拍 RAW，这个不用多说了吧。

### 后期

**5. 平滑曝光**

只要中途调节了曝光，就会遇到光线不平滑的问题。比如拍摄日落，每当光线暗到需要提高曝光，下一帧的亮度就会突然提高，然后随着光线减弱，照片亮度缓缓下降，直到下一次提高曝光。

整个过程中，照片亮度的变化可以描绘成一个倒过来的 SGOV：

![IMAGE](https://asset-cdn.uscardforum.com/original/4X/9/f/a/9fab8e87af51c51c1148efeff7cefce75c0031a0.png)

想解决这个问题，不能不提神器 [LRTimelapse](https://lrtimelapse.com/)（LRT），它是专门为此诞生的。用户只需要调好几张关键帧的曝光，LRT 会析其他所有的帧，自动修正每一张的曝光，让整段素材的亮度平滑变化。LRT 是买断制，价格 $120 欧元，但是免费版也能处理 400 张以内的素材，相当于 16 秒 24 帧的成片，用来发个社交媒体完全够用了。

不过 LRT 需要配合 Lightroom Classic（LRC）使用，后者是需要付费的。

**6. 导出**

LRT 会把曝光修正写入到单独 metadata 文件中供 LRC 读取，至此 LRT 的使命就完成了。接下来的步骤，个人习惯用 LRC 把照片导出成 TIFF 格式。TIFF 包含了 metadata 的曝光修正，并且支持 16bit 色深。导出时可以选择把文件按序号命名，记得选上。

接下来打开免费的 DaVinci Resolve，它能够把数百张命名好的 TIFF 识别成一整段素材。把素材拖进 DaVinci，设置一下分辨率、帧率、画面裁剪，就大功告成了。

🌰：2021 年 Maui 的日落。我的第一个延时，时间只有三秒（读起来怪怪的）。光线变化不明显，所以没有调光，只用了 DaVinci 合成视频。

[https://www.instagram.com/p/CQj2NG1BwV7/?hl=en](https://www.instagram.com/p/CQj2NG1BwV7/?hl=en)

🌰：2021 年湾区某山头的日转夜+银河。头铁没有使用 LRT，而是在 LR 里一张张手搓曝光修正，可以看到入夜时画面有明显闪烁。

<iframe style="position: relative; width: 100%;" height="360" src="https://www.youtube.com/embed/Y907qjrWP_w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

🌰：上个月在罗马拍摄梵蒂冈的日落。刚刚肝出来的，第一次用 LRT，过渡明显更丝滑。

<iframe style="position: relative; width: 100%;" height="360" src="https://www.youtube.com/embed/KvKZxhL0XiY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

