import requests

# http get requests

r = requests.get('https://httpbin.org/get')

print(r.status_code)

# helpful resourse of requests tutorial is https://www.edureka.co/blog/python-requests-tutorial/
# helpful resourse of requests tutorial is https://www.datacamp.com/community/tutorials/making-http-requests-in-python

# few notes

# you will have to pass stream=True in the request to get the raw response as per need
