import requests
import json



DATA_FILE = 'data.json'
API_TO_GET_DATA = "https://world.openfoodfacts.org/api/v0/product/737628064502.json"
API_TO_POST_DATA = "https://httpbin.org/post"



# To get data from API as JSON
def get_json_data():
    get_data = requests.get(API_TO_GET_DATA)
    print('\n Successfuly received data from API')
    return get_data.json()


def save_json_data_as_a_file(file_to_save, data_to_save):
    with open(file_to_save, 'w') as f:
        json.dump(data_to_save, f)
    
    print('\n Successfuly saved data as a local file named : '+ file_to_save)


def read_json_data_from_a_file(file_to_read):
    # Opening JSON file
    f = open(file_to_read,)
    data = json.load(f)

    print('\n Successfuly read data from a local file')
    return data


def post_data_to_api(data_to_post):
    post_response = requests.post(API_TO_POST_DATA, data = data_to_post)
    print('\n Successfuly initiated a POST request with the given data')
    return post_response




def main():

    ''' To get data from API and save it as a file '''
    data_to_save = get_json_data()
    save_json_data_as_a_file(DATA_FILE, data_to_save)


    ''' To read data from a file and to post it to api and get the response'''
    data_to_post = read_json_data_from_a_file(DATA_FILE)
    post_response = post_data_to_api(data_to_post)
    # Success response is of Status 200 OK
    print("\n POST_RESPONSE_STATUS : "+str(post_response))


if __name__ == "__main__":
    main()