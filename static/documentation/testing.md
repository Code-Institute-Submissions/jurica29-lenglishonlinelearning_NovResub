## User Story testing

Issue No. | Title | Acceptance criteria | Manual test carried out
----------|-------|---------------------|-------------------------
#01 | Create home page with products display | As a Site User I can see and access all items so that I can decide what to purchase. | Ensure that site users can access all items with one click.
#02 | Create product detail page | As a shopper, I want to see product descriptions. As a shopper, I want to add products/items to my cart. | Ensure that customers can see product details and add products to the cart
#03 | Create order and payment pages | As a site user, I want to add/remove items to/from the cart. As a site user, I want to add my details. As a site user, I want to get a site feedback when adding/removing items or applying the purchase option. | Ensure that site user can add and remove items from the cart, add billing address details and get a site feedback via toasts.
#04 | Product management within admin section | As a site admin, I want to create, edit or delete items. | Ensure full CRUD ability for the admin of the site.
#05 | Site registration and login functionality | As a site user, I want to register on the website. As a site user, I want to login into the website. As a site user, I want to log out off the website. As a site user, I can verify my email address and get an email confirmation of my registration. | Ensure smooth register, login and logout procedures, as well as email verification once user signs up.
#06 | Create custom 404/500 pages | As a site owner, I want to redirect users to the custom 404/500 error pages. | Ensure that custom error page is displayed once error is encountered so that users can easily return to the home page.
#07 | Create order history page | As a site user, I want to access and see what I've ordered previously. | Ensure that user can see previous order details.
#08 | User reviews | As a site user, I want to create, edit and delete my reviews for all items. As a site admin, I want to limit reviews to only one per user. | Ensure that users/customers can submit, edit and delete reviews under each of the products/items.

* Manual testing was performed to ensure that website is fully working without any issues.

Each page has been manually tested to ensure that the links and the contents are properly placed and functioning, and that all data entry is appropriately handled as expected. 
Restricted areas access has also been thoroughly tested.

All buttons and links were manually tested to ensure full functionality across the website.

## Manual testing on each page
  
#### Home page

**Users who are logged in**  

Ensure that users can see their username in the navbar and that they can click sign out no matter where they are within the website.
All the links and buttons have been manually tested across various devices.

***Newsletter signup***

Ensure that users can see input their email address and subscribe with appropriate feedback.

#### Product Detail page

**For site visitor who has not logged in**

Ensure that site visitors cannot submit, edit or delete reviews.
Ensure that site visitors are redirected to sign in/sign up page once they want to add item to the cart.
Ensure that links for easing the access to "log in" and "register" areas are functioning properly in review section.

**For registered and logged in users**

Ensure that users have full CRUD functionality enabled for reviewing below posts.

#### Delete/Edit Review page

**For registered and logged in users**

Ensure that both buttons perform the willing functions, whether to submit the change or just to return to the previous page.

#### About page

**For both users and site visitors**

Ensure that both users and visitors can see all relevant information about the website.
Ensure that external link for Zoom is working fine.

#### Register page

Ensure that relevant messages are displayed in case of errors and that toasts are displayed in case of successful registration.

#### Sign in option

Ensure that upon successful login, the user is redirected to home page where they can see their username in the navbar.

#### Sign out page

Ensure that user gets feedback once signed out.

#### Cart summary page

Ensure that users add/remove items from the cart, continue shopping or proceed to the next stage of the checkout process.

#### Billing address page

Ensure that users need to input their billing address details or if available, to apply the coupon code for discount.

#### Checkout page

Ensure that users can submit payment and see the appropriate feedback message.
Ensure that users can be redirected to order history after the payment is completed.

#### Order history page

Ensure that users can see their past orders.