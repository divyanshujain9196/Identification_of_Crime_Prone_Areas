// Get the form element
const form = document.querySelector('form');

// Add an event listener for the form submit
form.addEventListener('submit', (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the input values from the form
  const latitude = document.getElementById('latitude').value;
  const longitude = document.getElementById('longitude').value;
  const population = document.getElementById('population').value;
  const median_income = document.getElementById('median_income').value;

  // Send a POST request to the server with the input data
  fetch('/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      latitude: latitude,
      longitude: longitude,
      population: population,
      median_income: median_income
    })
  })
  .then(response => response.json())
  .then(data => {
    // Display the predicted crime rate in the result element
    const result = document.getElementById('result');
    result.innerHTML = `Predicted crime rate: ${data.crime_rate.toFixed(2)}%`;
  })
  .catch(error => {
    // Display an error message if the request fails
    const result = document.getElementById('result');
    result.innerHTML = 'Error predicting crime rate.';
  });
});
