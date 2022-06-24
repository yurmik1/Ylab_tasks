def domain_name(url):
    if "//" in url:
        url = url.split('//')
        url = url[1]
    url = url.split('.')
    if 'www' in url:
        url = url[1]
    else:
        url = url[0]
    return url

