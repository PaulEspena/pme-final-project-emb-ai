import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    if response.status_code == 200:
        try:
            formatted_response = response.json()  # requests has built-in json() method
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            
            emotion_dict = {
                'anger': emotions['anger'],
                'disgust': emotions['disgust'],
                'fear': emotions['fear'],
                'joy': emotions['joy'],
                'sadness': emotions['sadness']
            }
            
            dominant_emotion = max(emotion_dict, key=emotion_dict.get)
            emotion_dict['dominant_emotion'] = dominant_emotion
            
            return emotion_dict
        except (json.JSONDecodeError, KeyError, IndexError) as e:
            print(f"Error parsing response JSON or missing keys: {e}")
            return None
    else:
        print(f"Request failed with status code {response.status_code}")
        print(f"Response text: {response.text}")
        return None 