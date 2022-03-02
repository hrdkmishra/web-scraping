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
            scrape_data.append(f'{course_card} costs {course_price}')
        return scrape_data
    print("\nPrinting scraped data ... \n")
    for data in scrape() :
        print(data)
    save = input("\nDo you want to save the output ? (y or n) : ")
    if save == 'y' or save == 'Y' :
        with open('output.txt', 'w') as file :
            for data in scrape() :
                file.write(data + '\n')
        print("Saved as 'output.txt'\n")
    else :
        print("\nQuitting ... \n")
        exit