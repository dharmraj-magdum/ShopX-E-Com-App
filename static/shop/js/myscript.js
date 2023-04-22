$("#slider1, #slider2, #slider3").owlCarousel({
	loop: true,
	margin: 20,
	responsiveClass: true,
	responsive: {
		0: {
			items: 1,
			nav: false,
			autoplay: true,
		},
		600: {
			items: 3,
			nav: true,
			autoplay: true,
		},
		1000: {
			items: 5,
			nav: true,
			loop: true,
			autoplay: true,
		},
	},
});

////////////    product quantity modification   /////////////
amountEle = document.getElementById("amount");
totalEle = document.getElementById("total");
//add listerner to all plus buttons
$(".plus-cart").click(changeCount);
$(".minus-cart").click(changeCount);

function changeCount() {
	let id = $(this).attr("pid").toString();
	let action = $(this).attr("act").toString();
	// console.log("=========");
	// console.log("act", action);
	// console.log(product_id);

	//=======show the changed quantity
	//for plus its prev ele is showing quantity
	// console.log($(this).prev()); get it first then modify anytime
	add_quantityEle = $(this).prev();
	minus_quantityEle = $(this).next();
	// console.log(quantityEle);
	//now ajax make a new request to our app with url
	$.ajax({
		type: "GET",
		url: "/change-cart/",
		data: {
			product_id: id,
			act: action,
		},
		success: function (data) {
			// console.log(data);
			// console.log("display changed by ajax");
			if (action == "add") {
				add_quantityEle.text(data.quantity);
			} else {
				minus_quantityEle.text(data.quantity);
			}
			amountEle.innerText = data.amount;
			totalEle.innerText = data.total;
		},
	});
}

//// remove cart ele from cart of user
//add listerner to all plus buttons
$(".remove-cart").click(removeCart);

function removeCart() {
	let id = $(this).attr("pid").toString();
	// console.log("=========");
	// console.log(product_id);
	cartEle = $(this).parent().parent().parent().parent();
	// console.log(cartEle);
	$.ajax({
		type: "GET",
		url: "/remove-cart/",
		data: {
			product_id: id,
		},
		success: function (data) {
			// console.log(data);
			cartEle.remove();
			amountEle.innerText = data.amount;
			totalEle.innerText = data.total;
		},
	});
}

console.log("==script runned successfullly====");
