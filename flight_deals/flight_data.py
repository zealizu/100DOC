class FlightData:
    def __init__(self, search_data):
        self.search_data = search_data
    
    def display_prices(self, sheet_data):
        self.sheet_data = sheet_data
        self.prices = {}
        for data in self.sheet_data:
            print(f"Getting Flights for {data["city"]}...")
            current = self.search_data[data["city"]]
            prices = []
            try:
                for i in current:
                    price = i["price"]["total"]
                    prices.append({
                        "price":float(price),
                        "depature_airport_code":i["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                        "arrival_airport_code":i["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                        "termianl": i["itineraries"][0]["segments"][0]["departure"]["terminal"],
                        "depature_date":str(i["itineraries"][0]["segments"][0]["departure"]["at"]).split("T")[0],
                        "depature_time": str(i["itineraries"][0]["segments"][0]["departure"]["at"]).split("T")[1],
                        "return_date":str(i["itineraries"][1]["segments"][0]["departure"]["at"]).split("T")[0]
                        })
                    print(f"{data["city"]} : {price}")
                self.prices[f"{data["city"]}"] = prices
            except:
                print(f"{data["city"]} : N/A")
        # print(self.prices)
        
    def find_cheapest_flight(self):
        self.cheap_prices = {}
        for data in self.sheet_data:
            city = data["city"]
            l_price = data["lowestPrice"]
            cheap_price = []
            for i in self.prices[f"{city}"]:
                if i["price"] < l_price:
                    cheap_price.append(i)
            self.cheap_prices[f"{city}"] = cheap_price
        
        return self.cheap_prices
            
                
                