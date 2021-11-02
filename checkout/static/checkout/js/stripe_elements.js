var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements({
    fonts: [
        // integrate font into stripe (set it below in base object)
        // https://stackoverflow.com/questions/43824382/custom-font-src-with-stripe/56985340
        {cssSrc: 'https://fonts.googleapis.com/css2?family=Montserrat&display=swap'},
    ]
});

var style = {
    base: {
        color: '#061A40',
        fontFamily: 'Montserrat, sans-serif',
        fontSize: '16px',
        '::placeholder': {
            color: '#AAB7C4',
        }
    },
    invalid: {
        color: '#DC3545',
        iconColor: '#DC3545'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

// shows validation error message below card number input
card.addEventListener('change', function (event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <p class="text-danger small m-0 font-weight-bold">
                <i class="fas fa-times"></i> ${event.error.message}
            </p>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// form submission
const form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // prevents default, which is to post the form
    ev.preventDefault();
    // disable the card element and submit button to stop duplicate submissions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    // loading page
    $('#loading-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#save-checkout-info').is(':checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';
    
    // posts the above data to cache_checkout_data view 
    // view also collects user, metadata and cart and updates the intent
    $.post(url, postData).done(function() {
        // sends the card info to stripe
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    email: $.trim(form.email.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.street_address.value),
                        city: $.trim(form.town_or_city.value),
                        state: $.trim(form.county.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address.value),
                    city: $.trim(form.town_or_city.value),
                    state: $.trim(form.county.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                }
            },
        }).then(function(result) {
            // checks for error, shows message if there is an error
            if(result.error) {
                let errorDiv = document.getElementById('card-errors');
                let html = `
                    <p class="text-danger small m-0 font-weight-bold">
                        <i class="fas fa-times"></i> ${result.error.message}
                    </p>
                `;
                $(errorDiv).html(html);
                // stops the order processing overlay
                $('#loading-overlay').fadeToggle(100);
                // re-enable the submit button to allow submission again
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    // submits form if no errors are in the form
                    form.submit();
                }
            }
        });
    }).fail(function() {
        // reloads page, error message displays in toast, order is not taken!
        location.reload();
    })
});