# Multimodal Image Text Demo

这是一个多模态 AI 入门项目。

项目目标是使用 CLIP 模型完成图片和文本匹配：输入一张图片和多个候选文本，程序会判断图片最匹配哪一句文本。

## 项目背景

多模态 AI 指模型可以同时处理多种类型的数据，比如：

- 文本
- 图片
- 音频
- 视频

本项目使用 CLIP 模型完成图片和文本之间的相似度匹配。

CLIP 的核心思想是：

- 图片可以被编码成向量
- 文本也可以被编码成向量
- 图片向量和文本向量会被放到同一个语义空间
- 图片向量和文本向量越接近，说明它们语义越相似

## 项目功能

本项目会读取测试图片，并与多个候选文本进行匹配。

程序会输出每个文本和图片的匹配分数，并给出最高分的文本。

示例候选文本：

a black handwritten number 0 on a white background
a black handwritten number 1 on a white background
a black handwritten number 2 on a white background
a black handwritten number 3 on a white background
a black handwritten number 4 on a white background
a black handwritten number 5 on a white background
a black handwritten number 6 on a white background
a black handwritten number 7 on a white background
a black handwritten number 8 on a white background
a black handwritten number 9 on a white background
a cat
a car
a dog

## 项目结构

multimodal-image-text-demo/
├─ main.py
├─ README.md
└─ test_images/
   ├─ test_digit_3.png
   └─ test_digit_7.png

## 运行环境

建议使用 Python 3.10 或 Python 3.12。
需要安装：
torch
torchvision
pillow
transformers

## 创建虚拟环境
在项目根目录或 D:\ai-engineering 下创建一个新的虚拟环境：
cd D:\ai-engineering
python -m venv .venv-multimodal

## 激活虚拟环境：
.\.venv-multimodal\Scripts\Activate.ps1
如果 PowerShell 不允许运行脚本，可以先执行：
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
然后重新激活：
.\.venv-multimodal\Scripts\Activate.ps1

## 安装依赖
升级 pip：
python -m pip install --upgrade pip
安装 CPU 版 PyTorch：
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
安装其他依赖：
python -m pip install pillow transformers
注意：如果 pip.exe 被 Windows 应用程序控制策略阻止，不要直接使用：
pip install ...
应该使用：
python -m pip install ...

## 运行方式
进入项目目录：
cd D:\ai-engineering\ai-engineering-from-scratch\my-projects\multimodal-image-text-demo
运行：
python main.py
注意：如果已经激活 .venv-multimodal，直接运行 python main.py 即可。
不要再手动调用旧环境：
D:\ai-engineering\.venv\Scripts\python.exe
否则可能会出现：
ModuleNotFoundError: No module named 'torch'
因为旧 .venv 环境中没有安装当前项目需要的依赖。

## 代码流程
加载 CLIP 模型和 CLIPProcessor
读取本地测试图片
准备候选文本
将图片和文本同时交给 CLIPProcessor 处理
使用 CLIPModel 计算图片与每一句文本的匹配分数
使用 softmax 将匹配分数转换成概率
输出最匹配的文本
核心代码理解
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
这两行用于加载 CLIP 模型和预处理器。
inputs = processor(
    text=candidate_texts,
    images=image,
    return_tensors="pt",
    padding=True,
)
这一步会把图片和文本转换成模型可以处理的张量。
outputs = model(**inputs)
这一步让 CLIP 计算图片和文本之间的匹配关系。
probs = outputs.logits_per_image.softmax(dim=1)[0]
这一步把匹配分数转换成概率。
Best match
概率最高的文本，就是模型认为最符合图片内容的描述。

## 示例输出
测试数字 7 图片时，程序可能输出：
============================================================
Image: test_images\test_digit_7.png
------------------------------------------------------------
1. a handwritten digit two
   score: 0.3598
2. a handwritten digit seven
   score: 0.1702
3. a handwritten digit three
   score: 0.1614
4. a handwritten digit zero
   score: 0.0815
5. a handwritten digit nine
   score: 0.0657
6. a handwritten digit six
   score: 0.0434
7. a handwritten digit eight
   score: 0.0345
8. a handwritten digit five
   score: 0.0323
9. a handwritten digit four
   score: 0.0278
10. a handwritten digit one
   score: 0.0233
11. a dog
   score: 0.0000
12. a car
   score: 0.0000
13. a cat
   score: 0.0000
------------------------------------------------------------
Best match: a handwritten digit two
============================================================
这个结果说明代码已经成功跑通，但 CLIP 把数字 7 判断成了数字 2。
这不是代码错误，而是模型能力边界。
为什么 CLIP 会判断错手写数字
CLIP 不是专门训练来识别 MNIST 手写数字的模型。
它更擅长理解自然图片和自然语言描述，比如：
a cat
a dog
a car
a person riding a bike
a photo of food
但对于 28x28 的黑白手写数字小图，CLIP 不一定准确。
所以本项目的重点不是追求手写数字识别准确率，而是理解多模态图文匹配流程。

## 如何优化结果

可以尝试以下优化方式。
1. 使用更自然的文本描述
比起：
a handwritten digit seven
可以改成：
a black handwritten number 7 on a white background
CLIP 更适合自然语言描述，而不是非常短的标签。
2. 放大图片
CLIP 通常处理正常尺寸的图片，不适合太小的 28x28 图片。
可以在读取图片后加入：
image = Image.open(image_path).convert("RGB")
image = image.resize((224, 224))
3. 使用更清晰的测试图片
手写数字尽量清晰、居中、少倾斜。
4. 换更适合 CLIP 的图片
如果使用猫、狗、汽车、食物、风景等自然图片，CLIP 的图文匹配效果通常会更明显。

## 遇到的问题与解决方法

问题 1：PyTorch DLL 被 Windows 拦截
运行项目时出现：
OSError: [WinError 4551] 应用程序控制策略已阻止此文件。
Error loading "...torch_global_deps.dll"
原因：
Windows 应用程序控制策略阻止了 PyTorch 的 DLL 文件加载。
解决方法：
重新创建一个新的虚拟环境，并安装 CPU 版 PyTorch：
cd D:\ai-engineering
python -m venv .venv-multimodal
.\.venv-multimodal\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
python -m pip install pillow transformers

问题 2：旧虚拟环境无法删除
删除旧环境时出现：
Remove-Item : 无法删除项 D:\ai-engineering\.venv\Scripts\python.exe: 对路径“python.exe”的访问被拒绝。
原因：
旧虚拟环境里的 python.exe 正在被占用，可能是 VS Code、终端、Jupyter 或其他 Python 进程还在使用它。
解决方法：
不继续使用旧 .venv，改用新的环境名：
python -m venv .venv-multimodal
如果需要强制删除旧环境，可以先关闭 VS Code 终端，或者执行：
Get-Process python
Stop-Process -Name python -Force
Remove-Item -Recurse -Force D:\ai-engineering\.venv

问题 3：pip.exe 被应用程序控制策略阻止
安装依赖时出现：
程序“pip.exe”无法运行: 应用程序控制策略已阻止此文件。
原因：
Windows 策略拦截了虚拟环境中的 pip.exe。
解决方法：
不要直接使用：
pip install ...
改用：
python -m pip install ...
例如：
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
python -m pip install pillow transformers

问题 4：激活了新环境，却仍然调用旧 Python
错误命令：
& d:\ai-engineering\.venv\Scripts\python.exe d:/ai-engineering/ai-engineering-from-scratch/my-projects/multimodal-image-text-demo/main.py
这个命令会调用旧环境 .venv，不是新环境 .venv-multimodal。
如果旧环境里没有安装 torch，就会出现：
ModuleNotFoundError: No module named 'torch'
正确做法：
激活新环境后，只运行：
python main.py
也可以检查当前 Python 路径：
python -c "import sys; print(sys.executable)"
正确结果应该类似：
D:\ai-engineering\.venv-multimodal\Scripts\python.exe

## 我学到了什么

通过这个项目，我理解了：
多模态 AI 可以同时处理图片和文本
图片和文本都可以被编码成向量
CLIP 可以把图片和文本映射到同一个语义空间
图文匹配的本质是计算图片向量和文本向量的相似度
CLIP 适合自然图像和自然语言描述匹配
CLIP 不是专门的手写数字分类模型
同一个 demo 跑通并不代表模型一定会预测正确
Windows 环境下运行 PyTorch 时，可能会遇到 DLL 或 pip 被系统策略阻止的问题
使用 python -m pip 比直接使用 pip 更稳定
激活虚拟环境后，应该直接使用 python main.py，不要再手动调用旧 Python 路径
项目意义
这个 demo 是多模态 AI 的最小实践项目。
它虽然很简单，但已经包含了真实多模态系统的核心流程：
图片输入
  -> 图片编码
  -> 文本输入
  -> 文本编码
  -> 相似度计算
  -> 输出最匹配结果

## 后续可以基于这个项目继续扩展：

图片搜索系统
本地图片分类工具
图文检索 demo
多模态问答系统
简单视觉 Agent