import requests
from bs4 import BeautifulSoup

class Acura:
    def __init__(self, cars) -> None:
        self.cars = cars
    
    def scrape_func(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        car_models_list = soup.find_all("div", {"class" : "acr-current-model-card__text"})
        
        for car_model in car_models_list:
            temp_car_model_details_list = car_model.text.strip().split(" ")
            temp_car_model_details_list.remove("\nBUILD")         

            model_key = " ".join(temp_car_model_details_list[:-4])
            self.cars[model_key] = {}
            self.cars[model_key]["price"] = temp_car_model_details_list[-1]
            self.cars[model_key]["type"] = temp_car_model_details_list[-4]
            self.cars[model_key]["year"] = "2024"
        
        return self.cars