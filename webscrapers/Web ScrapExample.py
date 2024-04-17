import requests
from bs4 import BeautifulSoup

url="https://realpython.github.io/fake-jobs/"
page = requests.get(url)

#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
#print(results.prettify())

# .find_all grabs content and returns an iterable containing all the HTML for all the content on the page
job_elements = results.find_all("div",class_="card-content") # all the job listings are wrapped behind the div element with the class element

# print all the elements
for job_element in job_elements:
    title_element = job_element.find("h2",class_="title") # divide the job listings in separate features based on heading, paragraph HTML format
    company_element = job_element.find("h3",class_="company") # heading 3 <h3> = company
    location_element = job_element.find("p",class_="location") # paragraph or <p> = location
    print(title_element.text.strip) # print the element and strip the whitespace
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
print("\n-----")
# find all python jobs specifically
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
    ) # use string argument to filter for keywords
print(python_jobs)
for python_job in python_jobs:
    print(python_job.text.strip()) # clean the list, make it easier to read
    
print(len(python_jobs))
print("\n------")
# Now, create a list of all the python job listings with all relevant info
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs 
] # assigns the elements from the great-grandparent container with the div directly containing h2 (python job title) as the parent into a list

# Print all the jobs with all the relevant features 
for python_job_element in python_job_elements:
    title_element = python_job_element.find("h2",class_="title")
    company_element = python_job_element.find("h3",class_="company")
    location_element= python_job_element.find("p",class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    
    link_url = python_job_element.find_all("a")[0]["href"] # .find_all(key, index, attribute)
    print(f"Apply here: {link_url}\n") # we grabbed text under <a> </a> and picked the second index, and included the hyper link attribute

## Does the same thing, except grabs both links
#    links = python_job_element.find_all("a")
#    for link in links:
#        link_url = link["href"]
#        print(f"Apply here: {link_url}\n")
        