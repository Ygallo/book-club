
# Page Turner Book Club

Page Turner Book Club is an app to book lovers to find book to read and upload book for other user to explore. It is tarjet for people who like reading and areb interested in discussing and commenting about the books. There will be a monthly poll where user can vote for a book title to discuss on or just leave a comment. 


## Table of contents
- [Page Turner Book Club](#page-turner-book-club)

 * [User Experience (UX)](#user-experience-ux)
    + [User Stories](#user-stories)
    + [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  * [Agile Methodology](#agile-methodology)
  * [Data Model](#data-model)
  * [Testing](#testing)
  * [Security Features and Defensive Design](#security-features-and-defensive-design)
    + [User Authentication](#user-authentication)
    + [Form Validation](#form-validation)
    + [Database Security](#database-security)
    + [Custom error pages:](#custom-error-pages-)
  * [Features](#features)
    + [Header](#header)
    + [Footer](#footer)
    + [Home Page](#home-page)
    + [Books](#books-page)
* [User Account Pages](#user-account-pages)
    + [My Books](#my-books)
    + [Add Books](#add-book-form)
    + [Edit Book](#edit-book-form)
    + [Delete RecipeBook](#delete-book)
    + [Error Pages](#error-pages)
    + [Future Features](#future-features)
  * [Deployment - Heroku](#deployment---heroku)
  * [Forking this repository](#forking-this-repository)
  * [Cloning this repository](#cloning-this-repository)
  * [Languages](#languages)
  * [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  * [Credits](#credits)
  * [Acknowledgments](#acknowledgments)

## User Experience (UX)

A visitor of the Page Turner Book Club would be someone who is a an avid reader and is looking to be part of like-minded people group where he can discuss, recomend and find new reading interests.

### User Stories

#### User Profile
- As a User I can register an Account so that so I can join a book club and connect with other readers.
- As a User, I can log in or log out of my account so that I can have access to member benefits such as comments and votes.

#### User Navigation

- As a User, I can navigate the site intuitively  so that I can find content I am interested in.
- As a User, I can view a paginated list of books so that I can select a book to read more information about it.
- As a User, I can click on a book so that I can read the full description, and author and view comments left by other users.

#### Book Management and interaction 
- As a Site Admin/User I can add new books so that members can always find a book that appeals to them
- As a Site User I can like or unlike a book so that so that other members can get a sense of whether or not they would enjoy reading the same books.
- As a Site User I can vote on the book poll so that I can be involved in the monthly discussion.

#### Site Administration

- As a Site Admin I can create, read, update, and delete comments so that manage the content and the website remains safe.
- As a Site Admin I can moderate comments on the website so that the site remains safe and friendly.
- As a Site Admin/User I can add new books so that members can always find a book that appeals to them.
- As a Site Admin I can suggest books for the club to read in a poll so that so that we can continue to explore new topics and genres.

#### User stories for future implementation


## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

