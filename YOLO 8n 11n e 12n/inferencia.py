from ultralytics import YOLO
import os
import shutil

def inferir_e_salvar_dataset(model_path, pasta_imagens, pasta_saida):
    # Criar pastas do novo dataset
    pasta_images = os.path.join(pasta_saida, "images")
    pasta_labels = os.path.join(pasta_saida, "labels")
    os.makedirs(pasta_images, exist_ok=True)
    os.makedirs(pasta_labels, exist_ok=True)

    # Carregar modelo treinado
    model = YOLO(model_path)

    # Rodar inferência com salvar as detecções como .txt (formato YOLO)
    results = model.predict(source=pasta_imagens, save=True, save_txt=True, conf=0.4, imgsz=640)


    # Pegar a pasta onde as imagens com predições foram salvas
    pasta_predita = results[0].save_dir

    # Mover imagens e labels para o novo dataset organizado
    for arquivo in os.listdir(pasta_predita):
        origem = os.path.join(pasta_predita, arquivo)
        if arquivo.endswith('.jpg') or arquivo.endswith('.png'):
            shutil.copy(origem, os.path.join(pasta_images, arquivo))
        elif arquivo.endswith('.txt'):
            shutil.copy(origem, os.path.join(pasta_labels, arquivo))

    print(f"\n✅ Novo dataset salvo em: {pasta_saida}")
    print("Pronto para ser importado no Roboflow ou usado para novo treinamento.")

    metrics = model.val()
    print(metrics)


def main():
    # Caminho do modelo treinado
    model_path = "yolo_12n/yolo_12n/weights/best_saved_model/best_float32.tflite"

    # Imagens não rotuladas
    pasta_imagens = "beans_mosaic.v11-nova-versao.yolov11/test/images"

    # Novo dataset com predições convertidas
    pasta_saida = "novo_dataset"

    inferir_e_salvar_dataset(model_path, pasta_imagens, pasta_saida)



if __name__ == "__main__":
    main()
