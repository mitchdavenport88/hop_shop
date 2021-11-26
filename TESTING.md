# Milestone Project Four - Testing

The live site can be viewed here - [The Hop Shop](https://hop-shop.herokuapp.com/).

[Back to README file.](README.md)

![Site Mockup](readme-docs/screenshots/am-i-responsive1.jpg)

## Testing
All my code has been put through the following:

* W3C HTML validation.
* CSS AutoPrefixer.
* W3C CSS validation.
* JSHint JavaScript validation.
* PEP8 online check.

## Functionality
### Manual Testing
These are the steps I went through testing my website and it's functionality.

**Navigation:**
1.	Checked the navigation bar remains at the top of the page at all times and is never hidden by any other content.
2.	Checked the banner at the top of the navigation bar always displays delivery information.
3.	Clicked The Hop Shop logo at varying points to make sure it’s a link back to the home page.
4.	Tested the search bar:
    * Checked that it’s centrally aligned and that the placeholder is visible.
    * Hovered over the search button (icon) to check that the hover class works.
    * Clicked the button to test what it does:
        * Loads the products page and shows products that match the search.
        * I checked that by submitting an empty search I get an error message telling me so.
5.  Checked that the three icons linking to the profile page, wishlist and cart appear to the right of the navigation bar.
    * Checked that they perform as expected for:
        * Unregistered users.
        * Registered users.
        * Admin.
    * Checked that all the hover classes work.
    * Checked that if there are any items in the shopping cart then the number of items will show on the cart icon.
6.	I’ve clicked on all the links to ensure they do what they're supposed to do.
    * Home and blog take me to the relevant pages.
    * All Beers, beers by style and beers by country links have an additional dropdown menu that displays the filtering options. 
    * Tested that the hover classes all work.
7.	Checked that at widths below 992px the navigation bar adapts to something more suited to smaller screen sizes. 
    * Seen that all links are now displayed via a dropdown (hamburger) menu only.
        * Toggled the menu icon button on and off to check it displays and hides the menu accordingly.
        * Clicked all links to test they work as before and as expected.
    * Checked that the search bar is now hidden and can only be accessed by toggling the magnifying glass icon that now appears alongside the other three icons on the right hand side of the navigation bar.
    * Seen that the delivery information in the top banner adapts accordingly.

**Footer:**
1.	Checked the footer sticks to the bottom of every page and never hides any content.
2.	Checked that the social links are always aligned centrally and that the hover classes work.
3.	Clicked on all icons in the footer to check that they open and do so in a new tab.

**Home:**
1.	Checked that the background image isn't pixelated, is positioned well and loads as intended.
2.	Checked the text overlay box appears and that the relevant text and button is visible within it.
    * Tested the call-to-action button and it sends us to the Bottle Shop as desired.
    * Checked the hover class on the button works.
    * Checked the overlay box and its contents are always justified and aligned centrally.
    * Checked that at widths below 992px only the Hop Shop logo and call-to-action buttons are visible.
3.	Checked that the four most recently added products to the store are displayed under the hero image as part of the ‘new in…’ section.
    * All products are shown as individual cards and are suitably displayed dependant of the breakpoint.
    * Tested the cards against the ***individual product card** test that’s shown below as part of the products test.

**Products:**
1.	Checked that all pages are titled Bottle Shop.
2.	Checked that all products load as expected.
3.	Checked that if a filter has been applied from the navigation that it’s taken effect.
    * Products should display in the order specified (if applicable).
    * Correct products are displayed according to which filter has been applied (if applicable).
4.	Seen that the sort by… dropdown menu loads and is positioned where intended, underneath the page title and to the right of the page.
    * Checked that this gets centralised on screen widths below 992px.
    * Checked that each selection applies the intended filter and that the cards below are displayed in order of what’s selected.
5. Checked that the cards are displayed as intended at varying breakpoints:
    * In four columns on screen widths above 1200px.
    * In three columns on screen widths between 992px and 1200px.
    * In two columns on screen widths between 768px and 992px.
    * In one column on screen widths below 768px.

**Individual product card test (test also conducted on other sections)**

Check that every card contains:
* A product image that adjusts dependant to screen width.
    * Checked that this image also links to the products details page.
    * Shows the products name.
    * Details the products type | percentage | origin.
        * Tested that the products type and origin names act as links to the products page and apply a filter to the results shown based upon the category clicked. 
    * Show the products price.
    * The add to cart button and quantity selector appear at the bottom.
        * See that a quantity is shown in the box (default number should be 1).
        * Test that the + and – buttons increase or decrease the number.
            * Checked that + gets disabled at 99.
            * Checked that - gets disabled at 1.
            * Tested that numbers outside this range can’t be added manually.
        * Pressed the add button to check that the correct quantity of the item has been added to the cart.
            * Seen that a toast message appears confirming this addition.
            * The toast shows a preview of the cart.
            * Checked the cart icon in the navigation bar updates accordingly.
            * Checked the correct number of items have been added to the cart.
        * Hovered over the buttons to check the hover classes work.
    * Checked that for registered users a heart icon appears in the top right of each card, on top of the image. This indicates that it can be added to / removed from the wishlist.
        * As a heart outline indicates the item is not on the list I tested that clicking it adds the item to the wishlist and then the icon appeared solid. 
        * As a solid heart indicates the item is already on the list I tested that clicking it removes the item from the wishlist and the icon is now an outline.
        * Seen that the hover class works.
        * Checked that the toast message appears confirming whether it’s been added or removed from the list.

**Product detail page:**
1. Checked that the correct product has been loaded.
2. Check that the products name and size is shown at the top of the page as the page’s title.
3. Checked that all relevant information has been loaded and is displayed as expected.
4. Check the card according to the *individual product card test shown in the products test above as the results and functions are similar.
    * Checked that the product description is displayed as well as all the other information specified in the test.
5. Checked that on screen widths of below 576px the card adapts with the products information now being displayed underneath the products image but still in a card format.
6. Seen that the appropriate buttons based on the user’s registration status appear below underneath the product information:
    * The Continue Shopping button appears for all users underneath the products card and this takes me back to the Bottle Shop.
    * See that the edit and delete buttons appear for admin only.
        * Checked the edit product button opens the edit product form.
        * Checked the delete product button triggers the deletion modal.
    * Checked that all hover classes work.

**Cart:**
1.	Checked that at the top of the page a banner informing the user how much more they need to spend to qualify for free delivery shows (if applicable).
    * Checked that if items in the cart equate to over £30 then the user is informed they’ve qualified for free delivery.
2.	Checked the page title also displays the current count of items in the cart.
3.	A Continue Shopping button appears underneath the title taking users back to the Bottle Shop.
4.	Checked that if the cart is empty a message relaying this appears.
    * Seen that the page title reads just ‘My Cart’.
5.	Checked that if items do exist in the cart then each individual item line has its own row with the following details:
    * Image (this gets hidden below 768px).
        * Checked this links back to individual product page.
    * Product info should always be displayed.
        * Checked the title links back to individual product page.
    * Quantity adjustment buttons, quantity and the update and remove links.
        * Checked that the correct quantity is shown in the box.
        * Tested that the + and – buttons increase or decrease this number.
            * Checked that + gets disabled at 99.
            * Checked that - gets disabled at 1.
        * Pressed the update link:
            * Seen that the quantity in the cart has changed to that chosen.
            * Seen the toast message appears confirming this change.
            * Checked the rows subtotal adjusts accordingly.
            * Checked the overall totals below adjust.
            * Checked the free next day delivery banner adjusts (if applicable).
        * Pressed the remove link:
            * Checked that the item is removed from the cart and is no longer displayed. 
            * Seen the toast message appears confirming the removal.
            * Checked the rest of the cart reacts accordingly.
    * Checked that the subtotal is always displayed.
6.	Tested that each row is responsive to screen width and the most important information is always displayed.
7.	Checked the totals are shown underneath the last row and are done so in a clear and obvious manner.
8.	Pressed the checkout button at the bottom, this takes me to the checkout page.

**Checkout:**
1.	Tested that each page is fully responsive and everything stacks on top of one another at widths below 768px.
2.	Checked that the order summary section should be reflective of the cart page that we’ve just been on.
    * Checked that the order summary title has an item count next to it.
    * Checked each line item is listed and matches that of that what was in the cart.
    * Checked that the subtotal, delivery and total all match too.
3.	Adjust cart button takes the user back to the cart page if amendments need to be made.
4.	Checked the form to capture the users details, delivery information and payment details is broken into three sections
    * Details
        * Made up of three input fields: *full name, *email and *phone number. Fields marked with a * are required in order to submit the form.
        * Checked if the user is unregistered all fields will be blank showing the placeholders only. 
        * Checked if the user is registered and has ordered something previously from the site then these fields could be pre-populated if they have default delivery information saved to their profile.
    * Delivery
        * Made up of five input fields: *address, *town, county, postcode and *country. Fields marked with a * are required in order to submit the form.
        * Checked if the user is unregistered all fields will be blank showing the placeholder only. 
        * Checked if the user is registered and has ordered something previously from the site then these fields could be pre-populated if they have default delivery information saved to their profile.
    * Payment
        * One field that takes the card number, the MM/YY and CVC number.
        * Checked that this field is required and will always be blank.
5.	Checked the form validates properly by:
    * Attempting to send an empty form.
    * Attempting to send the form whilst leaving any of the * fields empty.
    * Checking that the email field only accepts something with an @ in it.
    * Attempted to send while leaving the payment field empty. This causes a validation error sent from Stripe.
6.	Checked that dependent on user status either a link to log in or sign up appears or a check box to save delivery information is shown after the delivery details.
    * Clicked the log in link.
    * Clicked the sign up link.
    * Toggled the checkbox to test it works and appears for registered users only.
7.	Checked that two buttons appear at the bottom of the screen along with a confirmation of the total:
    * Checked the hover classes works.
    * Checked the amounts match throughout.
    * Adjust cart button takes the user back to the cart page in case amendments need to be made.
    * Pressing the place order button starts the checkout / Stripe’s payment process.
8.	Checked the order processing overlay appears to show that something is happening.
9.	On successful completion of the order I’m sent to the order success page where a summary of the order is displayed.
10.	Checked the page is responsive and everything stacks on top on one another at widths below 768px.

**Order confirmation:**
1.	Checked confirmation page loads as it should. 
    * A note to say where the confirmation has been sent appears.
    * A success toast appears confirming the order.
    * All information on the confirmation is relevant and correct:
        * Order info (order number and order date) is shown.
        * Delivery info (address and contact number) is shown.
        * Order details shown.
        * Billing details (subtotal, delivery and total) are shown.
2.	Checked that I received the confirmation email sent.
3.	Checked that Stripe has taken the payment.
4.	Checked the order now appears in the database.
5.	Checked that if I’m a registered user the order appears in my profile under order history.
6.	Checked if my delivery information gets saved.
    * If box is ticked then existing information is overwritten.
    * If it’s left unticked then nothing gets saved.
7.	Checked that the page is responsive and everything stacks on top on one another at widths below 768px.