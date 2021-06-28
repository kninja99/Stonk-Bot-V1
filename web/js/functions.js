// base function we can use to add only one ticker at the moment
// just trying to get functionality down before optimizing for expansion
function addTicker(tick) {
  let h3 = document.querySelector('.ticker');
  h3.textContent = tick;
}
eel.expose(addTicker);

// script to set news articles, takes in an array of strings
// this function will also need work in order to expand the app
function setNewsArticles(newArticleArr) {
  let list = document.querySelector('.articles');
  for (const text of newArticleArr) {
    let article = document.createElement('li');
    article.textContent = text;
    list.appendChild(article);
  }
}
eel.expose(setNewsArticles);
