# mocktoa
Mocktoa is a very light project to generate mock data from setup jon file 

This project was created to address a problem of creating "fake" data for infrastructure tools like influxdb to regularly generate data around servers and services in customer datacenters.

This project is unpretentious. It uses a json file to create fake data from a model.

Example: we need to generate filesystem saturation lines for Linux servers, on /tmp (4 times out of 5) or /var (1 time out of 5) filesystems, with saturation thresholds between 80% and 100%. 

**The output text will be, for example: Filesystem /tmp is 98% full**

File mocktoa.json :
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

Example of a python script to generate a fake

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
