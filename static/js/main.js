const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
let stripe = Stripe("{{ STRIPE_PUBLIC_KEY }}");
let buyButton = document.getElementById("buy-button");
const url = buyButton.addEventListener("click", (e) => {
  fetch(url, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrf_token,
    },
  })
    .then((response) => response.json())
    .then((session) => stripe.redirectToCheckout({ sessionId: session.id }));
});
