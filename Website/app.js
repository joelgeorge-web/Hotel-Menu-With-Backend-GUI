let openShopping = document.querySelector('.shopping');
let closeShopping = document.querySelector('.closeShopping');
let list = document.querySelector('.list');
let listCard = document.querySelector('.listCard');
let body = document.querySelector('body');
let total = document.querySelector('.total');
let quantity = document.querySelector('.quantity');

openShopping.addEventListener('click', ()=>{
    body.classList.add('active');
})
closeShopping.addEventListener('click', ()=>{
    body.classList.remove('active');
})

let products = [
    {
        id: 1,
        name: 'CHICKEN AND EGG',
        image: '1.PNG',
        price: 120
    },
    {
        id: 2,
        name: 'CHICKEN TENDER',
        image: '2.PNG',
        price: 150
    },
    {
        id: 3,
        name: 'CHICKEN SALAD',
        image: '3.PNG',
        price: 220
    },
    {
        id: 4,
        name: 'PUMPKIN SOUP',
        image: '4.PNG',
        price: 90
    },
    {
        id: 5,
        name: 'SALAD',
        image: '5.PNG',
        price: 170
    },
    {
        id: 6,
        name: 'PIZZA',
        image: '6.PNG',
        price: 350
    }
];
let listCards  = [];

function addToCard(key) {
  if (listCards[key] == null) {
    // copy product form list to list card
    listCards[key] = JSON.parse(JSON.stringify(products[key]));
    listCards[key].quantity = 1;

  } else {
    listCards[key].quantity++;
  }

  reloadCard();
  showNotification();
}

  
function showNotification() {
    const notification = document.createElement('div');
    notification.classList.add('notification');
    notification.textContent = 'Item added to cart';
    document.body.appendChild(notification);
    setTimeout(() => {
      notification.remove();
    }, 500);
}
  

function reloadCard(){
    listCard.innerHTML = '';
    let count = 0;
    let totalPrice = 0;
    listCards.forEach((value, key)=>{
        if (value) {
            totalPrice = totalPrice + value.price;
            count = count + value.quantity;
            let newDiv = document.createElement('li');
            newDiv.innerHTML = `
                <div><img src="image/${value.image}"/></div>
                <div>${value.name}</div>
                <div>${value.price.toLocaleString()}</div>
                <div>
                    <button onclick="changeQuantity(${key}, ${value.quantity - 1})">-</button>
                    <div class="count">${value.quantity}</div>
                    <button onclick="changeQuantity(${key}, ${value.quantity + 1})">+</button>
                </div>`;
            listCard.appendChild(newDiv);
        }
    })
    
    total.innerText = totalPrice.toLocaleString();
    quantity.innerText = count;
}

function changeQuantity(key, quantity){
    if(quantity == 0){
        delete listCards[key];
    }else{
        listCards[key].quantity = quantity;
        listCards[key].price = quantity * products[key].price;
    }
    reloadCard();
}


document.querySelector('.confirm').addEventListener('click', () => {
    // create an array of cart items
    const cartItems = {};
    products.map((product,i)=>{
      listCards.forEach((item, index) => {
        if (item.id === i) {
          cartItems[`id${i+1}`] = item.quantity
        }
      });
      if(!cartItems[`id${i+1}`]){
        cartItems[`id${i+1}`] = 0
      }
    })

    
    // send cart data to server
    fetch('/save', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(cartItems)
    })
    .then(response => response.text())
    .then(data => {
      console.log(data);
      alert(data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  });