# import requests

# # URL of the webpage you want to retrieve
# url = 'https://www.toptal.com/'

# try:
#     # Make the GET request
#     response = requests.get(url)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Save the HTML content to index.html
#         with open('index.html', 'w', encoding='utf-8') as file:
#             file.write(response.text)
#         print('HTML content saved to index.html')
#     else:
#         print(f'Error {response.status_code}: {response.text}')

# except requests.exceptions.RequestException as e:
#     print(f'Request failed: {e}')

import requests

# URL of the webpage you want to retrieve
url = 'https://www.bbc.com/'

try:
    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful
    response.raise_for_status()  # Raises an error for HTTP error codes

    # Save the HTML content to index.html
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print('HTML content saved to index.html')

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Specific error for HTTP errors
except requests.exceptions.RequestException as req_err:
    print(f'Request failed: {req_err}')  # General request error
