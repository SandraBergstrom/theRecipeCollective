README

# the Recipe Collective

Are you tired of endless recipe searches, scrolling through pages of uninspiring dishes? Look no further than The Recipe Collective! Our community-driven platform offers a smorgasbord of culinary inspiration, from mouth-watering mains to decadent desserts. Whether you're a seasoned chef or a kitchen novice, we've got something to whet your appetite. Plus, with features like comments and likes, you can connect with fellow foodies and get feedback on your latest creations. 

So why settle for the same old boring meals? Join The Recipe Collective and spice up your kitchen game!

![Mockup image](docs/mockup.png)
Developer: Sandra Bergström <br>
[Live webpage](https://the-recipe-collective.herokuapp.com/)

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requrements and Expectations](#user-requrements-and-expectations)
    3. [User Stories](#user-stories)
3. [Database](#database)
    1. [User App](#user-app)
    2. [Cookbook App](#cookbook-app)
4. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colour](#colours)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Wireframes](#wireframes)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
6. [Methodology](#methodology)
    1. [Agile Project Management with GitHub Projects](#agile-project-management-with-github-projects)
    2. [User Stories as GitHub Issues](#user-stories-as-github-issues)
    3. [Bug Tracking](#bug-tracking)
    4. [Iterative Development Approach](#iterative-development-approach)
    5. [Backlog and Subsequent Iterations](#backlog-and-subsequent-iterations)
7. [Features](#features)
8. [Testing](#validation)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [Accessibility](#accessibility)
    4. [Performance](#performance)
    5. [Device testing](#performing-tests-on-various-devices)
    6. [Browser compatibility](#browser-compatability)
    7. [Testing user stories](#testing-user-stories)
9. [Bugs](#bugs)
10. [Deployment](#deployment)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

## Project Goals 
The Recipe Collective is a web application designed to provide users with a platform to discover, save, and organize recipes. The goals of the project include:

- Providing a user-friendly interface for users to browse and explore a collection of recipes.
- Allowing users to save their favorite recipes for easy access.
- Offering users the ability to upload and manage their own recipes within their personal cookbook.
- Facilitating the creation of a personal cookbook with three sections: the Collective's Recipes, User's Uploaded Recipes, and Favorite Recipes.
- Promoting culinary inspiration and sharing by enabling users to discover a variety of recipes from different cuisines and categories.

### User Goals
- Exploring and browsing a curated collection of recipes.
- Saving recipes to their personal cookbook for future reference.
- Uploading and managing their own recipes within their personal cookbook.
- Accessing their personal cookbook, which includes three sections: the Collective's Recipes, User's Uploaded Recipes, and Favorite Recipes.
- Finding culinary inspiration by discovering recipes from various cuisines, continents and categories.

### Site Owner Goals
- Providing a platform for users to discover, save, and organize recipes.
- Offering users the ability to upload and manage their own recipes.
- Enhancing user experience by curating a collection of diverse and appealing recipes.
- Encouraging users to engage with the site and share their culinary creations.

[Back up](#table-of-content)

## User Experience

### Target Audience
The Recipe Collective caters to the following target audience:

- Cooking enthusiasts and food lovers seeking culinary inspiration.
- Individuals interested in discovering recipes from various cuisines, continents, and categories.
- Users who have recipes scattered across different platforms and desire a centralized location to store and organize them.
- Individuals who want a convenient and user-friendly platform to store and manage their personal recipe collection.
- Users who wish to easily share their favorite recipes with friends and family.

By providing a seamless recipe storage and sharing experience, the Recipe Collective aims to simplify the process of organizing and accessing recipes, creating a go-to resource for home cooks and food enthusiasts alike.

### User Requirements and Expectations
When using the Recipe Collective, users can expect the following features and characteristics to meet their requirements:

- A user-friendly interface that allows for intuitive navigation and easy recipe browsing.
- High-quality recipe presentation, including clear instructions, ingredients, and visuals.
- Responsive design that ensures a visually appealing experience on different devices.
- Personalized features, such as a user cookbook to store favorite recipes and track personal creations.
- Access to a diverse collection of recipes, offering inspiration for everyday meals and special occasions.

The Recipe Collective strives to create an enjoyable and engaging environment for users to explore, discover, and share their love for cooking and delicious recipes.


### User Stories

#### Epic 1: User Authentication and Account Management

- [As a First Time User, I can create an account so that I can save my recipes](https://github.com/SandraBergstrom/theRecipeCollective/issues/3#issue-1676151139)<br>
- [As a Returning User, I can log in/out of my account so that I can access my saved recipes securely](https://github.com/SandraBergstrom/theRecipeCollective/issues/4#issue-1676185860)<br>
- [As a Returning User, I can go to my profile page so that I can see my saved recipes and personal information](https://github.com/SandraBergstrom/theRecipeCollective/issues/12#issue-1676233050)<br>
- [As a Site Owner, I can view and manage user accounts to ensure the security and integrity of the site and its users](https://github.com/SandraBergstrom/theRecipeCollective/issues/1#issue-1676139643)

#### Epic 2: Recipe Management
- [As a Returning User, I can save recipes that I find in my own "cookbook" so that I can find them easily in the future](https://github.com/SandraBergstrom/theRecipeCollective/issues/17#issue-1676239448)<br>
- [As a Returning User, I can delete my own recipe so that I can remove them if wanted](https://github.com/SandraBergstrom/theRecipeCollective/issues/8#issue-1676201972)<br>
- [As a Returning User, I can click on a recipe so that I can get all details and instructions about it](https://github.com/SandraBergstrom/theRecipeCollective/issues/6#issue-1676195459)<br>
- [As a Returning User, I can view all recipes so that I can find new recipes to try](https://github.com/SandraBergstrom/theRecipeCollective/issues/2#issue-1676140284)<br>
- [As a Returning User, I can edit my own recipes so that I can update them if needed](https://github.com/SandraBergstrom/theRecipeCollective/issues/7#issue-1676198620)<br>
- [As a Returning User, I can add a new recipe so that I can share it with others and save it for myself](https://github.com/SandraBergstrom/theRecipeCollective/issues/5#issue-1676191345)<br>
- [As a Site Owner, I can view and manage recipes to maintain a high standard of content and ensure the quality of the recipes on the site](https://github.com/SandraBergstrom/theRecipeCollective/issues/1#issue-1676139643)<br>

#### Epic 3: User Experience and Site Information
- [As a First Time User, I want to be able to access the About page so that I can learn more about the purpose, features, and benefits of the Recipe Collective without needing to create an account](https://github.com/SandraBergstrom/theRecipeCollective/issues/37#issue-1708609060)<br>
- [As a Returning User, I want to be able to navigate through a long list of recipes using pagination so that I can view and interact with the list easily](https://github.com/SandraBergstrom/theRecipeCollective/issues/21#issue-1688404118)<br>

[Back up](#table-of-content)

## Database
The Recipe Collective utilizes the following database schema:
<details><summary>See Database Schema</summary>
<img src="docs/database-er.jpeg">
</details>

### User App
- Profile model that extends the User model to add additional fields like image, food_relation, and country to store user-specific information.
- The Profile model is linked to the default Django User model using a one-to-one relationship.
- CloudinaryField from the cloudinary.models module to store the user's image with cloud-based hosting.

### Cookbook App
- Recipe model in the Cookbook app represents a recipe that users can create, view, update, and delete.
- Fields include title, author (linked to the Django User model), featured_image, excerpt, about, category, prep_time, cooking_time, servings, ingredients, instructions, date_posted, date_updated, and status.
- The favorites field establishes a many-to-many relationship with the User model, allowing users to save recipes as favorites.
- A FavoriteManager is implemented to retrieve recipes that are marked as favorites by a specific user.

[Back up](#table-of-content)

## Design
At the Recipe Collective, the design philosophy revolves around creating a clean and modern user interface that puts the spotlight on the recipes themselves. Taking inspiration from modern home kitchens, the aim is to provide a visually pleasing and immersive experience for users, where they can easily navigate, discover, and engage with a vast collection of recipes.

By adopting a minimalistic design approach, we strive to eliminate distractions and ensure that the focus remains on the culinary creations shared within the community. The use of ample white space, intuitive layouts, and crisp typography enhances readability and allows the vibrant colors and mouthwatering imagery of the recipes to take center stage.

### Design Choices

### Colour
![Mockup image](/docs/color-palette.png)

### Fonts
The Recipe Collective embraces the default fonts provided by Bootsrap 5. No specific modifications have been made to the default fonts, as they effectively contribute to the overall aesthetic and user experience of the Recipe Collective.

### Structure
The Recipe Collective is designed with a user-friendly and intuitive structure, making it easy for users to navigate and learn their way around the website. The overall structure of the website is organized into the following sections and pages:

#### Before Logged In:

- **Landing Page** The landing page serves as the initial entry point to the website, providing an introduction and overview of the Recipe Collective's purpose and features.<br>
- **About Page:** The about page provides detailed information about the Recipe Collective, including its mission, values, and the benefits of being a part of the community.<br>
- **Sign Up Page:** The sign-up page allows new users to create an account by providing their required details and registering as a member of the Recipe Collective.<br>
- **Login Page:** The login page is where registered users can securely log in to access their accounts and the full functionality of the website.<br>

#### When Logged In:
Upon logging in, users are directed to the main cookbook section of the Recipe Collective, which includes the following pages:

- **Home Page (Cookbook):** The home page of the cookbook section serves as the central hub, displaying a personalized collection of recipes based on the user's preferences, saved recipes, and recent activities within the community.<br>
- **My Recipes Page:** The "My Recipes" page allows users to view and manage the recipes they have created and contributed to the Recipe Collective. It provides options to edit, delete, and organize recipes for easy access and retrieval.<br>
- **My Favorites:** The "My Favorites" page displays a curated list of recipes that the user has marked as favorites, making it convenient to revisit and cook their preferred dishes.
- **Recipe Detail Page:** The recipe detail page provides comprehensive information about each recipe, including its title, description, ingredients, and instructions. Users have the option to add the recipe to their favorites, allowing them to easily revisit and cook their preferred dishes. Additionally, if the recipe belongs to the user, they can update or delete it, empowering them to manage their own recipes. <br>

#### Profile Navigation:
Upon clicking on the profile image in the navigation bar, additional links are revealed, providing access to specific profile-related pages and actions:

- **Profile Page:** The profile page displays the user's profile information, including their bio, profile picture, and other relevant details. It allows users to update and customize their profile settings.<br>
- **Add Recipe Page:** The "Add Recipe" page enables users to contribute their own recipes to the Recipe Collective. It provides a user-friendly form to input recipe details, including title, description, ingredients, instructions, and other relevant information.<br>
- **My Recipes:** The "My Recipes" page allows users to view and manage the recipes they have created and contributed to the Recipe Collective. It provides options to edit, delete, and organize recipes for easy access and retrieval.<br>
- **Favorite Recipes:** The "My Favorites" page displays a curated list of recipes that the user has marked as favorites, making it convenient to revisit and cook their preferred dishes.<br>
- **Logout:** The "Logout" option allows users to securely log out of their accounts, ensuring the privacy and security of their personal information.<br>

The structured design of the Recipe Collective ensures a seamless and enjoyable user experience, enabling users to explore, contribute, and manage their recipes with ease.


### Wireframes
The wireframes provide a visual representation of the different pages and features of the web application. They serve as a blueprint for the design and layout of each page, helping to visualize the user interface and overall user experience. These wireframes were created using Balsamiq, a tool that enables quick and intuitive sketching of design ideas.

<details><summary>Log in (landing page)</summary>
<img src="docs/wireframes/index.png">
</details>
<details><summary>About</summary>
<img src="docs/wireframes/about.png">
</details>
<details><summary>Sign Up</summary>
<img src="docs/wireframes/register.png">
</details>
<details><summary>The Collective Cookbook</summary>
<img src="docs/wireframes/home.png">
</details>
<details><summary>My Recipes</summary>
<img src="docs/wireframes/my-recipes.png">
</details>
<details><summary>My Favorites</summary>
<img src="docs/wireframes/my-favorites.png">
</details>
<details><summary>Add/Update Recipe</summary>
<img src="docs/wireframes/add-update-recipe.png">
</details>
<details><summary>Recipe Detail</summary>
<img src="docs/wireframes/recipe-detail.png">
</details>
<details><summary>Profile</summary>
<img src="docs/wireframes/profile.png">
</details>
<details><summary>Logout</summary>
<img src="docs/wireframes/logout.png">
</details>
<br>

[Back up](#table-of-content)

## Technologies Used

### Languages
- HTML
- CSS
- Python

### Frameworks
- Django: A high-level Python web framework used for building the Recipe Collective website.
- Crispy Forms: A Django package used for rendering forms in a more efficient and customizable way.
- Bootstrap v5.0: A popular CSS framework used for creating responsive and visually appealing user interfaces.
- Materialize: A modern responsive CSS framework that provides ready-to-use components and styles for building user interfaces in the Recipe Collective project.
- Cloudinary: A cloud-based media management platform used for storing and serving images in the Recipe Collective project.

### Database
- ElephantSQL: ElephantSQL is a PostgreSQL database as a service. It is used as the database for the Recipe Collective project, providing a reliable and scalable storage solution for the application's data.

### Tools
- Git: A distributed version control system used for tracking changes in the project's source code.
- GitHub: A web-based hosting service for version control repositories, used for storing and managing the project's source code.
- Gitpod: An online integrated development environment (IDE) used for developing and testing the Recipe Collective project.
- Heroku: A cloud platform that enables deployment and hosting of web applications. Heroku was used for deploying the Recipe Collective project to a live server.
- Adobe Photoshop: A professional image editing software used for advanced image manipulation and design in the Recipe Collective project.
- Balsamiq: A wireframing tool used for creating mockups and prototypes of the Recipe Collective website.
- Lucidchart: Lucidchart is a web-based diagramming tool that offers a wide range of diagramming capabilities, including ER diagrams. It provides an intuitive interface and collaboration features, making it suitable for both individual and team use.
- Google Fonts: A collection of free and open-source fonts used for typography on the Recipe Collective website.
- Font Awesome: A library of icons used for adding scalable vector icons to the Recipe Collective website.

### Supporting Libraries and Packages
- asgiref==3.6.0: ASGI specification reference implementation for Django.
- cloudinary==1.32.0: Python SDK for integrating Cloudinary into Django applications.
- crispy-bootstrap5==0.7: A Django app that adds crispy-forms support to Bootstrap 5.
- dj-database-url==0.5.0: A Django utility for utilizing 12factor inspired DATABASE_URL environment variables.
- dj3-cloudinary-storage==0.0.6: A Django package that provides Cloudinary storage for Django applications.
- django-crispy-forms==2.0: A Django package that helps you manage Django forms in a DRY way.
- gunicorn==20.1.0: A Python WSGI HTTP server for UNIX, commonly used for deploying Django applications.
- psycopg2==2.9.6: PostgreSQL adapter for Python, used for connecting Django to a PostgreSQL database.
- pytz==2023.3: A Python library that provides timezone support.
- sqlparse==0.4.4: A non-validating SQL parser for Python, used by Django for SQL query parsing.
- requests==2.26.0: A Python library for making HTTP requests, often used in Django projects for external API integrations.

[Back up](#table-of-content)

## Methodology
The Recipe Collective project has been developed using agile principles, enabling efficient collaboration, iterative development, and effective project management. The following methodology has been employed throughout the project:

### Agile Project Management with GitHub Projects
GitHub Projects has been utilized to facilitate agile project management. User stories and bugs have been organized as GitHub issues, allowing for a clear and structured approach to development. The project board in GitHub Projects serves as a Kanban board, providing an overview of the project's progress.

### User Stories as GitHub Issues
Each user story has been created as a GitHub issue, capturing the desired functionality from the user's perspective. The user stories are linked to their corresponding GitHub issues, allowing easy access to the acceptance criteria, tasks, and comments associated with each user story.

### Bug Tracking
Bugs encountered during the development process have also been logged as GitHub issues. These issues contain details about the specific bug, its impact, and steps to reproduce it. By linking the bugs in the README.md to their respective GitHub issues, users can gain insights into the bugs' resolution progress and view any additional comments.

### Iterative Development Approach
The Recipe Collective project adopts an iterative development approach, allowing for continuous improvement and progress within the given time constraints. Although the project timeline has been condensed, it has been structured to accommodate future iterations and enhancements.

### Backlog and Subsequent Iterations 
The user stories are tracked on the project board, and the "To do" column represents the backlog of user stories, indicating the tasks that will be addressed in subsequent iterations.

Please note that even though the project timeline has been accelerated, the iterative development approach allows for ongoing improvements and enhancements to meet the evolving needs of users.

For a comprehensive view of the project progress, user stories, and bug tracking, please see the [Kanban board](https://github.com/users/SandraBergstrom/projects/6).

[Back up](#table-of-content)

## Features
### Landing Page:
- The landing page serves as the entry point to the Recipe Collective, providing an introduction and overview of the platform.
- Users can easily navigate to different sections of the website through the navigation bar.

### Recipe Pages:
- Recipe details page displays comprehensive information about each recipe, including ingredients, instructions, and cooking time.
- Users can view, create, update, and delete recipes through CRUD functionality.

### User Account Management:
- Account sign-up form allows new users to create an account and join the Recipe Collective community.
- Users can log in to their accounts to access personalized features and settings.
- Profile page enables users to view and update their profile information.
- Users have the ability to update their delivery information and manage their account settings.

### Recipe Management:
- Recipe creators can add, edit, and delete recipes from their profile.
- Comprehensive forms facilitate easy recipe submission and editing.

### Navigation:
- The navigation bar provides easy access to different sections and pages of the Recipe Collective.

The Recipe Collective focuses on providing a clean and user-friendly design, with a focus on the recipes themselves. It emphasizes CRUD functionality, allowing users to create, read, update, and delete recipes as they contribute to the culinary community. The platform aims to inspire and facilitate the sharing of delicious recipes among users.

[Back up](#table-of-content)

## Testing
Index
About
Sign up
Login
Profile
Logout
Cookbook
My recipes
Favorite recipes
Recipe Details
Add/Update recipe
Delete recipe

### HTML Validation
[W3C Markup Validation](https://validator.w3.org/) is a service provided by the W3C that allows you to validate your HTML code against the official specifications. It checks for syntax errors, improper tag usage, and other issues that may affect the structure and semantics of your web pages. Validating your HTML code with W3C Markup Validation helps ensure that your pages are well-formed and adhere to web standards

<details><summary>Index</summary>
<img src="#">
</details>
<details><summary>About</summary>
<img src="#">
</details>
<details><summary>Sign up</summary>
<img src="#">
</details>
<details><summary>Login</summary>
<img src="#">
</details>
<details><summary>Profile</summary>
<img src="#">
</details>
<details><summary>Logout</summary>
<img src="#">
</details>
<details><summary>Logout</summary>
<img src="#">
</details>

### CSS Validation
[W3C Jigsaw](https://jigsaw.w3.org/css-validator/) is a tool provided by the World Wide Web Consortium (W3C) that allows you to validate and check the correctness of your HTML and CSS code. It helps ensure that your web pages comply with the standards set by the W3C, promoting interoperability and accessibility.

| **Tested** | **Result** | **Validation Result** |
| ----------- | ----------- | ----------- |
|CSS file | No errors |[Result](http://jigsaw.w3.org/css-validator/validator$link)|
|Whole webpage | When validating the page as a whole, the validator shows some errors linked to Bootstrap v5.0. When validating just my own custom CSS |[Result](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthe-recipe-collective.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv#banner)|
|

### Python Validation 
[PEP 8](https://pep8ci.herokuapp.com/) is a style guide for writing Python code to ensure consistency and readability. It provides guidelines on how to format code, naming conventions for variables and functions, and other best practices. Following PEP 8 helps to improve code quality, readability, and maintainability.

The settings file had one URL that was too long, while the other lines exceeding the recommended length were automatically generated by Django.All other files had no errors and were clear of any issues.

Note: The specific details and validation results for each file can be viewed by expanding the corresponding sections.

| **Tested** | **Result** |
| ----------- | ----------- |
| settings | One URL was too long, while the other lines that exceeded the recommended length were automatically generated by Django.|
<details><summary>Result</summary>![Result](/docs/validation/pep8/settings.png)</details>
| ----------- | ----------- |
| views | All clear, no errors found |<details><summary>Result</summary>![Result](/docs/validation/pep8/views.png)</details>|
|cookbook/models | 29: E501 line too long (108 > 79 characters) - URL for default image |<details><summary>Result</summary>![Result](/docs/validation/pep8/cookbook-models.png)</details>|
|cookbook/views | All clear, no errors found |<details><summary>Result</summary>![Result](/docs/validation/pep8/cookbook-views.png)</details>|
|users/forms | All clear, no errors found |<details><summary>Result</summary>![Result](/docs/validation/pep8/users-forms.png)</details>|
|users/models | One line too long because of URL |<details><summary>Result</summary>![Result](/docs/validation/pep8/users-models.png)</details>|
|users/signals | All clear, no errors found |<details><summary>Result</summary>![Result](/docs/validation/pep8/users-signals.png)</details>|
|users/views | All clear, no errors found |<details><summary>Result</summary>![Result](/docs/validation/pep8/users-viewss.png)</details>|
|

### Accessibility
[The WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) was used to assess the accessibility of the website. WAVE helps identify potential accessibility issues and provides guidance on how to improve the accessibility of web content.

During the evaluation, the following issues were identified:

- Errors: The website generated 5 errors, which are related to the Bootstrap footer. 

- Contrast Warning: I received a contrast warning for my primary button, which has white text against a brownish background. It's worth noting that I intentionally chose this design with white text, as it aligns with my overall aesthetic and branding. While I understand that using black text for better readability on the button, I have decided to maintain the white text as a deliberate design choice.

- Redundant Link Alert: The tool flagged one alert for a redundant link. This alert is due to the tool misinterpreting the {{}} inserted URL pages, mistakenly assuming they are duplicate links. I want to clarify that these links are not going to the same place. This alert does not impact the functionality or accessibility of my website.

By using the WAVE tool, I gained valuable insights into the accessibility of my website. While I have chosen not to address certain errors at this time, I remain committed to creating an inclusive user experience and will continue to explore ways to improve accessibility in the future.

### Performance 
Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website. 

| **Tested** | **Result** | **Validation Result** |
| ----------- | ----------- | ----------- |

<details><summary>Index</summary>
<img src="#">
</details>
<details><summary>About</summary>
<img src="#">
</details>
<details><summary>Sign up</summary>
<img src="#">
</details>
<details><summary>Login</summary>
<img src="#">
</details>
<details><summary>Logout</summary>
<img src="#">
</details>
<details><summary>Cookbook</summary>
<img src="#">
</details>
<details><summary>My recipes</summary>
<img src="#">
</details>
<details><summary>Recipe Details</summary>
<img src="#">
</details>
<details><summary>Add/Update recipe</summary>
<img src="#">
</details>
<details><summary>Delete recipe</summary>
<img src="#">
</details>
<details><summary>Cookbook</summary>
<img src="#">
</details>
<br>

### Performing tests on various devices 
The website was tested on the following devices:


In addition, the website was tested using Google Chrome Developer Tools Device Toggeling option for all available device options.

### Browser compatability
The website was tested on the following browsers:
- Google Chrome
- Mozilla Firefox
- Microsoft Egde

### Testing user stories


[Back up](#table-of-content)

## Bugs

### Known bugs

| **Bug** | **Status** |
| ----------- | ----------- |
| [I can't get the active link to show. I use active class according to bootstrap but it will not change when I go to another page.](https://github.com/SandraBergstrom/theRecipeCollective/issues/30)| ... |
|||

### Fixed bugs 

| **Bug** | **Fix** |
| ----------- | ----------- |
|[If there is less than 3 recipe cards it will not look good any longer. The cards get slimmer and the page layout get strange when only 1 card.](https://github.com/SandraBergstrom/theRecipeCollective/issues/36)|The problem seems to have been a fixed height on the .card-img-top. I have now changed it to keep an image ratio of 1:1 widht a full widht.|
|[Prep time and cooking time is showing seconds and not minutes.](https://github.com/SandraBergstrom/theRecipeCollective/issues/23)|Changed from DurationField to PositiveIntegerField. <br> [See detailed steps](https://github.com/SandraBergstrom/theRecipeCollective/issues/23#issuecomment-1549336886)|
|[Cant delete users from admin page](https://github.com/SandraBergstrom/theRecipeCollective/issues/35)|High priority: Because of an old field in one of the models. Will change database to a clean before deploy.|
|[Error message E-tag when deploying to Heroku. Temporary solves when I remove the static folder in Cloudinary. But that also removes all profile pictures and recipe images.](https://github.com/SandraBergstrom/theRecipeCollective/issues/32)|Before deploying on Heroku the static folder in Cloudinary have to be removed. This wiill not remove recipe or profile images.|
|[Heart icon does not show as saved (solid) when recipe is saved to favorites.](https://github.com/SandraBergstrom/theRecipeCollective/issues/28)|Temporary solution - removed it from the recipe card.<br> Low priority: Since we have a functioning heart icon in the recipe details for users to save them to favorites, this is of low priority and can be addressed in a future update.|
| [Default recipe pic is not showing](https://github.com/SandraBergstrom/theRecipeCollective/issues/25)| Added if statement in the detail template to show the placeholder if image is default, else show uploaded image. |
| [When trying to update a recipe with an uploade picture instead of the default placeholder, it will not update.](https://github.com/SandraBergstrom/theRecipeCollective/issues/27) | When fixing [#25](https://github.com/SandraBergstrom/theRecipeCollective/issues/25) I instead created this bug. I have now removed the if statment again. I then updated the recipe model and removed the placholder variable and instead added a placeholder image on cloudinary which I directly link to as default in the featured_image field. See more details in bug link.
|[Last updated field not working in recipe detail. It is working in the recipe card in the list so check there.](https://github.com/SandraBergstrom/theRecipeCollective/issues/22)|Corrected model field name.|
|[Default profile pic is not showing. Tried both to add a direct link to cloudinary and to store it locally.](https://github.com/SandraBergstrom/theRecipeCollective/issues/24)|In the profile model that extends the user I added a imageField instead of CloudinaryField. I switched, added a cloudinary link and problem solved.|
|[Can't connect to fontawesome](https://github.com/SandraBergstrom/theRecipeCollective/issues/26)|Installed fontawesome for bootstrap 5|
|[Food relation should be showing after username on the recipe cards, but it's not anymore. Now it's only showing the code.](https://github.com/SandraBergstrom/theRecipeCollective/issues/31)|When I use format document it creates a linebreak right after "{{" in "{{ recipe.author.profile.get_food_relation_display }}" which will create problems.|
|||

[Back up](#table-of-content)

## Deployment
The website was deployed using Heroku by following these steps:
1. Set DEBUG to False in the settings.py file.
2. Commit and push your code to the GitHub repository.
3. Clear the 'static' folder in Cloudinary to ensure the latest static files are used during deployment. This step is important to avoid any potential conflicts between cached versions of static files and the updated versions being deployed. Clearing the 'static' folder ensures that the latest versions of static files are used during the deployment process, preventing any eTag errors or inconsistencies.
4. Navigate to the project's deploy page in Heroku.
5. Choose the manual deployment option to deploy the latest code changes.

You can for fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
3. Wait for the forking process to complete. Once done, you will have a copy of the repository in your GitHub account.

You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select your preferred method for cloning: HTTPS, SSH, or GitHub CLI, and click the copy button to copy the repository URL to your clipboard.
4. Open Git Bash (or your preferred terminal).
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Type the command **'git clone'** followed by the URL you copied in step 3. The command should look like this: **git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY**.
7.Press Enter to create your local clone.

[Back up](#table-of-content)

## Credits
Images not referenced below are owned by the developer.

### Media

## Acknowledgements
I would like to acknowledge the following tutorial which provided valuable guidance and inspiration during the development of this project:

[Python Django Tutorial: Full-Featured Web App](https://youtu.be/UmljXZIypDc)  Key Insights:
- User Extension: The tutorial/resource explained how to create a custom user model that extends the default Django user model. It provided insights into adding additional fields to the user model, such as profile image, food relation, and country, allowing for more personalized user profiles.
- User Registration: I learned how to implement a user registration view using the UserCreationForm and handling form validation. The tutorial/resource also demonstrated how to display success messages upon successful registration.
- Profile Management: The tutorial/resource guided me through the process of creating views for profile editing and updating. It covered the usage of ModelForms and handling form submissions, including updating the user model and associated profile data.
- Authentication and Authorization: I gained a better understanding of implementing login and logout views using Django's built-in authentication system. The tutorial/resource explained how to leverage the authentication system's features for secure user authentication and authorization.
- Recipe-related Views: Additionally, the tutorial provided insights into creating views for managing recipes.

I am grateful for the creators of the tutorial for their efforts in creating a helpful learning material.

I would like to express my gratitude and extend my thanks to the following individuals who have been instrumental in my journey:
- Jubril Akolade, my mentor, for his invaluable feedback, advice, guidance, and support throughout this experience.
- Paul Thomas O'Riordan, our cohort facilitator, for his dedication and weekly meetings where he has provided guidance, support, and encouragement to our cohort.
- The wonderful members of the Code Institute Slack community for their willingness to provide peer code reviews and support.

I am truly grateful for their contributions, which have greatly enriched my learning and development.