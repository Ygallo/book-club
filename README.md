
# Page Turner Book Club

Page Turner Book Club is a dynamic app designed exclusively for book enthusiasts, providing them with a platform to discover new books and share their recommendations. It caters to individuals who have a genuine passion for reading and enjoy engaging in discussions and commentary surrounding books. One of the key features of Page Turner Book Club is its monthly poll, allowing users to vote on book titles to determine the next book for discussion. Additionally, users are encouraged to leave comments and participate in conversations, fostering a vibrant community of like-minded readers. 

The live link here - [Page Turner Book Club](https://page-turner-bookclub.herokuapp.com/)

![PageTurner](https://res.cloudinary.com/dne60wscn/image/upload/v1685005091/static/readme%20images/responsive_qrsrjz.jpg)

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
    + [Books detail](#books-detail)
* [User Account Pages](#user-account-pages)
    + [My Books](#my-books)
    + [Add Books](#add-book-form)
    + [Edit Book](#edit-book-form)
    + [Delete Book](#delete-book)
    + [Vote Question](#vote-question)
    + [Vote Choices](#vote-choices)
    + [Vote Results](#Vote-results)
    + [Pending Features](#future-features)
  * [Deployment - Heroku](#deployment---heroku)
  * [Cloning this repository](#cloning-this-repository)
  * [Languages](#languages)
  * [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  * [Credits](#credits)
  * [Acknowledgments](#acknowledgments)

## User Experience (UX)

A visitor of the Page Turner Book Club would be someone who is an avid reader and is looking to be part of like-minded people group where he can discuss, recommend and find new reading interests.

### User Stories

#### User Profile
- As a User, I can register an Account so that so I can join a book club and connect with other readers.
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

The following user stories were left out of the project due to time constraints and labeled as "Won't Have" on the project board on GitHub. It is intended for these user stories to be implemented at a later date. 

- As a Site User I can filter books by genre so that I can find the ones I am more interested in.
- As a Site User I can see a list of upcoming book club meetings and events so that I can plan a reading schedule accordingly.

- As a Site Admin I can schedule and manage events/meetings so that members can easily RSVP and keep track of upcoming events.
- As a Site Admin I can send out reminders and notifications about upcoming meetings/events so that everyone stays up to date with events/meetings.
- As a Site Admin I can send an automatic Zoom meeting link to members so that they can easily connect with members on the monthly discussion.

## Design

The book club website embraces a simple and clean design approach, intentionally chosen to align with its core objective of fostering a tranquil experience for users. The objective is to maintain a cohesive color scheme across the website, promoting a harmonious and relaxing aesthetic.

### Colour Scheme
Color palette from Colormind

![colormind](https://res.cloudinary.com/dne60wscn/image/upload/v1684098289/static/readme%20images/Colormind-pageturner_brcmmp.jpg)

The website color scheme primarily features a soft and gentle pale yellow for the backgrounds while employing a darker yellow for accents. The navigation bar adopts a sophisticated and subdued dark grey-blue tone, while the footer has a vibrant touch of orange.

These carefully selected colors create a harmonious and neutral ambiance, while simultaneously offering distinct contrasts that add visual interest to the design.

#### Imagery
There are only a few static images on the site's main page. Three big images for the carousel and one smaller one at the bottom for the featurette.  The rest of the imagery will be uploaded by users or the admin when adding books to the club. 

#### Fonts
Open Sans imported via Google Fonts is the main font used for the website.  Sans Serif is the fallback font.

#### Wireframe 

The project began with a manual wireframe sketch, serving as the initial foundation from which it evolved. This initial wireframe provided a starting point, allowing for a visual representation of the project's structure and layout. 

![wireframe](https://res.cloudinary.com/dne60wscn/image/upload/v1684238232/static/readme%20images/wireframe_bcghih.jpg)

## Agile Methodology 

GitHub projects were used to manage the development process using an agile approach. Please see a link to the project board [here](https://github.com/users/Ygallo/projects/3)

## Data Model

Throughout the project, I applied the principles of Object-Oriented Programming (OOP), leveraging the power of Django's Class-Based Generic Views. 

Django AllAuth was used for the user authentication system.

For the users/ admin to add books to the club a model was required. **User** entity represents the registered users of the website, who can add books, like, comment and participate in discussions. Each user has a unique ID, name, email, and password.

**Book** entity represents the collection of books that the book club members can read and discuss. Each book has a unique ID, title, author, image, description, and genre among others.

The **Comment** model allows users to comment on individual books. The Book is a foreign key in the comment model commented can only be linked to one book. 

The **Question** model represents a poll created to vote on the proposed books.
The **Choice** model represents the book choices the members will vote on. This is a ForeingKey as the choices will be taken from the books on the club.

The **Vote** represents a poll (question) created to vote on the proposed books.

The **Book of the Month** is the Model that will display the book the club is reading for the current month.

The diagram below details the database schema.

![datamodel](https://res.cloudinary.com/dne60wscn/image/upload/v1684098289/static/readme%20images/data-model_hedufr.jpg)


## Testing

Testing and results can be found [here](https://github.com/Ygallo/book-club/blob/main/TESTING.md)

## Security Features and Defensive Design

### User Authentication
The login_required decorator is used to ensure only logged in users can vote on the monthly book poll and non-authenticated users are redirected to the login page.

### Database Security

To enhance security, I implemented specific measures in the project. Firstly, I ensured that sensitive information like the database URL and secret key was stored in the env.py file and that the env.py file is included in my gitignore file. By keeping these details separate and preventing them from being pushed to Github during the initial setup, I minimized the risk of unauthorized access or unwanted connections to the database.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

### Custom error pages:

Custom error pages were meticulously designed and implemented to provide users with comprehensive information when encountering errors and to guide them seamlessly back to the site. 

![error](https://res.cloudinary.com/dne60wscn/image/upload/v1684152882/static/readme%20images/404_er7mvj.jpg)

- 400 Bad Request - Page Turner Book Club is unable to handle this request.
- 403 Page Forbidden - The page you are trying to access has forbidden content.
- 404 Page Not Found - Oh no! Whatever book you are lookin for doesn't seem to exist.
- 500 Server Error - Oh no! Something just isn't right. Please come back later.


## Features

## Header

![header](https://res.cloudinary.com/dne60wscn/image/upload/v1684238829/static/readme%20images/navbar1_vnd5tf.jpg)

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

![icons](https://res.cloudinary.com/dne60wscn/image/upload/v1684433780/static/readme%20images/iconsection_p1t8ae.jpg)

### Featurette

- Within this space, you will discover an image accompanied by a thoughtful description that captures the essence and purpose of the club. 

![featurette](https://res.cloudinary.com/dne60wscn/image/upload/v1684433773/static/readme%20images/featurette_ixguki.jpg)

## Books page 

- This page displays the book of the month at the top. A card the book image, title, except and the author's name. It also includes a Read more button that takes the user to the full description of the book. 
- The book cards are paginated after every 6 books. 
- Each card displays the book's image, title, excerpt and Author, as well as the read more button. 
- Clicking on the button will take the user directly to that book's detailed page.

![books](https://res.cloudinary.com/dne60wscn/image/upload/v1684098290/static/readme%20images/bookspage_feq03f.jpg)

## Books detail page

- The book detail section displays the book cover image, author, title, and full book description.
- It also displays a heart with a number next to it where the user can like a book. Also there are bubble speeches with a number to show if the book has any comments. 

![book_detail](https://res.cloudinary.com/dne60wscn/image/upload/v1684858252/static/readme%20images/booksdetail_guwt8m.jpg)


## Comment Section

- The comments section lists all comments left by users for that particular book.
- Comments can only be left if a user is logged in. Any comments left by the user must be first approved by the admin. Once approved th comment will show on the book detail page.

![comments](https://res.cloudinary.com/dne60wscn/image/upload/v1684858273/static/readme%20images/comments_tk7cuz.jpg)



## User Account Pages

**Sign Up**
 ![signup](https://res.cloudinary.com/dne60wscn/image/upload/v1684098289/static/readme%20images/singup_fsyeif.jpg)


**Log In**

![login](https://res.cloudinary.com/dne60wscn/image/upload/v1684098290/static/readme%20images/login_zu6zcw.jpg)

**Log Out**

![signout](https://res.cloudinary.com/dne60wscn/image/upload/v1684239900/static/readme%20images/signout_f4fj9t.jpg)

- The Signup, Login, and Log out functionality was implemented using Django allauth. This authentication package was integrated into the project, enabling seamless user registration, login, and logout processes.

- To enhance the user experience, success messages were incorporated to provide immediate feedback when users successfully log in or log out


## My Book

- Once the user is logged in, they will be displayed on this view if it has uploaded any books. From here they have the option to edit or delete the books uploaded.

![my_books](https://res.cloudinary.com/dne60wscn/image/upload/v1684856399/static/readme%20images/mybooks_v7y73j.jpg)

## Add Book Form

- If the user is logged in, then they can add a book by clicking on Add Book in the navigation bar.
- The form will be displayed with the required fields for the books's Title, Slug, Author, and Description, failing to complete them will render a message stating which fields you have missed.
- The field for the genre is a required field with a dropdown with different book genres, but it has a default blank option. 
- The image field also has a default image to display as the book cover. in case the user do not upload a cover.
- The form fields for 'Description' include a WYSIWYG editor called Summernote to help the user format their content.

![Addbook](https://res.cloudinary.com/dne60wscn/image/upload/v1685128054/static/readme%20images/addbook_n7xbsf.jpg)

### Edit Book Form

![editbook](https://res.cloudinary.com/dne60wscn/image/upload/v1685128408/static/readme%20images/editbook1_pvyehs.jpg)

-  Only a logged-in user can choose to edit a book they uploaded and showing in their "My Books" page. This is done by clicking the edit button on the book card. 
- The form opens with all fields populated with the original content.
- If a user tries to edit a book (by changing the URL) without being signed in they are redirected to the login page.

### Delete Book

 ![deletebook](https://res.cloudinary.com/dne60wscn/image/upload/v1684100192/static/readme%20images/delet4ebook_ke4jyp.jpg)

- Only a logged-in user can choose to delete a book they uploaded and showing on their "My Books" page. This is done by clicking the edit button on the book card. 
- The user is asked to confirm if they wish to delete the book or cancel.

### Vote question

- The vote question will only display the last poll title available for the coming month. 
- The user has the option to click on the **vote now** button to see the book options for the vote, or to click on **results** to see the results up to the moment.

![poll-question](https://res.cloudinary.com/dne60wscn/image/upload/v1684856757/static/readme%20images/pollquestion_wwdury.jpg)

### Vote choices

- The vote Choices will display the books up for a vote. A card with 3 books each with its Cover, Title, Author, and a **Vote for this book** button will be shown to the user.
- The User will need to select one option and then confirm the selection by clicking on Vote.
- If the user tries to vote for a second time a message will appear to inform the *they have already voted on this question*. 
- If a user tries to access the vote (by changing the URL) without being signed in they are redirected to the login page.

![vote-choices](https://res.cloudinary.com/dne60wscn/image/upload/v1684856677/static/readme%20images/pollvote_v3t89z.jpg)

### Vote results

 - The Results page will show the current results for the monthly poll. A book cover thumbnail with the title and author will display the number of votes for each book.

![vote-results](https://res.cloudinary.com/dne60wscn/image/upload/v1684100161/static/readme%20images/results_lhy6sb.jpg)


### Pending Features

- Add a filter option when accessing the books page, so the users can filter books by the different genres.
- Add a calendar for the user to see when signed in with the time and date of the monthly book discussion. 
- Send automatic invitations to the users and reminders with a link to connect to the meeting. 

## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
- Logged in to [Heroku](https://dashboard.heroku.com/apps).
- On the main page clicked the button labeled **New** in the top right corner and from the drop-down menu select **"Create New App"**.
- Entered the chosen app name.
- Next select the region.
- Clicked on the **Create App** button.

### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file:
- In my GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py
- Add the cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files / directories
- Create requirements.txt file
- Create  directories in the main directory for static and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi

### Update Heroku Config Vars
Add the following Config Vars in Heroku:
- SECRET_KEY value 
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and clicked Enable Automatic Deploys. Every push to main will deploy a new version of this app. Deploys happen automatically.

The site is now live and operational.

## Cloning this repository
- Locate the repository at this link [Page Turner Book Club](https://github.com/Ygallo/book-club).
- Above the list of files, click on the green button with the word: Code. 
- Copy the URL for the repository using HTTPS.
- Open the Terminal
- Change the current working directory to the location where you want the cloned directory.
- Type **git clone**, and then paste the URL copied earlier.
- Press **Enter** to create your local clone.

## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks - Libraries - Programs Used
- [Django](https://www.djangoproject.com/)
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [PostgreSQL](https://www.postgresql.org/)
- [Heroku](https://dashboard.heroku.com/login)
- [Responsive](https://ui.dev/amiresponsive) - Used to verify responsiveness of website on different devices.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
- [Font Awesome](https://fontawesome.com/) 
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/)
- [W3C](https://www.w3.org/) 
- [PEP8 Online](http://pep8online.com/) 
- [Jshint](https://jshint.com/)
- [Colormind](http://colormind.io/bootstrap/)
- [Favicon](https://favicon.io/)
- [Lucidchart](https://lucid.app/documents#/dashboard) - to create the database design
- [Grammerly](https://app.grammarly.com/) - for proof reading the README.md
- [Summernote](https://summernote.org/)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) 
- [Cloudinary](https://cloudinary.com/): for hosting the uploaded images.
- [Bootstrap 5](https://getbootstrap.com/)
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to convert excel testing tables to markdown
- [Javascript alert message](https://stackoverflow.com/questions/23101966/bootstrap-alert-auto-close)

## Credits

- [W3Schools](https://www.w3schools.com/)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Pexels](https://www.pexels.com/): All imagery on the site was sourced from Pexels.com
- [Pixabay](https://pixabay.com/): for more images.
- [Update View](https://pytutorial.com/django-updateview-example)
- [Pagination](https://docs.djangoproject.com/en/2.2/topics/pagination/#using-paginator-in-a-view)
- [@login required](https://docs.djangoproject.com/en/4.2/topics/auth/default/)
- [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog)
- [Poll](https://medium.com/analytics-vidhya/building-a-simple-poll-system-in-django-part-i-a0bfb4fc3699)
- [Another Poll](https://prettyprinted.com/tutorials/creating-a-poll-app-in-django/)
- [More polls](https://www.geeksforgeeks.org/voting-system-project-using-django-framework/)
- [The Gloss Book Club](https://theglossbookclub.com/): for inspirations and a few frases.
- [Success deleted message](https://www.pythontutorial.net/django-tutorial/django-deleteview/)
- [Success deleted message - Stackoverflow](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown)

## Acknowledgments

I would like to thanks my Mentor, Andre Aquilina who supported my project idea and help me on my vote model that was missing one final twist to work as intended. 

I am fortunate to have the unwavering support and invaluable feedback of my husband throughout this project. His continuous encouragement and guidance have been instrumental in my progress and success.
