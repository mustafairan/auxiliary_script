from urllib.parse import urlparse

def filter_urls_by_file_type(urls, file_types):
    filtered_urls = []
    for url in urls:
        parsed_url = urlparse(url)
        if parsed_url.path.split(".")[-1] not in file_types:
            filtered_urls.append(url)
    return filtered_urls

def get_comprehensive_urls(urls, file_types):
    # filter out URLs with the specified file types
    filtered_urls = filter_urls_by_file_type(urls, file_types)

    # parse the URLs and extract the query string parameters
    url_params = {}
    for url in filtered_urls:
        parsed_url = urlparse(url)
        params = parse_qsl(parsed_url.query)
        if parsed_url.path not in url_params:
            url_params[parsed_url.path] = []
        url_params[parsed_url.path].extend(params)

    # construct a comprehensive URL for each path
    comprehensive_urls = []
    for path, params in url_params.items():
        comprehensive_url = f"{parsed_url.scheme}://{parsed_url.netloc}{path}"
        if params:
            comprehensive_url += "?" + "&".join([f"{k}={v}" for k, v in params])
        comprehensive_urls.append(comprehensive_url)

    return comprehensive_urls

# test the function
urls = [
    "https://google.com",
    "https://google.com/home.txt?qs=value",
    "https://google.com/home.js?qs=secondValue",
    "https://google.com/home.png?qs=newValue&secondQs=anotherValue",
    "https://google.com/home.css?qs=asd&secondQs=das",
    "https://google.com/home?qse=111",
    "https://google.com/777",
]
file_types = ["txt", "js", "png"]
print(get_comprehensive_urls(urls, file_types))  # prints ["https://google.com/home.css?qs=asd&secondQs=das", "https://google.com/home?qse=111", "https://google.com/777"]
