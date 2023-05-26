# Table of Contents

- [Validator Testing](#validator-testing)
  * [HTML](#html)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
  * [Site Navigation](#site-navigation)
  * [Home Page](#home-page)
  * [Books Page](#book-page)
  * [Book Detail Page](#book-detail-page)
  * [My Books Page](#my-Books-page)
  * [Add Book Page](#add-book-page)
  * [Edit Book Page](#edit-book-page)
  * [Delete Book Page](#delete-book-page)
  * [Vote- Question](#poll-index-page)
  * [Vote- Choices](#poll-detail-page)
  * [Vote- Results](#poll-results-pages)
- [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)
 
    + [Required fields using Summernote extension submit with just whitespace entered](#required-fields-using-summernote-extension-submit-with-just-whitespace-entered)

    ## Validator Testing

### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.
  
| Page         	| Logged out 	| Logged in 	|
|--------------	|------------	|-----------	|
| Home         	| No errors   | No errors   |
| Books        	| No errors   | No errors   |  
| Book_detail  	| No errors         	
| add_book     	| N/A        	| No errors   |  
| edit_book    	| N/A        	| No errors   |
| delete_book  	| N/A        	| No errors   |          	
| my_books     	| N/A        	| No errors   |
| poll/index   	| N/A        	|   Note 1    |
| poll/detail  	| N/A        	| No errors   |
| poll/results 	| N/A        	| No Erorrs   |
| login        	| No errors   | N/A         |       	
| logout       	| N/A         |	No errors   |
| signup       	| No errors   | N/A         |           	
| 400          	| No errors   | No errors   |        	
| 403          	| No errors   | No errors   |       
| 404          	| No errors   | No errors   |         	
| 500          	| No errors   | No errors   |   

#### Note 1: poll/index Errors
When the poll/index page was run through the validator, 3 errors appeared: 
- **Missing main tag**: Both tags are present on the HTML source on the base page, they contain the block content for the other templates.
- **Unclosed element div**: All divs are closed on the original index/poll code. The first div (card) opens in line 4 and closes in line 26. The second div (card-body) opens in line 8 and closes in line 25. Since the errors encountered were not within my codebase, I regrettably could not rectify them. As a result, these errors remain unresolved.


### CSS
No errors were found when passing my CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

### Javascript
No errors were found when passing my javascript through [Jshint](https://jshint.com/)

![jshint](https://res.cloudinary.com/dne60wscn/image/upload/v1684260332/static/images/jshint_elkf9i.jpg)

### Python
All Python files were run through [Pep8](https://pep8ci.herokuapp.com/) with no errors found. 

## Lighthouse

| Page         	| Performance 	| Accessibility 	| Best Practise 	| SEO 	|
|--------------	|-------------	|---------------	|---------------	|-----	|
| Home         	| 73          	| 100           	| 92            	| 100 	|
| Books        	| 99          	| 96            	| 92            	| 90  	|
| book_detail  	| 99          	| 97            	| 92            	| 100 	|
| add_book     	| 98          	| 100           	| 100           	| 100 	|
| edit_book    	| 99          	| 98            	| 100           	| 100 	|
| delete_book  	| 100         	| 100           	| 100           	| 100 	|
| my_books     	| 93          	| 98            	| 100           	| 90  	|
| poll/index   	| 99          	| 100           	| 100           	| 100 	|
| poll/details 	| 85          	| 100           	| 100           	| 100 	|
| poll/results 	| 97          	| 100           	| 100           	| 100 	|
| login        	| 99          	| 100           	| 92            	| 100 	|
| logout       	| 99          	| 100           	| 92            	| 100 	|
| signup       	| 99          	| 100           	| 92            	| 100 	|

## Browser Testing
- The Website was tested on Google Chrome. Microsoft Edge and Firefox  browsers with no issues noted.

## Device Testing
The responsive design was checked using Chrome developer tools across multiple devices with structural integrity holding for the various sizes. The website was also viewed on different devices such as Desktop, Laptop, Google S6 and Samsung phone to ensure responsiveness on various screen sizes. The results where as intended. 

## Manual Testing

### Site Navigation


| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| NavBar                |            |                                                                    |           |
| Site Name             | Click      | Redirect to home                                                   | Pass      |
| Home Link             | Click      | Redirect to home                                                   | Pass      |
| Books Link            | Click      | Open Books Page                                                    | Pass      |
| Account Dropdown      | Click      | Open dropdown menu                                                 | Pass      |
| Vote Link             | Click      | Only visible if user in session                                    | Pass      |
| Add Books Link        | Click      | Only visibl if user in session                                     | Pass      |
| My Books Link         | Display    | Only visible if user in session                                    | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                  | Pass      |
| Sign Up Link          | Click      | Redirect to sign up page                                           | Pass      |
| Log In Link           | Click      | Open Login page                                                    | Pass      |
| Log In Link           | Click      | Redirect to log in page                                            | Pass      |
| Logout Link           | Click      | Open logout confirm page                                           | Pass      |
| All Nav Links         | Hover      | text changes color to pink - logout is higlighted                  | Pass      |

### Home Page

| Element                    	| Action 	| Expected Result        	| Pass/Fail 	|
|----------------------------	|--------	|------------------------	|-----------	|
| Carousel                   	| Click  	| Change Image           	| Pass      	|
| Carousel indicators        	| Click  	| Change Image           	| Pass      	|
| Book - View details        	| Click  	| Redirect to books page 	| Pass      	|
| Join - View details        	| Click  	| Redirect to sing up    	| Pass      	|
| Participate - View details 	| Click  	| Redirect to log in     	| Pass      	|

### Footer

| Element        	| Action 	| Expected Result                             	| Pass/Fail 	|
|----------------	|--------	|---------------------------------------------	|-----------	|
| Facebook icon  	| Click  	| Redirect to Facebook page opens on new tab  	| Pass      	|
| Instagram icon 	| Click  	| Redirect to Instagram page opens on new tab 	| Pass      	|
| Twitter icon   	| Click  	| Redirect to Twitter page opens on new tab   	| Pass      	|


### Books Page

| Element        	| Action 	| Expected Result                             	| Pass/Fail 	|
|----------------	|--------	|---------------------------------------------	|-----------	|
| Facebook icon  	| Click  	| Redirect to Facebook page opens on new tab  	| Pass      	|
| Instagram icon 	| Click  	| Redirect to Instagram page opens on new tab 	| Pass      	|
| Twitter icon   	| Click  	| Redirect to Twitter page opens on new tab   	| Pass      	|

### Books  Details Page

| Element                             	| Action  	| Expected Result                                         	| Pass/Fail 	|
|-------------------------------------	|---------	|---------------------------------------------------------	|-----------	|
| Book detail - heart (logged in)     	| Click   	| Clicking the outlined heart changes it to a solid heart 	| Pass      	|
| Book detail - heart (logged in)     	| Click   	| Clicking on the solid heart changes to outline          	| Pass      	|
| Comment - submit button (logged in) 	| Click   	| Submits the user's comment                              	| Pass      	|
| Comment - submit button (logged in) 	| Display 	| Your comment is awaiting approval                       	| Pass      	|

### Vote - Index Page

| Element         	| Action  	| Expected Result          	| Pass/Fail 	|
|-----------------	|---------	|--------------------------	|-----------	|
| Vote now button 	| Click   	| Redirect to Choices Page 	| Pass      	|
| Results button  	| Click   	| Redirect to results Page 	| Pass      	|

### Vote - Details Page

| Element            	| Action  	| Expected Result                                                	| Pass/Fail 	|
|--------------------	|---------	|----------------------------------------------------------------	|-----------	|
| Vote for this book 	| Click   	| Select voting book choice                                      	| Pass      	|
| Vote               	| Click   	| Submites the vote                                              	| Pass      	|
| Vote               	| Click   	| If already voted, message alerting the user that already voted 	| Pass      	|
| Back to polls      	| Click   	| Redirects to Vote -Index page                                  	| Pass      	|

### Vote - Results Page

| Element       	| Action  	| Expected Result                                                	| Pass/Fail 	|
|---------------	|---------	|----------------------------------------------------------------	|-----------	|
| Back to polls 	| Click   	| Redirects to Vote -Index page                                  	| Pass      	|                                           	| Pass/Fail 	|


###  My Books Page

| Element       	| Action  	| Expected Result                	| Pass/Fail 	|
|---------------	|---------	|--------------------------------	|-----------	|
| More button   	| Click   	| Redirects to Book details page 	| Pass      	|
| Edit button   	| Click   	| Redirects to Edit form         	| Pass      	|
| Delete Button 	| Click   	| Redirects to confirm deletion  	| Pass      	|

###  Add Book Page

| Element                       	| Action      	| Expected Result                                	| Pass/Fail 	|
|-------------------------------	|-------------	|------------------------------------------------	|-----------	|
| Form Text Input (if required) 	| Leave blank 	| Form won't submit                              	| Pass      	|
| Genre dropdown                	| Click       	| Display a drop down with the genre option      	| Pass      	|
| Genre dropdown                	| Leave blank 	| "Blank" by default - will allow form submition 	| Pass      	|
| Form image select button      	| Click       	| Open device storage                            	| Pass      	|
| Form image select button      	| Display     	| Chosen image name displayed once selected      	| Pass      	|
| Form image select button      	| Click       	| Default image is used if no image is selected  	| Pass      	|
| Submit button(form valid)     	| Click       	| Form submit                                    	|           	|

###  Edit Book Page
| Element      	| Action 	| Expected Result                     	| Pass/Fail 	|
|--------------	|--------	|-------------------------------------	|-----------	|
| Save button  	| Click  	| User is redirected to My Books page 	| Pass      	|

###  Delete Book Page
| Element        	| Action 	| Expected Result                     	| Pass/Fail 	|
|----------------	|--------	|-------------------------------------	|-----------	|
| Delete button  	| Click  	| User is redirected to My Books page 	| Pass      	|
| Cancel button  	| Click  	| User is redirected to My Books Page 	| Pass      	|

### Django All Auth Pages

### Django All Auth Pages
| Element                    | Action                                    | Expected Result                            | Pass/Fail |
|----------------------------|-------------------------------------------|--------------------------------------------|-----------|
| Sign Up                    |                                           |                                            |           |
| Log in link                | Click                                     | Redirect to login page                     | Pass      |
| Username field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Username field             | Leave empty                               | Error message displays                     | Pass      |
| Username field             | Insert correct format: numbers            | On submit: form submit                     | Pass      |
| Username field             | Insert duplicate username                 | On submit: form won't submit               | Pass      |
| Username field             | Insert duplicate username                 | Error message displays                     | Pass      |
| Email field                | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Email field                | Insert incorrect format                   | Error message displays                     | Pass      |
| Email field                | Insert correct format                     | On submit: form submit                     | Pass      |
| Email field                | Leave empty                               | On submit: form submit                     | Pass      |
| Email field                | Insert duplicate email                    | On submit: form won't submit               | Pass      |
| Email field                | Insert duplicate email                    | Error message displays                     | Pass      |
| Password field             | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Password field             | Insert incorrect format                   | Error message displays                     | Pass      |
| Password field             | Passwords don't match                     | On submit: form won't submit               | Pass      |
| Password field             | Passwords don't match                     | Error message displays                     | Pass      |
| Password field             | Insert correct format and passwords match | On submit: form submit                     | Pass      |
| Sign Up button(form valid) | Click                                     | Form submit                                | Pass      |
| Sign Up button(form valid) | Click                                     | Redirect to home page                      | Pass      |
| Sign Up button(form valid) | Click                                     | Success message confirming login appears   | Pass      |
| Sign Up button(form valid) | Click                                     | Success message fades after 3 seconds      | Pass      |
|                            |                                           |                                            |           |
| Log in                     |                                           |                                            |           |
| Sign up link               | Click                                     | Redirect to sign up page                   | Pass      |
| Username field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Username field             | Insert wrong username                     | On submit: form won't submit               | Pass      |
| Username field             | Insert wrong username                     | Error message displays                     | Pass      |
| Password field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Password field             | Leave empty                               | Error message displays                     | Pass      |
| Password field             | Insert wrong password                     | On submit: form won't submit               | Pass      |
| Password field             | Insert wrong password                     | Error message displays                     | Pass      |
| Login button(form valid)   | Click                                     | Form submit                                | Pass      |
| Login button(form valid)   | Click                                     | Redirect to home page                      | Pass      |
| Login button(form valid)   | Click                                     | Success message confirming login appears   | Pass      |
| Login button(form valid)   | Click                                     | Success message fades after 3 seconds      | Pass      |
|                            |                                           |                                            |           |
| Log Out                    |                                           |                                            |           |
| Logout button              | Click                                     | Redirect to homepage                       | Pass      |
| Logout button              | Click                                     | Success message confirming log out appears | Pass      |
| Logout button              | Click                                     | Success message fades after 3 seconds      | Pass      |

## Trouble shooting

- **Bug**:  On deploying>  heroku error: missing required flag: -a, --app app - wrong name - appname instead of project name. 
- **Fix**: by updating Requirements.txt 

- **Bug**: Forms not working.
- **Fix**: updated Crispy Bootstrap 4 to Crispy Bootstrap 5.

- **Bug**: style sheet not updating.
- **Fix**: solved until deployment by adding **?{% now "U" %}** to the end of the href. When the project was deployed for submission, the style sheet was not working on the deployed app. The solution was to remove **?{% now "U" %}** and upload the stylesheet to Cloudinary

## Unfixed bugs

-CSS style file stopped updating mid project, after hard reloading still would not upload changes, I added this code {% now "U" %} from  [Stack overflow](https://stackoverflow.com/questions/52682812/django-css-not-updating). This allowed my to keep working until deployment, but once deployed css was not loading at all. Finally uploaded the css to cloudinary and the styles load on the deployed page. This is not ideal as every change on css means I have to upload a new file but works until a better solution is reach.