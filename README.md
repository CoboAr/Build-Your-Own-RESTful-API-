# Build Your Own RESTful API

 Building a full REST API from scratch using Flask.

## Requirements
On the integrated terminal on Pycharm run:

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.


## How does it work?

### Testing API routes with Postman

One of the best tools to test APIs is [Postman](https://www.postman.com/downloads/)     
It allows the user to add key-value pairs for the request parameters and it will automatically format the URL. It will also allow the user to automatically create documentation for his API.    
Download Postman for free here: https://www.postman.com/downloads/    


Create a new collection called Cafe & Wifi and add all the existing routes to the collection.

<img width="301" alt="Screenshot 2024-01-11 at 11 16 50 AM" src="https://github.com/CoboAr/Build-Your-Own-RESTful-API-/assets/144629565/911dc162-797b-4d6d-91ff-fad8cfc1b9b7">


<ul>
  <li>
    HTTP GET - a Random Cafe </br>
  It creates a /random route that serves up a random cafe.
  <img width="1157" alt="Screenshot 2024-01-11 at 11 18 52 AM" src="https://github.com/CoboAr/Build-Your-Own-RESTful-API-/assets/144629565/ba54bc3e-49de-4f35-97c6-c6a08ab49394">
</li>

 <li>
    HTTP GET - All the Cafes </br>
    When a GET request is made to this /all route, the server should return all the cafes in your database as a JSON.         
    
https://github.com/CoboAr/Build-Your-Own-RESTful-API-/assets/144629565/56cd229f-c329-4928-ae71-62c53bbe7537

  </li>

<li>
    HTTP GET - Find a Cafe </br>
    It creates a /search route to search for cafes at a particular location.      
    
  https://github.com/CoboAr/Build-Your-Own-RESTful-API-/assets/144629565/ce37307e-193c-4a2a-874e-db0c6bc17ac0

  </li>

  <li>
    HTTP POST - A New Cafe </br>
    Adding a new cafe to the website.

https://github.com/CoboAr/Build-Your-Own-RESTful-API-/assets/144629565/f96c61d5-daba-4593-82f6-c40ca1bd5051

  </li>

  <li>
    HTTP PATCH - A Cafe's Coffee Price </br>
    Update the coffee_price field of the café and leave the rest of the cafe's data unchanged by using the cafe's id as a reference.


https://github.com/CoboAr/Build-Your-Own-RESTful-API-/assets/144629565/4acad1e8-0e01-4150-b080-40ef93732025

    
  </li>

   <li>
    HTTP DELETE - A Cafe that's Closed </br>
    Make a DELETE request to the server and update the database. Only users that have the correct api-key insterted into the url can successfully delete a café    
    

https://github.com/CoboAr/Build-Your-Own-RESTful-API-/assets/144629565/fa6aa2d7-e9af-457a-9f93-ffd19d794784


    
  </li>
  </ul>

  ## Build Documentation for this API

If we want other people to use our API, then we have to document how to use it. People can't see the code on our servers, so we have to tell them how to interact with our servers via the API constraints.  e.g. What are the routes, what are the required parameters etc.      

Postman generates the documentation automatically.   

<ol>
  <li>
     Make sure that you've made each of the requests and they work as you expect.
  </li>
  <li>
    Make sure all the requests are saved in the same collection e.g. My collection is called Cafe & wifi:
  </li>
  <li>
    Click on the three dots next to your collection name and go to "Publish Docs":
  </li>

  <li>
    Go through the steps to publish your documentation and this is what you should end up with:   
    <img width="1434" alt="Screenshot 2024-01-11 at 12 23 46 PM" src="https://github.com/CoboAr/Build-Your-Own-RESTful-API-/assets/144629565/597ef8d6-1092-4538-ac83-78d909615c22">

  URL for published documentation:   
  https://documenter.getpostman.com/view/28971881/2s9YsMAWsb
  </li>
</ol>

Enjoy! And please do let me know if you have any comments, constructive criticism, and/or bug reports.
## Author
## Arnold Cobo




