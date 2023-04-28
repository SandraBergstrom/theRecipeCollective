# the Recipe Collective

Are you tired of endless recipe searches, scrolling through pages of uninspiring dishes? Look no further than The Recipe Collective! Our community-driven platform offers a smorgasbord of culinary inspiration, from mouth-watering mains to decadent desserts. Whether you're a seasoned chef or a kitchen novice, we've got something to whet your appetite. Plus, with features like comments and likes, you can connect with fellow foodies and get feedback on your latest creations. 

So why settle for the same old boring meals? Join The Recipe Collective and spice up your kitchen game!

[AmIResponsive-img]

Visit the live web app: The Recipe Collective

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)



### User Stories


## Design


### Colour Scheme


### Typography


### Imagery



### Wireframes


## Features

### General features on each page


### Future Implementations


### Accessibility


## Technologies Used


### Languages Used


### Frameworks, Libraries & Programs Used

## Deployment & Local Development


### Deployment


### Local Development


#### How to Fork


#### How to Clone


## Testing

Testing
Registration form
- Name validation tested - if username already excists - can't register
- Password validation - if not a match, can't register
- Flash message shows to confirm user is created when validation is ok. Yes
- Check in django admin panel if user was actually created. Yes, it was
- Check if email was saved  - yes

## Bugs

### Known bugs
- Last updated not working in recipe detail.
- Prep time and cooking time is showing seconds and not minutes
- Default profile pic is not showing. Tried both to add a direct link to cloudinary and to store it locally. 
- Default recipe pic is not showing.
- Can't connect to fontawesome

### Solved bugs
- Update user profle form is not working. Keep getting the error message: Type Error at /profile/. Exception Value: 'UserUpdateForm' object is not iterable. 
  - Solved: Forgot to put inherit forms.ModelForm in the class UserUpdateForm. 

- Cancel in delete view not working. Asking for a success url. 
  - Had to switch from <button> to <a>

- Recipe images are not showing. Trying to re-direct to default. 
  - Had to add image field in the detail template. 


## Credits


### Code Used


### Content


###  Media

  
###  Acknowledgments
