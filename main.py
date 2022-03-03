from bs4 import BeautifulSoup
with open('index.html' , 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_file= soup.find_all('div', class_='card')
    def scrape () :
        scrape_data = []
        for course in course_file:
            course_card = course.h5.text
            course_price = course.a.text.split()[-1]
            scrape_data.append({
                "course_card": course_card,
                "course_price": course_price
            })
        return scrape_data
    print("\nPrinting scraped data ... \n")
    for data in scrape() :
        print(f'{data["course_card"]} costs {data["course_price"]}')
    save = input("\nDo you want to save the output ? (y or n) : ")
    if save == 'y' or save == 'Y' :
        with open('output.csv', 'w') as file :
            file.write("Course Name\tPrice\n")
            for data in scrape() :
                file.write(f'{data["course_card"]}\t{data["course_price"]}' + '\n')
        print("Saved as 'output.csv'\n")
    else :
        print("\nQuitting ... \n")
        exit