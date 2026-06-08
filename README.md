# PyTorch Image Classifier

Image classification using PyTorch and pretrained ResNet models.

## Features
- Transfer learning with ResNet50
- Custom dataset support
- Data augmentation
- TensorBoard logging
- Model export to ONNX

## Training
```bash
python train.py --data ./data --epochs 50 --batch-size 32
```

## Results
- Accuracy: 94.5% on CIFAR-10
- Inference: ~15ms per image (GPU)

## License
MIT
