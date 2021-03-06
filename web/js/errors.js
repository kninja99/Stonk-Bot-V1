/**
 * this function handles a search error on the front end
 */
function searchError(ticker) {
  alert(`${ticker} does not exist`);
}
eel.expose(searchError);
/**
 * this function will alert an error if a duplicate entry is tried
 */
function duplicateDataError() {
  alert('Data has alread been retrieved for this stock ticker');
}
eel.expose(duplicateDataError);
