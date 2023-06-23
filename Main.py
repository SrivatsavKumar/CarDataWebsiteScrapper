import Mercedes
import BMW
import Chevrolet

class Main:
    #Get class dynamically for each name in car_websites
    def get_class_by_module_name(module_name):
        module = __import__(module_name)

        class_obj = None
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and attr.__module__ == module_name:
                class_obj = attr
                break
        return class_obj

    cars = {}

    car_websites = [
        {"name": Mercedes, "url": "https://www.mbusa.com/en/all-vehicles"},
        {"name": BMW, "url": "https://www.bmwusa.com/"},
        {"name": Chevrolet, "url": "https://www.chevrolet.com/"}
    ]

    for website in car_websites:
        module_name = website["name"].__name__
        obj = get_class_by_module_name(module_name)({})
        data = obj.scrape_func(website["url"])
        cars[module_name] = data
    
    print(cars)