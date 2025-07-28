import requests

def fetch_ramdom_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    # print(response)
    # print(data)

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        user_location = user_data["location"]["country"]
        return username, user_location
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        user_name, country = fetch_ramdom_user()
        print(f"Username: {user_name} \nUser Country: {country}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()
