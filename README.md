# PyTorch Image Classifier

Transfer learning and fine-tuning image classification models with PyTorch.

## Features
- ResNet, EfficientNet, Vision Transformer support
- Custom dataset loading with albumentations
- Mixed precision training (AMP)
- Weights & Biases integration
- Model export to ONNX/TorchScript

## Quick Start
```bash
pip install -r requirements.txt
python train.py --model resnet50 --data ./data --epochs 100
```

## License
MIT