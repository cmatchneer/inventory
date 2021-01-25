# inventory
Hello my name is Christoper welcome to my inventory app created with Django framework using bootstrap for stylingl. The login uses built-in Django as does the database. This app was my real attempt to make anything using Django. The only part of the page that can be accessed without being logged is the home page. Everything else would require the user to login. Once logged in the user can hit the product link to see all the products that are on the database. From that page they either update the information or delete the product off the database. Hitting update takes them to a form page that they can then make the changes hit submit and head back to see the changes that have gone into the database. Hitting the delete button will take them to the page to make sure they wish to delete the item. Hitting either button will bring the user back to the product page. If the user wishes to add a new product to the database all they need to do is hit the link go to that page and fill out the form and once submitted they can go back to the product page to see the new product has been added.

The hardest part for me was wrapping my head around how views work and what they do. That is still my biggest weakness when it comes to this framework. I understand the basics but that is about it for now. Using for loops and if statements in the HTML was the easiest thing to pick up for me along with passing HTML between pages. That was a lot like react and translated very quickly once I understood the syntax for it. I was unsure of how to add Javascript to this project. I had a lot of issues getting my static css to connect. I didn't feel comfortable trying to add Javascript and connecting it as well.  

Being my first real attempt at Django there was a lot of functionality I could not add that with more knowledge I would have liked to add. Such as tracking which user last updated the database, tracking the expiration dates and creating warnings based on how close to the current date it was one for low quantities as well, breaking up products into departments allowing searches based on department for larger scale stores. Different levels for the users such as manager and employee with different levels of access to the system. Making it so the user can update or delete the product right on the product page instead of going to another page to do that. 

admin login: username = admin password =admin1
user login: username = test@test.com password=tester101

I used Django docs and lots of googling and looking at stackoverflow to help me solve a lot of issues. I also used a few other sources as well

Youtube video that taught me the basics and helped me build the products app and its accompanying github 
YouTube video: https://www.youtube.com/watch?v=F5mRW0jo-U4&t=1826s
Github: https://github.com/codingforentrepreneurs/Try-Django
A source that helped me create the login: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication





