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
