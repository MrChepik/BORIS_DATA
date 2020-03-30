#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import os
from pprint import pprint

#Create a SpeechToText adapter object, where need to add APIkey and "URL" to API endpoint, which is can be obtained from
#IBM_watson_studio from API credentional manage

authenticator = IAMAuthenticator('wGVXi0TCEItoJ2kuJBj_nEos6Gp1FARt0SJ9vAxydTue') #API key
s2t = SpeechToTextV1(authenticator = authenticator)
s2t.set_service_url = ('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/70078570-120d-4600-b588-a821559af6cb') #url to API endpoint, which can be obtained from API credentials
#print(s2t)

#os.system('wget -O PolynomialRegressionandPipelines.mp3  https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3)  #Download .mp3 file, can be added locally

filename = '/home/boris/git-repos/My_projects/PolynomialRegressionandPipelines.mp3'

with open(filename, mode = 'rb') as wav:
	out_text = s2t.recognize(audio = wav, content_type = 'audio/mp3')


out_text.result
#pprint(out_text.result)

print(json_normalize(out_text.result['results'], 'alternatives'))

recognized_text = out_text.result['results'][1]['alternatives'][0]['transcript'] #in case, that original output is dictionare, we can obtain part of the text by key and value

print(recognized_text)




