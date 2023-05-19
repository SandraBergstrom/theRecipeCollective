# the Recipe Collective Testing
The testing.md file provides an overview of the testing conducted on the Recipe Collective website. It covers code validation, accessibility, performance, testing on various devices, browser compatibility, testing user stories, and user feedback and improvements. Each section describes the tools used, the issues found (if any), and the corresponding test results.

## Table of Content

1. [Code Validation](#html-validation)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Python Validation](#python-validation)
2. [Accessibility](#accessibility)
3. [Performance](#performance)
    1. [Desktop Performance](#desktop-performance)
    2. [Mobile Performance](#mobile-performance)
4. [Performing tests on various devices](#performing-tests-on-various-devices)
5. [Browser compability](#browser-compability)
6. [Testing user stories](#testing-user-stories)
7. [User feedback and improvements](#user-feedback-and-improvements)
8. [Summary](#summary)


## Code Validation

### HTML Validation
[W3C Markup Validation](https://validator.w3.org/) is a service provided by the W3C that allows you to validate your HTML code against the official specifications. It checks for syntax errors, improper tag usage, and other issues that may affect the structure and semantics of your web pages. Validating your HTML code with W3C Markup Validation helps ensure that your pages are well-formed and adhere to web standards

All pages passed through the validation and the code was pasted in and I used a filter to remove issues related to the Django templating system. <details><summary>See filter</summary>![Result](/docs/validation/html/filter.png)</details>

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|base| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/base.png)</details>| :white_check_mark:
|index| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/index.png)</details>| :white_check_mark:
|about| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/about.png)</details>| :white_check_mark:
|register| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/register.png)</details>| :white_check_mark:
|login| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/login.png)</details>| :white_check_mark:
|profile| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/profile.png)</details>| :white_check_mark:
|logout| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/logout)</details>| :white_check_mark:
|home| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/home.png)</details>| :white_check_mark:
|myrecipes| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/my-recipes.png)</details>| :white_check_mark:
|favorites| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/favorites.png)</details>| :white_check_mark:
|cookbook_links| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/cookbook-links.png)</details>| :white_check_mark:
|list_card| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/list_card.png)</details>| :white_check_mark:
|pagination| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/pagination.png)</details>| :white_check_mark:
|recipe_form| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/recipe-form.png)</details>| :white_check_mark:
|recipe_detail| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/recipe-detail.png)</details>| :white_check_mark:
|recipe_confirmation_delete| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/recipe-confirm-delete.png)</details>| :white_check_mark:
|

### CSS Validation
[W3C Jigsaw](https://jigsaw.w3.org/css-validator/) is a tool provided by the World Wide Web Consortium (W3C) that allows you to validate and check the correctness of your HTML and CSS code. It helps ensure that your web pages comply with the standards set by the W3C, promoting interoperability and accessibility.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|CSS file | No errors |[Result](http://jigsaw.w3.org/css-validator/validator$link)| :white_check_mark:
|Whole webpage | When validating the page as a whole, the validator shows some errors linked to Bootstrap v5.0. When validating just my own custom CSS |[Result](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthe-recipe-collective.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv#banner)| :white_check_mark:
|

### Python Validation 
[PEP 8](https://pep8ci.herokuapp.com/) is a style guide for writing Python code to ensure consistency and readability. It provides guidelines on how to format code, naming conventions for variables and functions, and other best practices. Following PEP 8 helps to improve code quality, readability, and maintainability.

The settings file had one URL that was too long, while the other lines exceeding the recommended length were automatically generated by Django.All other files had no errors and were clear of any issues.

Note: The specific details and validation results for each file can be viewed by expanding the corresponding sections.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
| settings | One URL was too long, while the other lines that exceeded the recommended length were automatically generated by Django. | ![Result](/docs/validation/pep8/settings.png) | :white_check_mark:
| views | All clear, no errors found |![Result](/docs/validation/pep8/views.png)| :white_check_mark:
|cookbook/models | 29: E501 line too long (108 > 79 characters) - URL for default image |![Result](/docs/validation/pep8/cookbook-models.png)| :white_check_mark:
|cookbook/views | All clear, no errors found |![Result](/docs/validation/pep8/cookbook-views.png)| :white_check_mark:
|users/forms | All clear, no errors found |![Result](/docs/validation/pep8/users-forms.png) | :white_check_mark:
|users/models | One line too long because of URL |![Result](/docs/validation/pep8/users-models.png)| :white_check_mark:
|users/signals | All clear, no errors found | ![Result](/docs/validation/pep8/users-signals.png)| :white_check_mark:
|users/views | All clear, no errors found |![Result](/docs/validation/pep8/users-views.png)| :white_check_mark:
|

[Back to the top](#table-of-content)

<br>

## Accessibility
[The WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) was used to assess the accessibility of the website. WAVE helps identify potential accessibility issues and provides guidance on how to improve the accessibility of web content.

During the evaluation, the following issues were identified:

- Errors: The website generated 5 errors, which are related to the Bootstrap footer. 

- Contrast Warning: I received a contrast warning for my primary button, which has white text against a brownish background. It's worth noting that I intentionally chose this design with white text, as it aligns with my overall aesthetic and branding. While I understand that using black text for better readability on the button, I have decided to maintain the white text as a deliberate design choice.

- Redundant Link Alert: The tool flagged one alert for a redundant link. This alert is due to the tool misinterpreting the {{}} inserted URL pages, mistakenly assuming they are duplicate links. I want to clarify that these links are not going to the same place. This alert does not impact the functionality or accessibility of my website.

By using the WAVE tool, I gained valuable insights into the accessibility of my website. While I have chosen not to address certain errors at this time, I remain committed to creating an inclusive user experience and will continue to explore ways to improve accessibility in the future.

[Back to the top](#table-of-content)

<br>

## Performance 
The Recipe Collective website was tested using [Google Lighthouse in Google Chrome Developer Tools](https://developer.chrome.com/docs/lighthouse/). The performance scores were evaluated for both desktop and mobile devices. Here are the summarized results:

### Desktop Performance
- Average performance score: 92/100
- The majority of pages received scores above 90/100, indicating excellent performance.
- The Logout page received a score of 85/100 due to preventing back/forward cache restoration, which is intentional to maintain security.

| **Tested** | **Performance Score** | **View Result** | **Pass** |
--- | --- | --- | :---:
|index| 98 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/index.png)</details> | :white_check_mark:
|about| 98 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/about.png)</details> | :white_check_mark:
|sign up| 98 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/signup.png)</details> | :white_check_mark:
|login | 98 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/login.png)</details> | :white_check_mark:
|profile| 94 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/profile.png)</details> | :white_check_mark:
|logout| 85 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/logout.png)</details> | :white_check_mark:
|cookbook| 83 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/cookbook.png)</details> | :white_check_mark:
|my recipes| 95 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/my-recipes.png)</details> | :white_check_mark:
|my favorites| 99 / 100| <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/my-favorites.png)</details> | :white_check_mark:
|recipe details| 98 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/recipe-detail.png)</details> | :white_check_mark:
|add recipe| 92 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/add-recipe.png)</details> | :white_check_mark:
|update recipe| 95 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/update-recipe.png)</details> | :white_check_mark:
|delete recipe|| <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/desktop/delete-recipe.png)</details> | :white_check_mark:
|

### Mobile Performance
- Average performance score: 77/100
- The pages showed slightly lower performance compared to desktop, but still maintained a satisfactory score.
- The Logout page received a score of 71/100 due to preventing back/forward cache restoration, which is intentional to maintain security.

| **Tested** | **Performance** | **View Result** | **Pass** |
--- | --- | --- | :---:
|index| 77 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/index.png)</details> | :white_check_mark:
|about| 76 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/about.png)</details> | :white_check_mark:
|sign up| 77 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/signup.png)</details> | :white_check_mark:
|login | 72 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/login.png)</details> | :white_check_mark:
|profile| 71 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/profile.png)</details> | :white_check_mark:
|logout| 71 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/logout.png)</details> | :white_check_mark:
|cookbook| 80 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/cookbook.png)</details> | :white_check_mark:
|my recipes| 77 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/my-recipes.png)</details> | :white_check_mark:
|my favorites| 88 / 100| <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/my-favorites.png)</details> | :white_check_mark:
|recipe details| 72 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/recipe-detail.png)</details> | :white_check_mark:
|add recipe| 73 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/add-recipe.png)</details> | :white_check_mark:
|update recipe| 72 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/update.png)</details> | :white_check_mark:
|delete recipe| 72 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/validation/lighthouse/mobile/delete-recipe.png)</details> | :white_check_mark:
|

Overall, the Recipe Collective website performed well in terms of performance, providing a smooth user experience on both desktop and mobile devices.

[Back to the top](#table-of-content)

<br>

## Performing tests on various devices 
The website was tested on the following devices:
- Samsung Galaxy Note S20 ultra
- Samsung Galaxy Note S22 ultra
- Apple iPhone 12
- OnePlus 8

In addition, the website was tested using Google Chrome Developer Tools Device Toggeling option for all available device options.

[Back to the top](#table-of-content)

<br>

## Browser compability
The website was tested on the following browsers:
- Google Chrome
- Mozilla Firefox
- Microsoft Egde

[Back to the top](#table-of-content)

<br>

## Testing user stories

### As a first-time user...
| **User Story** | **Action** | **Expected Result** | **Pass** |
--- | --- | --- | :---:
|[I can create an account so that I can save my recipes](https://github.com/SandraBergstrom/theRecipeCollective/issues/3#issue-1676151139)|Click on the "Signup" navigation link or the signup button on the landing page|The user should be redirected to the signup form|:white_check_mark:
|[I want to be able to access the About page so that I can learn more about the purpose, features, and benefits of the Recipe Collective without needing to create an account](https://github.com/SandraBergstrom/theRecipeCollective/issues/37#issue-1708609060)|Click on the "About" button in the navigation bar on the landing page|The user should be directed to the About page|:white_check_mark:
|

### As a returning user...
| **User Story** | **Action** | **Expected Result** | **Pass** |
--- | --- | --- | :---:
|[I can log in to my account](https://github.com/SandraBergstrom/theRecipeCollective/issues/4#issue-1676185860)|Press the login button either on the landing page or in the navbar|The user should be directed to the login page|:white_check_mark:
|[I can log out of my account](https://github.com/SandraBergstrom/theRecipeCollective/issues/4#issue-1676185860)|Press the profile button and then select the logout option|The user should be logged out of their account|:white_check_mark:
|[I can go to my profile page so that I can see my saved recipes and personal information](https://github.com/SandraBergstrom/theRecipeCollective/issues/12#issue-1676233050)|Press the profile button on the right side of the navbar and then on Profile in the drop down menu|The user should be redirected to their profile page|:white_check_mark:
|[I want to be able to navigate through a long list of recipes using pagination so that I can view and interact with the list easily](https://github.com/SandraBergstrom/theRecipeCollective/issues/21#issue-1688404118)|Scroll down to the bottom of the Cookbook, My Recipes, or Favorites section|If there are more than 9 recipes, pagination is displayed to navigate through the list|:white_check_mark:
|[I can view all recipes so that I can find new recipes to try](https://github.com/SandraBergstrom/theRecipeCollective/issues/2#issue-1676140284)|Click on the "Cookbook" link in the navigation bar|The user is directed to the recipe list view|:white_check_mark:
|[I can click on a recipe so that I can get all details and instructions about it](https://github.com/SandraBergstrom/theRecipeCollective/issues/6#issue-1676195459)|Click on the recipe title or the info button|The user is taken to the recipe detail page|:white_check_mark:
|[I can save recipes that I find in my own "cookbook" so that I can find them easily in the future](https://github.com/SandraBergstrom/theRecipeCollective/issues/17#issue-1676239448)|Click on the heart icon on the upper right part of the recipe detail page|The recipe is added to the favorites page, and a flash message appears confirming that it has been saved to favorites|:white_check_mark:
|[I can add a new recipe so that I can share it with others and save it for myself](https://github.com/SandraBergstrom/theRecipeCollective/issues/5#issue-1676191345)|Press the profile button and then "Add recipe in the dropdown navigation bar|The user is directed to the recipe form|:white_check_mark:
|[I can edit my own recipes so that I can update them if needed](https://github.com/SandraBergstrom/theRecipeCollective/issues/7#issue-1676198620)|Click on the "Update" button in the upper right corner of the recipe detail page|The user is directed to the recipe form to update the recipe|:white_check_mark:
|[I can delete my own recipe so that I can remove them if wanted](https://github.com/SandraBergstrom/theRecipeCollective/issues/8#issue-1676201972)|Click the delete button on the recipe detail page|The user is taken to a confirmation page to confirm the deletion of the recipe. Upon confirming, the recipe is deleted|:white_check_mark:
|[I can comment on a recipe so that share my thoughts and suggestions](https://github.com/SandraBergstrom/theRecipeCollective/issues/11#issue-1676227838)|Scroll down to the comment form on the recipe detail card and add a comment|The comment is successfully added|:white_check_mark:
|

### As a site owner...
| **User Story** | **Action** | **Expected Result** | **Pass** |
--- | --- | --- | :---:
|[I can view and manage user accounts to ensure the security and integrity of the site and its users](https://github.com/SandraBergstrom/theRecipeCollective/issues/1#issue-1676139643)|Access the Django admin section and navigate to the user management section|The admin section displays all users and their associated information. The owner can perform actions such as deleting users and managing their comments|:white_check_mark:
|[I can view and manage recipes to maintain a high standard of content and ensure the quality of the recipes on the site](https://github.com/SandraBergstrom/theRecipeCollective/issues/1#issue-1676139643)|Access the admin page and navigate to the recipe management section|The admin page allows the owner to view and manage all recipes, ensuring the quality and standards of the content|:white_check_mark:
|

[Back to the top](#table-of-content)

<br>

## User feedback and improvements
I conducted user testing with 10 individuals to gather feedback on their experience using the website. I asked them to perform the following tasks and provide feedback on their experience:

- Create an account
- Update the profile
- Add a recipe (1 or more)
- Update a recipe
- Delete a recipe
- Mark a recipe as a favorite
- Comment on a recipe
- Test links

Each participant was encouraged to provide feedback and report any issues or improvements they encountered during the testing process. Below is the feedback/issues reported. 

| **Feature** | **Feedback** | **Result** | **Pass** |
--- | --- | --- | :---:
|Navbar| Some users found the initial profile icon (chef's hat) unclear. Both color and icon was changed to make it more clear that this is a button for the user profile section | <details><summary>Screenshot of result</summary>![Result](/docs/validation/user-testing/user-default-img.png)</details> | :white_check_mark:
|Scrolling Recipes| Some users found the sticky footer annoying. The sticky footer was removed, resulting in a better scrolling experience for recipes. | Removed the sticky-bottom to footer which gives a better experience when scrolling the recipes in the cookbook | :white_check_mark:
|

[Back to the top](#table-of-content)

## Summary
Overall, the Recipe Collective website performed well in in all testings. The issues identified were acknowledged, and some were not addressed at the time due to design choices. 