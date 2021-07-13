const searchButton = document.querySelector('button');
const inputForm = document.querySelector('input');

/**
 * funtion that will add a stock ticker and its respected news articles
 * @param {string} tick - the ticker symbol in terms of a string
 * @param {array of type string} articlesArr - array of strings that represent the news articles
 */
function addStock(tick, headerArr, previewArr) {
  // first target the container for all stock related items
  let container = document.querySelector('.container');
  // div that holds all the stocks elements in that row
  let div = document.createElement('div');
  div.className = 'row';
  // ticker implementation
  let ticker = document.createElement('h3');
  ticker.className = 'ticker';
  ticker.textContent = tick;
  div.appendChild(ticker);
  // list implementation
  let list = document.createElement('ul');
  list.className = 'articles';
  // for loop tha builds up the list element
  for (let i = 0; i < headerArr.length; i++) {
    let li = document.createElement('li');
    let h5 = document.createElement('h5');
    h5.textContent = headerArr[i];
    h5.className = 'article-header';
    let p = document.createElement('p');
    p.className = 'article-preview';
    p.textContent = previewArr[i];
    li.appendChild(h5);
    li.appendChild(p);
    list.appendChild(li);
  }
  div.appendChild(list);
  //finally appends everything onto the container
  container.appendChild(div);
}
eel.expose(addStock);

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
  inputForm.value = '';
}
eel.expose(searchError);

//search bar handlers
searchButton.addEventListener('click', searchBarHandler);
// this event handler allows the user to press enter for input
inputForm.addEventListener('keyup', function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    searchButton.click();
  }
});
