var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements({
    fonts: [
        // integrate font into stripe - https://stackoverflow.com/questions/43824382/custom-font-src-with-stripe/56985340
        {cssSrc: 'https://fonts.googleapis.com/css2?family=Montserrat&display=swap'},
    ]
});

var style = {
    base: {
        color: '#061A40',
        fontFamily: 'Montserrat, sans-serif', // set integrated font family
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