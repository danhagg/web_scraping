from bs4 import BeautifulSoup


# remove all attributes
def _remove_all_attrs(soup):
    for tag in soup.find_all(True):
        tag.attrs = {}
    return soup


# remove all attributes except some tags
def _remove_all_attrs_except(soup):
    whitelist = ['a', 'img']
    for tag in soup.find_all(True):
        if tag.name not in whitelist:
            tag.attrs = {}
    return soup


# remove all attributes except some tags(only saving ['href','src'] attr)
def _remove_all_attrs_except_saving(soup):
    whitelist = ['a', 'img']
    for tag in soup.find_all(True):
        if tag.name not in whitelist:
            tag.attrs = {}
        else:
            attrs = dict(tag.attrs)
            for attr in attrs:
                if attr not in ['src', 'href']:
                    del tag.attrs[attr]
