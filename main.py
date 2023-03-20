# import the importlib module
import importlib

# specify the name of the module to be imported (this could be modified)
module_name = "example_module"

# dynamically import the module using importlib 
my_module = importlib.import_module(module_name)


name = config["name"]
print(f"Hello,  {name}")
