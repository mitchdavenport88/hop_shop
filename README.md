# Family Feasts

### Milestone Project Four
Over the past couple of years the UK has had a craft beer boom with its popularity never being higher. The market for craft beers is now a saturated, highly competitive one with new breweries and retailers specialising in it appearing all the time. As demand grows, tastes change and the fact that consumers now expect a greater variety of choice has made bottle shops very popular.

The Hop Shop is an e-commerce store that is tapping into this demand. They'll offer numerous types of beers from all over Europe to be purchased conveniently, all from one place satisfying the everyday beer aficionado. 

## Demo
The live site can be viewed here - [The Hop Shop](https://hop-shop.herokuapp.com/).

GitHub repository can be viewed here - [mitchdavenport88/hop_shop](https://github.com/mitchdavenport88/hop_shop).

![Site Mockup](readme-docs/screenshots/am-i-responsive2.jpg)

## UX
<!-- ### Strategy -->

### User Stories
As a shopper I'd like to:
* View a selection of products and select those I wish to purchase.
* Look at individual product details in order to consolidate my decision on whether to purchase the item or not.
* Filter products based on their type or where they originate from.
* Sort products by price, strength or size.
* To search for products by using keywords.
* Add items to the cart to purchase a later point.
* Easily view the carts contents and the number of items within it.
* Be given the ability to amend the quantity of items within the cart or remove items completely.
* Be rewarded with free delivery if I’m buying a decent amount of products.
* Checkout, pay and complete my order easily.
* Have order confirmation once my order has been completed.
* Navigate around the site easily and the site to be user friendly.
* Receive feedback whilst interacting with the site.
* Do all of the above regardless of what device I’m using.

As a returning user I'd like:
* To sign up and register for an account easily. 
* To login and logout easily.
* To receive email confirmation of registration and have the ability to recover forgotten passwords.
* A personalised user profile where I can see my order history and set my default delivery information if desired.
* Access to a wishlist where favourites can be added / removed so I can easily purchase them at a later date.
* To read beer related articles as I’m a regular consumer of beer and I’d find a blog of interest.
* The ability to comment and interact with other users on the blog posts.

As the site owner / admin I want:
* The ability to add new products to the store.
* To be able to edit and remove products from the store.
* The ability to create and post new articles to the blog.
* To be able to edit and remove existing posts from the blog.

<!-- ### Scope - functionality -->

<!-- ### Scope - content -->

<!-- ### Structure -->

### Skeleton
Home - [desktop](readme-docs/wireframes/home(desktop).png) | 
[tablet](readme-docs/wireframes/home(tablet).png) | 
[mobile](readme-docs/wireframes/home(phone).png).

Products - [desktop](readme-docs/wireframes/products(desktop).png) | 
[tablet](readme-docs/wireframes/products(tablet).png) | 
[mobile](readme-docs/wireframes/products(phone).png).

Product detail - [desktop](readme-docs/wireframes/product-detail(desktop).png) | 
[tablet](readme-docs/wireframes/product-detail(tablet).png) | 
[mobile](readme-docs/wireframes/product-detail(phone).png).

Add / edit product - [desktop](readme-docs/wireframes/edit-add-product(desktop).png) | 
[tablet](readme-docs/wireframes/edit-add-product(tablet).png) | 
[mobile](readme-docs/wireframes/edit-add-product(phone).png).

Cart - [desktop](readme-docs/wireframes/cart(desktop).png) | 
[tablet](readme-docs/wireframes/cart(tablet).png) | 
[mobile](readme-docs/wireframes/cart(phone).png).

Checkout - [desktop](readme-docs/wireframes/checkout(desktop).png) | 
[tablet](readme-docs/wireframes/checkout(tablet).png) | 
[mobile](readme-docs/wireframes/checkout(phone).png).

Checkout success - [desktop](readme-docs/wireframes/checkout-success(desktop).png) | 
[tablet](readme-docs/wireframes/checkout-success(tablet).png) | 
[mobile](readme-docs/wireframes/checkout-success(phone).png).

Profile - [desktop](readme-docs/wireframes/profile(desktop).png) | 
[tablet](readme-docs/wireframes/profile(tablet).png) | 
[mobile](readme-docs/wireframes/profile(phone).png).

Blog - [desktop](readme-docs/wireframes/blog(desktop).png) | 
[tablet](readme-docs/wireframes/blog(tablet).png) | 
[mobile](readme-docs/wireframes/blog(phone).png).

Blog post / article - [desktop](readme-docs/wireframes/blog-post(desktop).png) | 
[tablet](readme-docs/wireframes/blog-post(tablet).png) | 
[mobile](readme-docs/wireframes/blog-post(phone).png).

Wishlist - [desktop](readme-docs/wireframes/wishlist(desktop).png) | 
[tablet](readme-docs/wireframes/wishlist(tablet).png) | 
[mobile](readme-docs/wireframes/wishlist(phone).png).

Allauth templates - [desktop](readme-docs/wireframes/all-auth-template(desktop).png) | 
[tablet](readme-docs/wireframes/all-auth-template(tablet).png) | 
[mobile](readme-docs/wireframes/all-auth-template(phone).png).

### Surface
The Hop Shop is built using Bootstraps grid system. I’ve used a combination of containers, rows and columns along with the built in flexbox capabilities to position content as well as making each page responsive at all breakpoints. Another positive to using this grid system is that it’s allowed me to keep the layout of pages consistent throughout.

Pages have a similar layout of page title followed by its content. Some pages contain a lot of information (such as the product pages) so in order not to overpower the user with a lot of information at once products are displayed via cards. These cards show just the basic information and link to the individual product page. Where the use of cards wasn’t applicable (such as the individual product pages and pages that feature forms) I broke information up by using block colour and columns. Doing so ties in with the overall aesthetic of the site, adds some space between information and forms where appropriate whilst remaining visually appealing and responsive.

I found a suitable colour palette using [Coolors](https://coolors.co/). I found a suitable colour palette using Coolors. The scheme is a combination of Oxford Blue (#061A40) and Celadon Blue (#1A759F) that work well together, work well with white text and gives the site the professional, modern aesthetic I was after. I decided that buttons for adding, updating and checking out were to use Bootstraps success class as this green colour is more associated with actions of this type. For delete functions I used Bootstraps danger class for the same reasoning. The Google font Montserrat is used throughout. I used it for just the logo initially and it worked really well so I decided to use it everywhere else. I feel it works well with the colour scheme, fits in with the aesthetic created and more importantly it is easy to read.

![Coolors - color palette](readme-docs/screenshots/color-palette.jpg)