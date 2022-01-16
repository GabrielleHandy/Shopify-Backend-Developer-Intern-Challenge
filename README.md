# Shopify-Backend-Developer-Intern-Challenge
Shopify Backend Developer Intern Challenge - Summer 2022


Hello! Thank you for trying out my challenge submission!

I used Flask to run the webpage, MySQL and PostgreSQL for the database, bootstrap for simple styling, and javascript for responsive-ness.

I did all coding in VSCode

Here are the steps to use my program:

1) Clone this git repo into your work station

2) Move into that repo *it should be a folder in your work station*
ex. ~/filePath $ cd Awesome-Intern-Challenge/
~/filePath/Awesome-Intern-Challenge $

2) Activate the virtual env
ex. ~/filePath/Awesome-Intern-Challenge $ source env/bin/activate

3) Install requirements from requirements.txt

ex. (env) ~/filePath/Awesome-Intern-Challenge $ pip3 install -r requirements.txt

---*Your environment is ready to go!*---

4) Run seed.py to create a database and create some example inventory items and shipments.
ex. (env) ~/filePath/Awesome-Intern-Challenge $ python3 seed.py

5) Run server.py and go to https://localhost:5002 *If you need a different port: you can change the port in the bottom of server.py in app.run ex. you want to run the port on 5005, this is what app.run should look like app.run(host='127.0.0.1', port=5005)*
ex. (env) ~/filePath/Awesome-Intern-Challenge $ python3 server.py

