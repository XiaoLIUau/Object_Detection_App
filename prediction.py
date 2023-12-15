import timm
import torch

from PIL import Image
from utilities import util_setup

# Setup for model labels
LALBES =util_setup()


def load_model():
    model = timm.create_model('tiny_vit_5m_224.dist_in22k', pretrained=True)
    model = model.eval()
    return model


def predict_frame(image, model_pipe):
    img = Image.fromarray(image)
    # get model specific transforms (normalization, resize)
    data_config = timm.data.resolve_model_data_config(model_pipe)
    transforms = timm.data.create_transform(**data_config, is_training=False)
    predictions = model_pipe(transforms(img).unsqueeze(0))  # unsqueeze single image into batch of 1
    values, indices = torch.topk(predictions.softmax(dim=1) * 100, k=5)
    labels = [{'label': LALBES[idx.item()], 'value': val.item()} for val, idx in zip(values[0], indices[0])]
    # return 'cat' if 'cat' in labels[0]['label'] else 'No Cat'
    return 'Cap' if 'cap' in labels[0]['label'] else 'No Cap'
    # return labels[0]['label']
