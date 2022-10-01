import requests
import json

def main():
    # run a GET request
    response = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
    print(response, response.reason)
    #print(response.content)
    #print(response.content[0])
    #print(response.text)
    print(response.json()[0])

    data_string = response.text
    entry_list = json.loads(data_string)
    print(entry_list[0])
    first_entry = entry_list[0]
    mass =first_entry['mass']
    print(mass)


if __name__ == '__main__':
    main()
