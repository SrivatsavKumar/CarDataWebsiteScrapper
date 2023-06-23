import requests
from bs4 import BeautifulSoup

class Mercedes:
    def __init__(self, cars) -> None:
        self.cars = cars

    def scrape_func(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        car_models_list = soup.find_all("li", {"class":"all-vehicles__model"})

        for car_model in car_models_list:
            temp_car_model_details_list = car_model.text.strip().split(" ")
            temp_car_model_details_list.remove("")
            model_key = ""
            if temp_car_model_details_list[-1] == "Soon":
                model_key = " ".join(temp_car_model_details_list[:-4])
                self.cars[model_key] = {}
                self.cars[model_key]["type"] = temp_car_model_details_list[-4]
                self.cars[model_key]["price"] = "Price Coming Soon"
                self.cars[model_key]["year"] = ""
            else:
                model_key = " ".join(temp_car_model_details_list[:-2])
                self.cars[model_key] = {}
                self.cars[model_key]["type"] = temp_car_model_details_list[-2]
                self.cars[model_key]["price"] = temp_car_model_details_list[-1]
                self.cars[model_key]["year"] = ""
        return self.cars
