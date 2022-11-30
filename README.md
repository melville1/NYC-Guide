<h2>NYC-Guide</h2>

<h3>Welcome to the Big Apple!</h3>

<p>
And boy is it big! At over 300 square miles, no one would blame you for getting lost. What makes The City so special is it's rich diversity. In fact, Queens borough is often referred to as "The World's Borough" because of how many diverse ethnic groups live there. You can walk down the street and visit the world's cuisines all in a single block. It isn't an overstatement to say that in Queens you could have a Greek breakfast, Brazilian coffee, Lebanese falafel for lunch, and swing by your favorite Ethiopian restaurant for delectable awaze tibs for dinner.

This brings up an important feature of Gotham City. It is divided into five boroughs that each have their own unique characters and energies. Each of them (except for poor tiny Staten Island) could qualify as major cities in their own right! It is with the vastness of The Empire City in mind that we bring you this web guide. Right here, at your fingertips, you can preview all of the things that make NYC such a treat. Whether you're looking to visit it's iconic parks, get lost in a museum, or just take a nice relaxing day off at the beach, we provide you with the definitive guide to where you can find it. Happy traveling!
</p>

<h3>And now for all you boring coding people...</h3>

<p>

This is a project completed for Justice Through Code by Melvin and Milad (mostly Melvin). We utilized the Django framework to create this app. Here are the steps we took to create and run a virtual environment, create a requirements.txt file, and run the app on our local servers:
</p>

<ol>

<li>Create the virtual environment with <em>py -m venv venv</em></li>
<li>Activate the virtual environment with <em>venv\scripts\activate (on Windows)</em></li>
<li>Create a requirements file with <em>pip freeze > requirements.txt</em></li>
<li>Create a Django project with <em>django-admin startproject NYCGuide</em></li>
<li>Create the app within the project with <em>py manage.py startapp nycAPP</em></li>
<li>Install the app in the NYCGuide <em>settings.py</em> file</li>
<li>Create a <em>urls.py</em> file inside of nycAPP</li>
<li>Include the nycAPP <em>urls.py</em> path in the NYCGuide <em>urls.py</em> file</li>
<li>Create views and templates and <em>make sure they work</em></li>
<li>Run the server with <em>py manage.py runserver</em></li>
<li>Try it out, and most importantly, <em>have fun!</em></li>

</ol>

