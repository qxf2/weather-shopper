$(document).ready(function () {
    $('[data-toggle="popover"]').popover();
});

var cart = {};
var item_count = 0;
function addToCart(name, price) {
    cart[name]=price;
    console.log(cart);
    item_count = item_count + 1;
    document.getElementById("cart").innerHTML = item_count + " item(s)";
};
function goToCart() {
    //Make a post here
    //Src: https://stackoverflow.com/a/51214863
    var form = document.createElement('form');
    form.style.visibility = 'hidden'; // no user interaction is necessary
    form.method = 'POST'; 
    form.action = '/cart';
    console.log(Object.keys(cart));
    $.each(Object.keys(cart), function(index, key) {
        var input = document.createElement('input');
        input.name = key;
        input.value = cart[key];
        form.appendChild(input); 
    });
    document.body.appendChild(form); // forms cannot be submitted outside of body
    form.submit();
};
