const searchButton = document.querySelector('#search_button');
const inputForm = document.querySelector('input');

class Stock_List {
  constructor() {
    // fetching the json file and building
    this.initialData();
    this.data = null;
  }

  /**
   * this will read the json file, get the data needed
   * and then build up the initial list on startup that was
   * saved in the json file
   */
  async initialData() {
    const response = await fetch('../stocks.json');
    const data = await response.json();
    for (const stock of data.stock_info) {
      this.add_stock(stock);
    }
  }

  /**
   * will fetch the data from the json file and set it equal to a data array
   * this array is filled with the same info from the stock_info array in the
   * json file
   */
  async fetchJson() {
    const response = await fetch('../stocks.json');
    const data = await response.json();
    this.data = data.stock_info;
  }

  /**
   * this will add a stock to the front end
   * @param {*} jsObject - A JavaScript Object of stock info
   */
  add_stock(jsObject) {
    let big_container = document.querySelector('.background');
    // this statement fixes the background once a stock is added
    big_container.style.position = 'sticky';
    let stock_container = document.createElement('div');
    stock_container.className = 'stock_container';
    stock_container.id = jsObject['stock_ticker'];
    // stock header being built
    stock_container.innerHTML = `
    <div class="stock_header">
      <h2 class="stock_ticker">${jsObject['stock_ticker']}</h2>
      <h2 class="price">${jsObject['price']}</h2>
      <h2 class="percent_change">${jsObject['percent_change']}</h2>
      <button id = ${jsObject['stock_ticker']}>
        <div class="line"></div>
      </button>
    </div>`;
    // articles being built
    for (let i = 0; i < jsObject['headers'].length; i++) {
      stock_container.innerHTML += `
      <div class="articles">
        <h3>${jsObject['headers'][i]}</h3>
        <p>
          ${jsObject['articles'][i]}
        </p>`;
    }
    // closing off the div of the stock container
    stock_container.innerHTML += `
    </div>`;

    // binding the remove button to the remove function
    let remove_button = stock_container.querySelector('button');

    remove_button.addEventListener('click', this.remove_stock);
    // appending all of the content to the container
    big_container.appendChild(stock_container);
  }

  /*
  removes a stock from the front end
  and calls a function to remove it from the back end
  */
  remove_stock() {
    let removed_stock = document.querySelector(`#${this.id}`);
    console.log(removed_stock);
    eel.remove_stock(this.id);
    removed_stock.remove();
  }
}

/**
 * This function will be handling the search bar inputs
 */
function searchBarHandler() {
  const input = inputForm.value;
  inputForm.value = '';
  eel.grabInput(input);
}

//search bar handlers
searchButton.addEventListener('click', searchBarHandler);
// this event handler allows the user to press enter for input
inputForm.addEventListener('keyup', function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    searchButton.click();
  }
});

// this will create a Stock_List object
let user_stocks = new Stock_List();
