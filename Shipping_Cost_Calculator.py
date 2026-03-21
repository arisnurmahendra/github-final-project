# Shipping Cost Calculator

function calculateShipping() {
  const weight = parseFloat(document.getElementById('weightInput').value);
  let cost;
  if (weight <= 1) cost = 5.00;
  else if (weight <= 5) cost = 10.00;
  else cost = 20.00;
  document.getElementById('output').innerText = `Total: £${cost}`;
}
