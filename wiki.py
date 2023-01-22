import wikipedia

while True:
    page_title = input("Title: ")
    if page_title.strip() != "":
        print(wikipedia.search(page_title))
        print(wikipedia.suggest(page_title))
        print(wikipedia.summary(page_title))
    else:
        break
