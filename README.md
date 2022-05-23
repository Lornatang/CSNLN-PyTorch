# CSNLN-PyTorch

### Overview

This repository contains an op-for-op PyTorch reimplementation
of [Image Super-Resolution with Cross-Scale Non-Local Attention and Exhaustive Self-Exemplars Mining](https://arxiv.org/abs/2006.01424v1).

### Table of contents

- [CSNLN-PyTorch](#csnln-pytorch)
    - [Overview](#overview)
    - [Table of contents](#table-of-contents)
    - [About Image Super-Resolution Using Very Deep Residual Channel Attention Networks](#about-image-super-resolution-with-cross-scale-non-local-attention-and-exhaustive-self-exemplars-mining)
    - [Download weights](#download-weights)
    - [Download datasets](#download-datasets)
    - [How Test and Train](#how-test-and-train)
        - [Test](#test)
        - [Train model](#train-model)
        - [Resume train model](#resume-train-model)
    - [Result](#result)
    - [Credit](#credit)
        - [Image Super-Resolution with Cross-Scale Non-Local Attention and Exhaustive Self-Exemplars Mining](#image-super-resolution-with-cross-scale-non-local-attention-and-exhaustive-self-exemplars-mining)

## About Image Super-Resolution with Cross-Scale Non-Local Attention and Exhaustive Self-Exemplars Mining

If you're new to CSNLN, here's an abstract straight from the paper:

Deep convolution-based single image super-resolution (SISR) networks embrace the benefits of learning from large-scale external image resources for
local recovery, yet most existing works have ignored the long-range feature-wise similarities in natural images. Some recent works have successfully
leveraged this intrinsic feature correlation by exploring non-local attention modules. However, none of the current deep models have studied another
inherent property of images: cross-scale feature correlation. In this paper, we propose the first Cross-Scale Non-Local (CS-NL) attention module with
integration into a recurrent neural network. By combining the new CS-NL prior with local and in-scale non-local priors in a powerful recurrent fusion
cell, we can find more cross-scale feature correlations within a single low-resolution (LR) image. The performance of SISR is significantly improved
by exhaustively integrating all possible priors. Extensive experiments demonstrate the effectiveness of the proposed CS-NL module by setting new
state-of-the-arts on multiple SISR benchmarks.

## Download weights

- [Google Driver](https://drive.google.com/drive/folders/17ju2HN7Y6pyPK2CC_AqnAfTOe9_3hCQ8?usp=sharing)
- [Baidu Driver](https://pan.baidu.com/s/1yNs4rqIb004-NKEdKBJtYg?pwd=llot)

## Download datasets

Contains DIV2K, DIV8K, Flickr2K, OST, T91, Set5, Set14, BSDS100 and BSDS200, etc.

- [Google Driver](https://drive.google.com/drive/folders/1A6lzGeQrFMxPqJehK9s37ce-tPDj20mD?usp=sharing)
- [Baidu Driver](https://pan.baidu.com/s/1o-8Ty_7q6DiS3ykLU09IVg?pwd=llot)

## How Test and Train

Both training and testing only need to modify the `config.py` file. 

### Test

- line 31: `upscale_factor` change to `2`.
- line 33: `mode` change to `valid`.
- line 71: `model_path` change to `results/pretrained_models/CSNLN_x2-DIV2K-xxxxxxxx.pth.tar`.

### Train model

- line 31: `upscale_factor` change to `2`.
- line 33: `mode` change to `train`.
- line 35: `exp_name` change to `CSNLN_x2`.

### Resume train model

- line 31: `upscale_factor` change to `2`.
- line 33: `mode` change to `train`.
- line 35: `exp_name` change to `CSNLN_x2`.
- line 49: `resume` change to `samples/CSNLN_x2/epoch_xxx.pth.tar`.

## Result

Source of original paper results: https://arxiv.org/pdf/1807.02758.pdf

In the following table, the value in `()` indicates the result of the project, and `-` indicates no test.

| Method | Scale |      Set5 (PSNR/SSIM)      |      Set14(PSNR/SSIM)      |     BSD100(PSNR/SSIM)      |     Urban100(PSNR/SSIM)     |    Manga109(PSNR/SSIM)     |
|:------:|:-----:|:--------------------------:|:--------------------------:|:--------------------------:|:---------------------------:|:--------------------------:|
|  DRLN  |   2   | 38.28(**-**)/0.9616(**-**) | 34.12(**-**)/0.9223(**-**) | 32.40(**-**)/0.9024(**-**) | 33.25(**-**)/0.9386(**-**)  | 39.37(**-**)/0.9785(**-**) |
|  DRLN  |   3   | 34.74(**-**)/0.9300(**-**) | 30.66(**-**)/0.8482(**-**) | 29.33(**-**)/0.8105(**-**) | 29.13(**-**)/0.8712(**-**)  | 34.45(**-**)/0.9502(**-**) |
|  DRLN  |   4   | 32.68(**-**)/0.9004(**-**) | 28.95(**-**)/0.7888(**-**) | 27.80(**-**)/0.7439(**-**) | 27.22(**-**)/0.8168(**-**)  | 31.43(**-**)/0.9201(**-**) |
         
Low Resolution / Super Resolution / High Resolution
<span align="center"><img src="assets/result.png"/></span>

### Credit

#### Image Super-Resolution with Cross-Scale Non-Local Attention and Exhaustive Self-Exemplars Mining

_Yiqun Mei, Yuchen Fan, Yuqian Zhou, Lichao Huang, Thomas S. Huang, Humphrey Shi_ <br>

**Abstract** <br>
Deep convolution-based single image super-resolution (SISR) networks embrace the benefits of learning from large-scale external image resources for
local recovery, yet most existing works have ignored the long-range feature-wise similarities in natural images. Some recent works have successfully
leveraged this intrinsic feature correlation by exploring non-local attention modules. However, none of the current deep models have studied another
inherent property of images: cross-scale feature correlation. In this paper, we propose the first Cross-Scale Non-Local (CS-NL) attention module with
integration into a recurrent neural network. By combining the new CS-NL prior with local and in-scale non-local priors in a powerful recurrent fusion
cell, we can find more cross-scale feature correlations within a single low-resolution (LR) image. The performance of SISR is significantly improved
by exhaustively integrating all possible priors. Extensive experiments demonstrate the effectiveness of the proposed CS-NL module by setting new
state-of-the-arts on multiple SISR benchmarks.

[[Code(PyTorch)]](https://github.com/yulunzhang/RCAN) [[Paper]](https://arxiv.org/pdf/2006.01424v1)

```
@inproceedings{Mei2020image,
  title={Image Super-Resolution with Cross-Scale Non-Local Attention and Exhaustive Self-Exemplars Mining},
  author={Mei, Yiqun and Fan, Yuchen and Zhou, Yuqian and Huang, Lichao and Huang, Thomas S and Shi, Humphrey},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2020}
@InProceedings{Lim_2017_CVPR_Workshops,
  author = {Lim, Bee and Son, Sanghyun and Kim, Heewon and Nah, Seungjun and Lee, Kyoung Mu},
  title = {Enhanced Deep Residual Networks for Single Image Super-Resolution},
  booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
  month = {July},
  year = {2017}
}
```
