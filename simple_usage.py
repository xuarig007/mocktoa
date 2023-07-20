import mocktoa

# mocktoa instance 
mt = mocktoa.Mocktoa()

# types list available
print(f"Available types : { mt.get_keys() }")

# random type data
type_data = mt.get_random_type()
print(f"type_data = {type_data}")

# get random data for type data and operating system type
typeOs="Linux Server"
data=mt.get_data_from_type(type_data,typeOs)

print("Data = { data }") 
