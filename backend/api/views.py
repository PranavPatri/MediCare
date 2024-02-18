from rest_framework.decorators import api_view
from django.http import JsonResponse
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import requests
import json

url = "https://api.perplexity.ai/chat/completions"


headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer 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"
}






class_names = ['Eczema','Warts Molluscum and other Viral Infections', 'Melanoma','Atopic Dermatitis','Basal Cell Carcinoma (BCC)','Melanocytic Nevi (NV)','Benign Keratosis-like Lesions (BKL)','Psoriasis pictures Lichen Planus and related diseases','Seborrheic Keratoses and other Benign Tumors','Tinea Ringworm Candidiasis and other Fungal Infections']


def load_my_model():
    model=load_model('skin.h5')
    return model


@api_view(["post"])
def predict_disease(request):
    model=load_my_model()
    uploaded_image = request.FILES.get('image')
    print(type(uploaded_image))
    if uploaded_image:
        with uploaded_image.open() as f:
            image = Image.open(f)
            size = (300, 300)
            image = ImageOps.fit(image, size, Image.LANCZOS)
            img = np.asarray(image)
            img_reshape = img[np.newaxis,...]
            prediction = model.predict(img_reshape)
            string = "Detected Disease : " + class_names[np.argmax(prediction)]
            return JsonResponse({'replay':string},status=200)
    return JsonResponse({'replay':"missing required data in the request body."},status=400)



@api_view(["post"])
def get_response_bot(request):
    data = json.loads(request.body.decode('utf-8'))
    messages = data.get("messages", None)
    
    if messages:
        payload = {
            "model": "mistral-7b-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": messages
                }
            ]
        }
        response = requests.post(url, json=payload, headers=headers)
        
        data_dict = json.loads(response.text)
        #.get("choices")[0]["message"]["content"]
        return JsonResponse({"replay":data_dict['choices'][0]['message']['content']},status=200)
        

    return JsonResponse({"replay":"missing required data in the request body."},status=400)

