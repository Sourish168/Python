import requests
from transformers import pipeline

def meal_id(data):
    return data["data"]["idMeal"]

def meal_name(data):
    return data["data"]["strMeal"]

def meal_area(data):
    if data["data"]["strArea"]==("" or " "):
        return "Meal area not found..."
    else:
        return data["data"]["strArea"]
    
def meal_category(data):
    if data["data"]["strCategory"]==("" or " "):
        return "Meal category not found..."
    else:
        return data["data"]["strCategory"]

def meal_ingredient(data):
    ingredients_list = []

    for i in range(1, 31):
        ingredient = data["data"].get(f'strIngredient{i}', '').strip()
        measure = data["data"].get(f'strMeasure{i}', '').strip()

        if ingredient:
            if not measure:
                measure = "According to your taste"
            ingredients_list.append([ingredient, measure])

    return ingredients_list

def meal_recipe(data):
    return data["data"]["strInstructions"]

def update_the_meal(data):
    generator = pipeline("text2text-generation",
                        model="google/gemma-2b-it",
                        device_map="auto")
    m_id = meal_id(data)
    m_name = meal_name(data)
    m_area = meal_area(data) if meal_area != "Meal area not found..." else ""
    m_category = meal_category(data) if meal_category(data) != "Meal category not found..." else ""
    ingredients_list = meal_ingredient(data)
    m_ingridents = ""
    for item in ingredients_list:
        m_ingridents += f"{item[0]}: {item[1]}"
    m_recipe = meal_recipe(data)

    data_organised = f"""
    Meal Name: {m_name}\n
    Meal Area: {m_area}\n
    Meal Category: {m_category}\n
    Meal Ingredients:\n{m_ingridents}\n
    Meal Recipe:\n{m_recipe}
    """

    desired_type = str(input("Please write your desired style of cuisine: "))

    prompt = f"""
    Suppose you are a master-chef and you understand all the cuisines in the world. Even you can prepare all kind of recipes with any combination of ingredients available in your hand. You have a special ability to make different cuisine's food in another different cuisine with proper accuracy of quality and flavour of the latter cuisine in the former cuisine. Now, please make the below mentioned meal preparation method in {desired_type} style cuisine. Hope you can defend your master-chef title. And please maintain the same format as mentioned in the former style of cuisine.
    """

    input_text = prompt + "\n" + data_organised

    print("Updating the meal... Please wait for a moment!!")
    output = generator(input_text, max_length=200, do_sample=True)[0]['generated_text']

    updated_meal = f"{m_id} (Updated)\n{output}"

    return updated_meal

def fetch_ramdom_meal_data(choice, data):
    
    if data["success"] and "data" in data:
        # print("\n")
        match choice:
            case "0":
                print(meal_id(data))
            case "1":
                print(meal_name(data))
            case "2":
                print(meal_area(data))
            case "3":
                print(meal_category(data))
            case "4":
                ingredients_list = meal_ingredient(data)
                print("<: This is your ingredient list :>")
                for item in ingredients_list:
                    print(f"{item[0]}: {item[1]}")
            case "5":
                print("<: This is your recipe :>")
                print(meal_recipe(data))
            case "6":
                print(update_the_meal(data))
            case _:
                print("Invalid Choice!!! Please Give The Valid Number...")
    else:
        raise Exception("Failed to fetch meal data")

def fetching_random_meal():
    try:
        url = "https://api.freeapi.app/api/v1/public/meals/meal/random"
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(str(e))

def main():
    try:
        data = fetching_random_meal()
        # print(data)
        print("Random meal fetched...")
        while True:
            print("\nRandom Meal Selector | Operations")
            print("0. Meal ID")
            print("1. Meal Name")
            print("2. Meal Area")
            print("3. Meal Category")
            print("4. Meal Ingredients")
            print("5. Meal Recipe Methods")
            print("6. Update The Meal Based On Your Region")
            print("7. Stop The Process")

            choice = input("Write your favorite choice: ")
            match choice:
                case "7":
                    break
                case _:
                    fetch_ramdom_meal_data(choice, data)
            
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()
