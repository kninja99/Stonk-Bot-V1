const searchButton = document.querySelector('#search_button');
const inputForm = document.querySelector('input');

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

//search bar handlers
searchButton.addEventListener('click', searchBarHandler);
// this event handler allows the user to press enter for input
inputForm.addEventListener('keyup', function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    searchButton.click();
  }
});
