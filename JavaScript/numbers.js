// Pick random number between 1-100
var randomNumber = Math.floor(Math.random() * 100) + 1;

// Initialize number of guesses
var numGuesses = 0;

// Main function
function checkGuess() {
  var guess = parseInt(document.querySelector("#guess").value);
  var result = document.querySelector("#result1");
  numGuesses++;
  
// If conditions
  // Correct message
  if (guess === randomNumber) {
    result.innerHTML = "Correct ✔️ It took you " + numGuesses + " guesses to win.";
  } 
  // Number is higher than guess hint
  else if (guess < randomNumber) {
    result.innerHTML = "Incorrect. The number is higher 👆: Guess#" + numGuesses;
  } 
  // Number is lower than guess hint
  else {
    result.innerHTML = "Incorrect. The number is lower 👇: Guess#" + numGuesses;
  }
}

//---------------------------------------------------------


function Calc(num) {
  // If number is 0 or 1
  if (num <= 1) {
    return 1;
  } 
  // If number is above 1
  else {
    return num * Calc(num - 1);
  }
}

// Take and pass the input value
function factorial() {
  const num = document.querySelector("#number").value;
  const result = Calc(num);
  const resultText = `The factorial of ${num} is ${result}.`;
  const resultOutput = document.querySelector("#result2");
  resultOutput.textContent = resultText;
}

//---------------------------------------------------------

function handleClick() {
  const input = document.querySelector("#numbers").value;
  const numbers = input.split(",").map(num => Number(num.trim()));

  // Array functions
  const evenNumbers = numbers.filter(num => num % 2 === 0);
  const oddNumbers = numbers.filter(num => num % 2 === 1);
  const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue);
  const squaredNumbers = numbers.map(num => num ** 2);
  const greaterThanTen = numbers.filter(num => num > 10);

  // Output
  const output = `Even Numbers: ${evenNumbers.join(", ")}<br>
                  Odd numbers: ${oddNumbers.join(", ")}<br>
                  Summed numbers: ${sum}<br>
                  Numbers squared: ${squaredNumbers}<br>
                  Numbers greater than ten: ${greaterThanTen}`;

  // Print
  const outputElement = document.querySelector("#result3");
  outputElement.innerHTML = output;
}

//---------------------------------------------------------
