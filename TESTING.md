# Table of Contents

- [Validator Testing](#validator-testing)
  * [HTML](#html)
    + [Fixed Errors](#fixed-errors)
    + [Unfixed Errors](#unfixed-errors)
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
| Home         	|            	|           	|
| Books        	|            	|           	|
| Book_detail  	|            	|           	|
| add_book     	| N/A        	|           	|
| edit_book    	| N/A        	|           	|
| delete_book  	| N/A        	|           	|
| my_books     	| N/A        	|           	|
| poll/index   	| N/A        	|           	|
| poll_detail  	| N/A        	|           	|
| poll_results 	| N/A        	|           	|
| login        	|            	|           	|
| logout       	|            	|           	|
| signup       	|            	|           	|
| 400          	|            	|           	|
| 403          	|            	|           	|
| 404          	|            	|           	|
| 500          	|            	|           	|


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

###  Add Book Page

###  Edit Book Page

###  Delete Book Page
