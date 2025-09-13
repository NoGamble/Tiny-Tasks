# ONNX (Open Neural Network Exchange)

## 🧠 定义

**ONNX** (**O**pen **N**eural **N**etwork **E**xchange) 是一个开放的**模型表示标准**，用于在不同的深度学习框架和硬件平台之间实现模型的**互操作性与交换**。

## 🎯 核心目标

其核心目标是**解耦模型的训练与部署**，让开发者能够：
- **使用任何框架进行训练** (如 PyTorch, TensorFlow)
- **在任何环境中进行部署** (如云端、边缘设备、移动端)

## 🔧 核心价值：解决碎片化问题

在 ONNX 出现之前，AI 生态是割裂的：

| 训练框架 (Training) | 推理引擎/硬件 (Inference) | 问题 |
| :--- | :--- | :--- |
| PyTorch | NVIDIA TensorRT | **格式不兼容** |
| TensorFlow | Intel OpenVINO | 需要复杂的模型转换 |
| PaddlePaddle | Apple Core ML | 无法发挥硬件极致性能 |
| MXNet | Android NNAPI | 部署流程冗长 |

**ONNX 作为通用的“中间语言”**，完美地解决了这个问题。

## 📊 工作原理与流程

其典型工作流如下所示，展示了模型从训练到部署的完整过程：
### 1. 训练 (Training)
- 使用原生框架（PyTorch等）训练模型

### 2. 转换 (Conversion)
- 通过各框架导出工具转换为`.onnx`文件
- to be updated...

### 3. 优化 (Optimization)
- **图优化**：常量折叠、算子融合
- **量化**：FP32 → INT8（减小体积、加速）
- **验证**：格式与兼容性检查

### 4. 部署 (Deployment)
**跨平台推理运行时**：
- ONNX Runtime（官方跨平台）
- NVIDIA TensorRT (GPU)
- Intel OpenVINO (Intel硬件)
- 移动端：Core ML / NNAPI

### 5. 推理 (Inference)
- 应用程序加载ONNX模型
- 输入数据 → 获取结果

## ✨ 优势
- **互操作性**：打破框架壁垒
- **硬件支持**：一份模型，多处部署
- **高效优化**：统一优化接口
- **简化流程**：降低部署复杂度