
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

menu = soup.find('h1', attrs={"class": "_aacl._aaco._aacu._aacx._aad7._aade"})
print(menu.prettify())

# html파일쓰기
f = open('megatodaymenu.html', 'w')
message = menu.prettify()
f.write(message)
f.close()