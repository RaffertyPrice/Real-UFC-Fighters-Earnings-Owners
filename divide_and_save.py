<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Division Rankings</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      background-color: #f9f9f9;
    }
    h1 {
      text-align: center;
    }
    form {
      background: white;
      padding: 15px;
      border-radius: 10px;
      box-shadow: 0 0 5px rgba(0,0,0,0.1);
      max-width: 400px;
      margin: auto;
    }
    input, button {
      width: 100%;
      padding: 8px;
      margin: 5px 0;
      border-radius: 5px;
      border: 1px solid #ccc;
    }
    table {
      width: 80%;
      border-collapse: collapse;
      margin: 20px auto;
      background: white;
    }
    th, td {
      padding: 8px;
      border: 1px solid #ddd;
      text-align: center;
    }
    .gold { background-color: #d4edda; }
    .silver { background-color: #cce5ff; }
    .bronze { background-color: #fff3cd; }
    .undefined { background-color: #f8d7da; }
  </style>
</head>
<body>

<h1>Division Rankings</h1>

<form id="dataForm">
  <input type="text" id="name" placeholder="Dataset name" required>
  <input type="number" step="any" id="dividend" placeholder="Dividend" required>
  <input type="number" step="any" id="divisor" placeholder="Divisor" required>
  <button type="submit">Add Dataset</button>
  <button type="button" onclick="finishInput()">Finish & Show Rankings</button>
</form>

<div id="results"></div>

<script>
  let datasets = [];

  document.getElementById('dataForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value.trim();
    const dividend = parseFloat(document.getElementById('dividend').value);
    const divisor = parseFloat(document.getElementById('divisor').value);

    let result = null;
    if (divisor !== 0) {
      result = dividend / divisor;
    }

    datasets.push({ name, dividend, divisor, result });

    // Clear inputs
    document.getElementById('name').value = '';
    document.getElementById('dividend').value = '';
    document.getElementById('divisor').value = '';
  });

  function finishInput() {
    // Sort datasets by result (highest first, undefined last)
    datasets.sort((a, b) => {
      if (a.result === null) return 1;
      if (b.result === null) return -1;
      return b.result - a.result;
    });

    let tableHTML = `
      <table>
        <tr>
          <th>Rank</th>
          <th>Name</th>
          <th>Dividend</th>
          <th>Divisor</th>
          <th>Result</th>
        </tr>
    `;

    datasets.forEach((entry, index) => {
      let rowClass = '';
      if (entry.result === null) {
        rowClass = 'undefined';
      } else if (index === 0) {
        rowClass = 'gold';
      } else if (index === 1) {
        rowClass = 'silver';
      } else if (index === 2) {
        rowClass = 'bronze';
      }

      let resultText = entry.result === null ? 'undefined' : entry.result.toFixed(2);

      tableHTML += `
        <tr class="${rowClass}">
          <td>${index + 1}</td>
          <td>${entry.name}</td>
          <td>${entry.dividend}</td>
          <td>${entry.divisor}</td>
          <td>${resultText}</td>
        </tr>
      `;
    });

    tableHTML += '</table>';
    document.getElementById('results').innerHTML = tableHTML;
  }
</script>

</body>
</html>
