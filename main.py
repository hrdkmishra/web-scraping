from bs4 import BeautifulSoup
with open('index.html' , 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_file= soup.find_all('div', class_='card')
    for course in course_file:
        course_card = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_card} costs {course_price}\n')