
Create the Projects section

1. Create an app named projects
2. Install the app in setting.py under config folder
3. Create a folder named projects under templates folder
4. Create a template named list.html
    4.1 Add the projecs section of the old version of the porfolio (use the about.html as example)
5. Create a view named projects_list
    5.1 Render the list.html
6. Create the urls.py file under projects app
7. Create the urlpattern to for the projects_list view
8. Include the urls of the projects app to the urls under config folder

Fernanda Murillo 8:03 PM
Create the Projects section

1. Create an app named projects:
    python3 manage.py startapp projects 

2. Install the app in setting.py under config folder
    INSTALLED_APPD = [
        'pages',
        'projects',
    ]

3. Create a folder named projects under templates folder


4. Create a template named list.html
    4.1 Add the projecs section of the old version of the porfolio (use the about.html as example)

5. Create a view named projects_list
    5.1 Render the list.html

6. Create the urls.py file under projects app

7. Create the urlpattern to for the projects_list view

8. Include the urls of the projects app to the urls under config folder

Mini challenge 2

 create the experience section



<h2> My experience is here! </h>

Fernanda Murillo 11:17 AM
Create the Experience section

1. Create an app named experience:
    python3 manage.py startapp experience 

2. Install the app in setting.py under config folder
    INSTALLED_APPD = [
        'pages',
        'projects',
        'experience',
    ]

3. Create a folder named experience under templates folder

4. Create a template named list.html
    4.1 Add <h2>My experence section here</h2>

5. Create a view named experience_list
    5.1 Render the list.html

6. Create the urls.py file under experience app

7. Create the urlpattern to for the experience_list view

8. Include the urls of the experience app to the urls under config folder


mini challenge 3

    1.1 entity
    1.2 title
    1.3 description
    1.4 period
    1.5 technologies
    Note: Do not forget about the __str__ function.

2. Create the Technology model with the following attibutes:
    2. name
    Note: Do not forget about the __str__ function.

3. Register the modeles in the admin panel.
    Note: Do not forget to makemigrations and migrate.

4. Add two experience records from the admin panel.

5. Get the data in the experience_list view.
    5.1 Pass the data to the html as a dictionary. 
    
6. Display the data in list.html under templates  > experience.

