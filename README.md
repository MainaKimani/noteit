# Note It API
This is a notes app api that is built using django. The api acts as a backend and has endpoints that can communicate with a frontend application. 
In this case, I developed a react frontend application that was integrated with this api. ([Here is the github repository](https://github.com/MainaKimani/noteit-frontend))

With the React frontend application, users can register,  and create notes that will only be available to them.

Swagger UI was used to visualize and interact with the API’s resources without having any frontend in place.  
Here are the screenshots of the available endpoints (notes and authentication)!

<img width="720" alt="API-notes_api" src="https://user-images.githubusercontent.com/48632817/213995435-72019ff7-0a9d-4f12-a108-f5e0380c4791.png">  


<img width="720" alt="API-auth" src="https://user-images.githubusercontent.com/48632817/213994866-1d86a8c1-90ea-4333-8e15-f982d60b0594.png">



## Installation steps
Feel free to clone or fork this repository, disect, and build a beautify front-end 

1. Ensure you have python3 and pip installed

2. Clone the repository 
    ```
        git clone https://github.com/MainaKimani/noteit.git`
        cd noteit
    ```

3. create a virtual environment using `virtualenv env`

4. Activate the virtual environment by running `venv/bin/activate`

    - On Windows use `venv\Scripts\activate.ps1`

5. Install the dependencies using `pip install -r requirements.txt`

6. You also need to edit .env (.env.bat on windows) file to specify SECRET_KEY and the email credentials if you'll have to send users a verification link upon registration.

7. Run the django development server using 
    `python manage.py runserver`
    #or
    `gunicorn --chdir simple_notes simple_notes.wsgi --preload`


## Testing 
Tests are a key aspect in ensuring that the application works and is the first line of defense against bugs. Additionally, tests help in CI/CD by automating the tests. Manual testing of code becomes tedious as the application size grows. Unit tests ensure that every component you add to your application works as expected without breaking the functionality of other features.
Each application within the project has its own test folder that contain the test files. 

-There are URL tests which makes a HTTP request to the provided path and checks if the result code is successful.

-Model tests on the other hand tests whether the value returned from each model is valid as well as the absolute URL returned from the model.

-The views tests check whether and end points can be created correctly and data passing based on authentication status.

I am continually writing and refining tests within this section so don’t worry if you find some changes if you are following along.
You can run the test using this command

`$ python manage.py test`

You can also check the scope of test coverage by running this command to see the stats.

`$ coverage report`  

Django supplies are the deployment checklists. These are scripts that check for potentially dangerous security settings.

To run the checklist: 

` $ python manage.py check --deploy`


## Git Workflow and CI/CD simulation
Although this project was handled individually, I assumed that I was working with a team hence followed a workflow that mirrored how developers work in their daily lives. This involved working with commits, pushes, pull requests, merges and a ci/cd pipeline using GitHub Actions.

The workflow involved the following major steps:

1. Creating a repository with both a `MASTER` and `Development`branches. Reason behind this set up is that, any push to master branch will be deployed to production and develop to the staging.
2. A developer working on any feature should create a branch from the `DEVELOPMENT` branch and then submit a pull request upon completion.
3. On submit requeste, a workflow should run and check if the formatting of the codes are fine, run tests, package, and deploy to staging (docker hub in this case) among other jobs that might be in the pipeline. 
4. Afterwards, the project lead and other reviewers can approve the staged deployment, thus pushing it to the master branch, thus triggering the final tests and deployed to production.

Here is a link to learn more about how I automated this projects's workflow from building to tessting to deploying on Docker Hub using GitHub Actions. 


## Security Considerations
The project has two important applications; the authentication and notes applications. The notes application has GET, POST, PUT, and DELETE endpoints that make it easier to be integrated with any frontend application.

The authentication app brings in the registration and login features on board to ensure that only the authorized users can use the application. Besides, JSON Web Token authentication was also utilized for this simple client-server communication. 

The signature is issued by the JWT backend, using the header + payload + SECRET_KEY. Upon each request this signature is verified. If any information in the header or in the payload was changed by the client it will invalidate the signature. As a result, this upholds the integrity of the backend data since only an authenticated user can perform CREATE, READ, UPDATE, and DELETE requests.

## Monitoring
Prometheus is used in this project to monitor the application during runtime; which is an open-source systems monitoring and alerting toolkit that can be used to easily and cheaply monitor infrastructure and applications. Once you run the application, you case the logs on port `:8000/metrics`. However, the view a detailed dashbord, one would require cloud platform or a running container instance. 
