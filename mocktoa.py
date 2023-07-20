import json
import os
import numpy as np
from datetime import datetime
import random
import time
import regex as re


class Mocktoa:

    mockdata_json = None
    schemas=None
    fake = None

    def __init__(self):
        self.json_file=open("mockdata.json","r")
        self.mockdata_json=json.load(self.json_file)
        self.schemas=self.mockdata_json["schemas"]
        self.fake=self.mockdata_json["fake"]

    def get_keys(self):
        return self.fake.keys()

    def get_data_from_type(self,type,typeOs):
        data=None
        classes=[x["typeOs"] for x in self.fake[type]["classes"]]

        if typeOs in [x["typeOs"] for x in self.fake[type]["classes"]]:
            index_classe = classes.index(typeOs)
            schema=[x["mockSchema"] for x in self.fake[type]["classes"]][index_classe]
            print("Récupération d'une fake data")
            data = self.getDataFromJson(schema)
        return data

    def getDataFromJson(self,schema):
        data = None
        
        if self.schemas == None or schema == None or not isinstance(schema,str) or schema == "":
            return data
        
        if schema not in self.schemas:
            return data

        schema_setup_list=self.schemas[schema]
        if not isinstance(schema_setup_list,list):
            return data
        
        data = {}
        field_values = {}

        for index in range(len(schema_setup_list)):
            schema_setup=schema_setup_list[index]
            field=schema_setup["field"] if "field" in schema_setup else None
            type=schema_setup["type"] if "type" in schema_setup else "template"
            value=schema_setup["value"] if "value" in schema_setup else ""
            minNumber=schema_setup["min"] if "min" in schema_setup else 0
            maxNumber=schema_setup["max"] if "max" in schema_setup else 1
            weights=schema_setup["weights"] if "weights" in schema_setup else None

            if field == None:
                return None
            
            if type == "list":
                nb_values = len(value)
                p=None
                if weights != None and isinstance(weights,list):
                    nb_weights=len(weights)
                    sum_weights= np.sum(weights)
                    p=[]
                    if nb_weights == nb_values:
                        for weight in weights:
                            p.append(weight/sum_weights)
                value = np.random.choice(value,p=p)

            if type == "number":
                value = random.randrange(minNumber,maxNumber)

            if type == "template":
                tokens_word=re.findall(r"{([^\}.]*)}",value)
                if tokens_word !=None and isinstance(tokens_word,list):
                    for token_word in tokens_word:
                        if token_word in data:
                            v=data[token_word]
                            if isinstance(v,int):
                                v=str(v)
                            value=value.replace("{"+token_word+"}",v)

            data[field]  = value
            

        return data
