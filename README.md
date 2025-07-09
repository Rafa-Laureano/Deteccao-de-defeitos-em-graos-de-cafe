# Detecção de defeitos em amostras de grão de café

Este repositório contém os códigos, modelos treinados e scripts utilizados para o desenvolvimento de um sistema inteligente de classificação de defeitos em grãos de café, integrando técnicas de visão computacional, modelos de detecção de objetos e um aplicativo móvel embarcado com suporte a TensorFlow Lite.

## 🧠 Objetivo

Desenvolver uma solução automatizada capaz de identificar e contar defeitos em grãos de café por meio de imagens capturadas em dispositivos móveis, com foco em acessibilidade para pequenos produtores e cooperativas. A detecção é realizada localmente no celular, com alta precisão e baixo tempo de inferência.

## 🔍 Principais Funcionalidades

- Treinamento de modelos YOLOv8n, YOLO11n, YOLO12n com dataset personalizado
- Comparação com modelos SSD MobileNetV2 e FPNLite (quantizados e não quantizados)
- Conversão de modelos para o formato `.tflite` para uso em Android
- Integração do modelo YOLO11n em um aplicativo móvel 

## 📊 Dataset

O dataset contém mosaicos de **36 grãos por imagem**, com 8 classes principais de defeitos:
- `Broken`
- `Dry Cherry`
- `Full Black`
- `Fungus Damage`
- `Healthy`
- `Husk`
- `Parchment`
- `Severe Insect Damage`

> Disponível publicamente via Roboflow: [beans_mosaic dataset](https://app.roboflow.com/instituto-nacional-de-telecomunicaes/beans_mosaic/12)

## 📲 Aplicativo Android


> Baseado em: [pub-yolo-android](https://github.com/estebanuri/pub-yolo-android)



