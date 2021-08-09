const searchButton = document.querySelector('#search_button');
const inputForm = document.querySelector('input');

class Stock_List {
  constructor() {
    let big_container = document.querySelector('.background');
    let stock_container = document.createElement('div');
    stock_container.className = 'stock_container';
    stock_container.innerHTML = `
    <div class="stock_header">
      <h2 class="stock_ticker">AAPL</h2>
      <h2 class="price">$23.99</h2>
      <h2 class="percent_change">+2.5%</h2>
      <button>
        <div class="line"></div>
      </button>
    </div>
    <div class="articles">
      <h3>News Header</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Est modi
        magni numquam doloribus, ipsum commodi aliquam optio quis! Eaque
        veritatis, dolor doloribus, voluptatum laudantium incidunt
        consequuntur quasi est nihil officiis quo adipisci libero dolorem
        animi?
      </p>
      <h3>News Header</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Est modi
        magni numquam doloribus, ipsum commodi aliquam optio quis! Eaque
        veritatis, dolor doloribus, voluptatum laudantium incidunt
        consequuntur quasi est nihil officiis quo adipisci libero dolorem
        animi?
      </p>
      <h3>News Header</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Est modi
        magni numquam doloribus, ipsum commodi aliquam optio quis! Eaque
        veritatis, dolor doloribus, voluptatum laudantium incidunt
        consequuntur quasi est nihil officiis quo adipisci libero dolorem
        animi?
      </p>
    </div>
    `;

    big_container.appendChild(stock_container);
  }
}

let temp = new Stock_List();

// fetching the json file (async)
fetch('../stocks.json')
  .then(function (resp) {
    return resp.json();
  })
  .then(function (data) {
    console.log(data);
  });

/**
 * This function will be handling the search bar inputs
 */
function searchBarHandler() {
  const input = inputForm.value;
  inputForm.value = '';
  eel.grabInput(input);
}

/**
 * this function handles a search error on the front end
 */
function searchError() {
  alert('No such stock ticker exist');
}
eel.expose(searchError);

function duplicateDataError() {
  alert('Data has alread been retrieved for this stock ticker');
}
eel.expose(duplicateDataError);

// This section will handle the adding and deleteing of the stocks on the front end

//search bar handlers
searchButton.addEventListener('click', searchBarHandler);
// this event handler allows the user to press enter for input
inputForm.addEventListener('keyup', function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    searchButton.click();
  }
});
