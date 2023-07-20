# mocktoa
Mocktoa is a very light project to generate mock data from setup jon file 

Ce projet a été créé pour répondre à un problème de création de données "fake" pour des outils d'infrastructure comme influxdb pour générer régulièrement des données autour des serveurs et services dans les datacenters des clients

Ce projet est sans prétention. Il permet grace à un fichier json de créer à partie de modème des fake data.

Exemple1 : nous devons générer des lignes de saturation des filesystèmes pour les serveurs linux , sur les filesystems /tmp (4 fois sur 5) ou /var (1 fois sur 5), avec des seuils de saturation entre 80% et 100%. 
Le texte de sortie sera par exemple : **Filesystem /tmp is 98% full**

Fichier mocktoa.json :
```json
{
    "schemas" : { 
        "event_filesystem_linux" : [
            { "field" : "type", "type" : "template", "value" : "filesystem"},
            { "field" : "value", "type" : "list", "value" : ["/tmp","/var"], "weights" : [ 4, 1 ] },
            { "field" : "percentage", "type" : "number", "min" : 80, "max" : 100 },
            { "field" : "text", "type" : "template", "value" : "Filesystem {value} is {percentage}% full"}
        ]
    },
    "fake": {
        "filesystem" : {
            "choice" : 1.0,
            "classes" : [
                {
                    "typeOs" : "Linux Server",
                    "mockSchema" : "event_filesystem_linux"
                }
            ]
        }
    }
}
```

Exemple de script python pour générer un fake

``` python
import mocktoa

print("1) New instance of Mocktoa => mt = mocktoa.Mocktoa()\n")
# mocktoa instance
mt = mocktoa.Mocktoa()

# types list available
print(f"2) Available types => list(mt.get_keys()) => { list(mt.get_keys()) }\n")

# random type data
type_data = mt.get_random_type()
print(f"3) Random type_data => type_data = mt.get_random_type() => \"{type_data}\"\n")

# get random data for type data and operating system type
typeOs="Linux Server"
data=mt.get_data_from_type(type_data,typeOs)

print(f"4) Get data for {typeOs} =>  data=mt.get_data_from_type(type_data,typeOs) => { data }\n") 
```
![image](https://github.com/xuarig007/mocktoa/assets/35503724/67b71660-6fdf-4e3e-befd-470ac1f54d87)
