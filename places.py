import placesResults as rs, pprint

def main():
    searchFor = input("iHello: ")
    results = rs.placesResults(searchFor)
    for result in results:
        title = result[0]
        url = result[1]
        print(f"{title}, {url}\n")

if __name__ == '__main__':
    main()
    