import requests

def fetch_ramdom_meal():
    url = "https://api.freeapi.app/api/v1/public/meals/meal/random"
    response = requests.get(url)
    data = response.json()
    # print(response)
    # print(data)


def main():
    try:
        # fetch_ramdom_meal()
        while True:
            print("\nRandom Meal Selector | Operations")
            print("1. Recipe Name")
            print("2. Recipe Ingredients")
            print("3. Recipe Methods")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()
