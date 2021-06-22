function addTicker(text) {
  // grabs ticker
  var ticker = document.getElementById('ticker');
  // text
  ticker.innerHTML += text;
}
eel.expose(addTicker);

// this is used to test if the script is working or not
addTicker('hello');
