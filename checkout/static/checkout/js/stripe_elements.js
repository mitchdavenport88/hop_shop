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
}

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
    // sends the card info to stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        // check for error
        if(result.error) {
            let errorDiv = document.getElementById('card-errors');
            let html = `
                <p class="text-danger small m-0 font-weight-bold">
                    <i class="fas fa-times"></i> ${result.error.message}
                </p>
            `;
            $(errorDiv).html(html);
            $('#loading-overlay').fadeToggle(100);
            // re-enable the card element and submit button to allow submission again
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});