const searchButton = document.querySelector('#search_button');
const inputForm = document.querySelector('input');

class Stock_List {
  constructor() {
    // fetching the json file and building
    this.data = null;
    this.initialData();
  }

  /**
   * this will read the json file, get the data needed
   * and then build up the initial list on startup that was
   * saved in the json file
   */
  async initialData() {
    this.fetchJson().then(() => {
      for (const stock of this.data) {
        this.add_stock(stock);
      }
    });
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
    return data;
  }

  /**
   * this will add a stock to the front end
   * @param {*} jsObject : A JavaScript Object of stock info
   */
  add_stock(jsObject) {
    let big_container = document.querySelector('.background');
    // this statement fixes the background once a stock is added
    if (this.data.length > 1) {
      big_container.style.position = 'sticky';
    }

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
    // checks negative to add the correct style
    this.check_negative(stock_container);

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
    eel.remove_stock(this.id);
    removed_stock.remove();
    background_adjuster();
  }

  /**
   * will correct the style of the stocks percent change
   * if the stock is down for the day
   * @param {*} stockContainer : Stock container that the function is correcting
   */
  check_negative(stockContainer) {
    let percent_change = stockContainer.querySelector('.percent_change');
    let inner = percent_change.innerHTML;
    if (inner.charAt(0) == '-') {
      percent_change.className = 'negative';
    }
  }
}

/**
 * this function is used in the remove stock function in Stock_list
 * it will adjust the background properly to keep the display consitent for the
 * user
 */
function background_adjuster() {
  let stocks_displayed = document.querySelectorAll('.stock_container').length;
  let background = document.querySelector('.background');
  //clears the sticky background assigend while adding stocks when the document
  //has less then 2 stocks displayed
  if (stocks_displayed <= 1) {
    background.style = '';
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

/**
 * allows communications for the backend and
 * the front end to dymanically add stocks
 * to the front end
 */
function add_new_stock() {
  user_stocks.fetchJson().then(() => {
    let stock_arr = user_stocks.data;
    let added_stock = stock_arr[stock_arr.length - 1];
    user_stocks.add_stock(added_stock);
  });
}
eel.expose(add_new_stock);
