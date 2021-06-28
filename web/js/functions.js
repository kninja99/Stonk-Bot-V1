/**
 * funtion that will add a stock ticker and its respected news articles
 * @param {string} tick - the ticker symbol in terms of a string
 * @param {array of type string} articlesArr - array of strings that represent the news articles
 */
function addStock(tick, articlesArr) {
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
  for (const text of articlesArr) {
    let articles = document.createElement('li');
    articles.textContent = text;
    list.appendChild(articles);
  }
  div.appendChild(list);
  //finally appends everything onto the container
  container.appendChild(div);
}
eel.expose(addStock);
