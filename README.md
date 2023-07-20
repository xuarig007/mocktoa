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
