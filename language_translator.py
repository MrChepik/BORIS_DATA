#!/usr/bin/env python3
#/-*-coding:utf-8-*-

from ibm_watson import LanguageTranslatorV3
from pandas.io.json import json_normalize

#url_lt='https://api.us-south.speech-to-text.watson.cloud.ibm.com'
#apikey_lt='Xp6fmWNm13Q-teNKZVH734hfbxCmCjjV5wO9p0n_NsAH'


version_lt='2018-05-01'

authenticator = IAMAuthenticator('GKgdl64euHP6R-sy8ApkgIIWWjf_ERrdjAIYP_ZlfHJU')
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/6ce7d11b-fdbe-425f-950e-5caee4925929')
language_translator

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

translation_response_1 = language_translator.translate(\
    text=recognized_text, model_id='en-ru')
translation_response_1

russian_translation =translation['translations'][0]['translation']
russian_translation 

translation_new = language_translator.translate(text=russian_translation ,model_id='ru-en').get_result()

translation_eng=translation_new['translations'][0]['translation']
translation_eng


