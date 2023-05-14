
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
    + [Delete Book](#delete-book)
    + [Vote Question](#vote-question)
    + [Vote Choices](#vote-choices)
    + [Vote Results](#Vote-results)
    + [Error Pages](#error-pages)
    + [Future Features](#future-features)
  * [Deployment - Heroku](#deployment---heroku)
  * [Forking this repository](#forking-this-repository)
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

The following user stories were left out of the project due to time constraints and labelled as "Won't Have" on the project board on Github. It is intended for these user stories to be implemented at a later date. 

- As a Site User I can filter books by genre so that I can find the ones I am more interested in.
- As a Site User I can see a list of upcoming book club meetings and events so that I can plan a reading schedule accordingly.

- As a Site Admin I can schedule and manage events/meetings so that members can easily RSVP and keep track of upcoming events.
- As a Site Admin I can send out reminders and notifications about upcoming meetings/events so that everyone stays up to date with events/meetings.
- As a Site Admin I can send an automatic Zoom meeting link to members so that they can easily connect with members on the monthly discussion.

## Design

The book club website embraces a simple and clean design approach, intentionally chosen to align with its core objective of fostering a tranquil experience for users. The objetive was to maintain a cohesive color scheme across the website, promoting a harmonious and relaxing aesthetic. 

### Colour Scheme
Colour palette from Colormind

![colormind](https://res.cloudinary.com/dne60wscn/image/upload/v1684098289/static/readme%20images/Colormind-pageturner_brcmmp.jpg)

The website embraces a color scheme that primarily features a soft and gentle pale yellow for the backgrounds, while employing a pink shade for accents. The navigation bar adopts a sophisticated and subdued dark grey-blue tone, while the footer has a vibrant touch of orange.

These carefully selected colors create a harmonious and neutral ambiance, while simultaneously offering distinct contrasts that add visual interest to the design. By combining neutral and contrasting colors, the website achieves a balanced and engaging aesthetic that appeals to users and enhances their overall experience.

#### Imagery
There are only a few static images on the site-s main page. Three big images for the carousel and one smaller one at the bottom for the featurette.  The rest of the imagery will be uploaded by users or the admin on when adding books to the club. 

#### Fonts
Open Sans imported via Google Fonts is the main font used for the the website.  Sans Serif is the fallback font.

#### Wireframes

![wireframe]

## Agile Methodology 

Github projects was used to manage the development process using an agile approach. Please see link to project board [here](https://github.com/users/Ygallo/projects/3)

## Data Model

Throughout the project, I applied the principles of Object-Oriented Programming (OOP), leveraging the power of Django's Class-Based Generic Views. 

Django AllAuth was used for the user authentication system.

In order for the users/ admin to add books to the club a model was required. **User** entity represents the registered users of the website, who can add books, like, comment and participate in discussions. Each user has a unique ID, name, email, and password.

**Book** entity represents the collection of books that the book club members can read and discuss. Each book has a unique ID, title, author, image, description and genre among the others.

The **Comment** model allows users to comment on individual books and the Book is a foreign key in the comment model given a comment can only be linked to one book. 

The **Question** model represents a poll created to vote on the proposed books.
The **Choice** model represent the book choices the members will vote on. This is a ForeingKey as the choices will be take from the books on the club.

The **Vote** represents a poll (question) created to vote on the proposed books.

The **Book of the Month** is the Model that will display the winner book of the vote.

The diagram below details the database schema.

![datamodel](https://res.cloudinary.com/dne60wscn/image/upload/v1684098289/static/readme%20images/data-model_hedufr.jpg)


## Testing

# link testing
Testing and results can be found [here]()

## Security Features and Defensive Design

### User Authentication
The login_required decorator is used to ensure only logged in users can vote on the monthly book poll and non-authenticated users are redirected to the login page.

### Database Security

To enhance security, I implemented specific measures in the project. Firstly, I ensured that sensitive information like the database URL and secret key were stored in the env.py file. By keeping these details separate and preventing them from being pushed to Github during the initial setup, I minimized the risk of unauthorized access or unwanted connections to the database.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

### Custom error pages:

Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

- 404 Page Not Found - Oh no! Whatever book you are lookin for doesn't seem to exist.

## Features

## Header

![header]

- The name of the Page is to the left of the navigation bar, is present in all the pages and likes back to the homepage.
- The navigation bar includes links to all the pages on the site.
- The Account navigation link is a drop down menu which includes the Sign up and Log in links. 


![logged-user](https://res.cloudinary.com/dne60wscn/image/upload/v1684098289/static/readme%20images/navbar_myqcp1.jpg)

- When the user has logged in, the Account drop down menu changes to display the opcion to add Books, My books and Log out option.
- The navigation bar is fully responsive, collapsing into a hamburger menu when the screen size becomes too small.
- Hovering over the links will change the font from pale yellow to pink.

### Footer

![footer](https://res.cloudinary.com/dne60wscn/image/upload/v1684098289/static/readme%20images/footer_x1qvbf.jpg)

- The footer section includes links to Facebook, Instagram and Twitter.
- Clicking the links in the footer opens a separate browser tab to avoid pulling the user away from the site.

## Home Page

- The homepage has a carousel featuring three libraries and book images with a quote on each of the images. 

![carousel](https://res.cloudinary.com/dne60wscn/image/upload/v1684098290/static/readme%20images/carousel_rr241g.jpg)

### About the club section

- In this section there are three font awesome icons with the information for users to join, like a propose books. Each icon has a line of information and a button with a link to the correct section. 

![icons](https://res.cloudinary.com/dne60wscn/image/upload/v1684098290/static/readme%20images/iconsection_wem0qm.jpg)

### Featurette

- Within this space, you will discover an image accompanied by a thoughtful description that captures the essence and purpose of the club. 

![featurette](https://res.cloudinary.com/dne60wscn/image/upload/v1684098290/static/readme%20images/featurette_og1wh8.jpg)

## Books page 

- This page displays the book of the month at the top. A card the book image, title, except and the author's name. It also includes a Read more button that takes the user to the full description of the book. 
- The book cards are paginated after every 6 books. 
- Each card displays the book's image, title, excerpt and Author, as well as the read more button. 
- Clicking on the button will take the user directly to that book's detailed page.

![books](https://res.cloudinary.com/dne60wscn/image/upload/v1684098290/static/readme%20images/bookspage_feq03f.jpg)

**Sign Up**
 ![signup](https://res.cloudinary.com/dne60wscn/image/upload/v1684098289/static/readme%20images/singup_fsyeif.jpg)


**Log In**

![login](https://res.cloudinary.com/dne60wscn/image/upload/v1684098290/static/readme%20images/login_zu6zcw.jpg)

**Log Out**
# img

![signout]

- The Sign up, Log in, and Log out functionality was implemented using Django allauth. This authentication package was integrated into the project, enabling seamless user registration, login, and logout processes.

- To enhance the user experience, success messages were incorporated to provide immediate feedback when users successfully log in or log out

## Books detail page

- The book detail section displays the book cover image, author, title, and full book description.
- It also display a heart with a number where the user can like a book. Also there are bubble speachs with a number to show if the book has any comment. 

## Comment Section

- The comments section lists all comments left by users for that particular book.
- Comments can only be left if a user is logged in. Any comments left by the user must be first approved by the admin. Once approved th comment will show on the book detail page.

![comments]

## Add Book Form
# img

### Edit Book Form

# img

-  Only a logged in user can choose to edit a book they uploaded and showing in their "My Books" page. This is done by clicking the edit button on the book card. 
- The form opens with all fields populated with the original content.
- If a user tries to edit a book (by changing the url) without being signed in they are redirected to the log in page.

### Delete Recipe

 ![deletebook](https://res.cloudinary.com/dne60wscn/image/upload/v1684100192/static/readme%20images/delet4ebook_ke4jyp.jpg)

- Only a logged in user can choose to delete a book they uploaded and showing in their "My Books" page. This is done by clicking the edit button on the book card. 
- The user is asked to confirm if they wish to delete the book or cancel.

### Vote question


### Vote choices

![vote-choices](https://res.cloudinary.com/dne60wscn/image/upload/v1684100161/static/readme%20images/vote_rffnew.jpg)

### Vote results

![vote-results](https://res.cloudinary.com/dne60wscn/image/upload/v1684100161/static/readme%20images/results_lhy6sb.jpg)

    