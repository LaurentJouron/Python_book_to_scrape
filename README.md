<h1 align="center">Welcome to readme scraping 👋</h1>
<p align="center">
  <a href="https://twitter.com/LaurentJouron">
    <img alt="Twitter: LaurentJouron"
      src="https://img.shields.io/twitter/follow/LaurentJouron.svg?style=social" target="_blank" />
  </a>   
  <a href="https://github.com/LaurentJouron">
    <img alt="GitHub followers" 
      src="https://img.shields.io/github/followers/LaurentJouron?style=social" />
  </a>
</p>

___

You are a marketing analyst at Books Online, a major online bookstore specializing in used books. As part of your job, 
you try to manually track the prices of used books on your competitors' websites, but that’s too much work, and you can’t
cope with it: there are too many books and too many online bookstores ! You and your team decided to automate this
laborious task via a program (a scraper) developed in Python, able to extract price information
from other online libraries.

___________
<h1 align="center">Books Online</h1>

*In order to better manage the company in which I work, I created a scraping application on the website
Book-toScrape.com. Scraping is a method of extracting data to analyze information.*

https://books.toscrape.com/

___________
<h1 align="center">Purpose of the application</h1>

<p align="center">
    <img align="right"
      width="300px" 
      src="https://www.e-bdd.com/images/scraping-web.webp" />
</p>

* Initially this software will take:
  * the names of the categories
  * category links.
 
* Then according to the links of the Categories, it will load :
  * the titles of the books
  * the links of the books
  * the covers of books

<p align="center">
    <img align="right"
      width="300px"
      src="https://www.okvoyage.com/wp-content/uploads/2021/01/bibliotheque-nationale-finlande-1024x683.jpeg" />
</p>

* Finally, he will retrieve the information from the books :

  * UPC (universal_product_code)
  * product_type
  * price_excl_tax
  * price_incl_tax
  * tax
  * available_in_stock
  * number_of_review
  * synopsis

___________
<h1 align="center">Library</h1>

We used 4 different libraries for this project, here are the explanatory documents:

<table>
  <tr>
    <td align="center">
      <a href="https://docs.python-requests.org/en/latest">
        <img width="130px"
          src="https://docs.python-requests.org/en/latest/_static/requests-sidebar.png" /><br />
        <sub><b>Requets</b></sub></a><br />
      <a href="https://docs.python-requests.org/en/latest" title="Documentation Requests" ></a>
    </td>
    <td align="center">
      <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">
        <img width="130px"
          src="https://www.crummy.com/software/BeautifulSoup/bs4/doc/_images/6.1.jpg" /><br />
        <sub><b>BeautifulSoup</b></sub></a><br />
      <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" title="Documentation BeautifulSoup" ></a>
    </td>
    <td align="center">
      <a href="https://docs.python.org/fr/3/library/csv.html">
        <img width="150px"
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeFQCFFmRX7dsxcyLmKNYn9Umgdg71FDMsZQ&usqp=CAU" /><br />
        <sub><b>csv</b></sub></a><br />
      <a href="https://docs.python.org/fr/3/library/csv.html" title="Documentation csv" ></a> 
    </td>
    <td align="center">
      <a href="https://docs.python.org/3/library/os.html">
        <img width="150px"
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGeVC6EubMa9PBsn1aoXsbCmGEVENRpb9wlg&usqp=CAU" /><br />
        <sub><b>os</b></sub></a><br />
      <a href="https://docs.python.org/3/library/os.html" title="Documentation csv" ></a> 
    </td>
  </tr>
</table>

___________
<h1 align="center">Installation and use</h1>

* To start you must clone the project with the following url :
  * ``git clone https://github.com/LaurentJouron/Python_scraping_book_to_scrape.com.git``

* There is no virtual environment, so you must create it with the command :
  * ``cd Python_scraping_book_to_scrape``
  * ``mkdir .venv``
  * ``pipenv install``

* Enable this environment, with the command : 
  * ``pipenv shell``

* To start the program type this line in your terminal :
  * ``python scraping``

As the process progresses, we note the writing of .csv files that allow the analysis of the information of the books .

<p align="center">
    <img align="center" 
      width="350px" 
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRCQnMkK3eTUga21tSq4dsh6xBfffxX5YWVg&usqp=CAU" />
</p>

___________
<h1 align="center">Author and collaborators</h1>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LaurentJouron">
        <img width="100px"
          src="https://github.com/LaurentJouron/LaurentJouron.github.io/blob/main/ressources/img/logo/ikigai.png" /><br />
        <sub><b>Laurent Jouron</b></sub></a><br />
      <a href="https://github.com/LaurentJouron/Python_scrape_book_to_scrape" title="Application Coder">💻</a>
    </td>
  </tr>
</table>
