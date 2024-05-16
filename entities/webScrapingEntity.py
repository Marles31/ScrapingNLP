import requests
from bs4 import BeautifulSoup


class webScrappingEntity:

    def HomeResponse(self):

        porsche_list = []
        url = "https://www.porsche.com/latin-america-es/"
        page = requests.get(url)
        soap = BeautifulSoup(page.content, 'html.parser')
        porsche_elements = soap.find_all("a", class_="m-102-slider__item")

        for porsche_element in porsche_elements:
            title_element = porsche_element.find("span").text.strip()
            title_element = title_element.replace("Encuentre ", "").capitalize()
            image_element = porsche_element.find("img")["data-image-src"]

            porsche_info = {
                "Title": title_element,
                "Image": image_element
            }
            porsche_list.append(porsche_info)

        return porsche_list

    def classResponse(self):

        jobs_list = []
        url = "https://realpython.github.io/fake-jobs/"
        page = requests.get(url)
        soap = BeautifulSoup(page.content, 'html.parser')
        results = soap.find(id="ResultsContainer")
        jobs_elements = results.find_all("div", class_="card-content")

        for jobs_element in jobs_elements:
            title_element = jobs_element.find("h2", class_="title")
            company_element = jobs_element.find("h3", class_="company")
            location_element = jobs_element.find("p", class_="location")

            jobs_info = {
                "Title": title_element.text.strip(),
                "Company": company_element.text.strip(),
                "Location": location_element.text.strip()
            }
            jobs_list.append(jobs_info)

        return jobs_list