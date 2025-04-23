let chart = null;

document.getElementById('formulario').addEventListener('submit', async (e) => {
  e.preventDefault();
  const horizon = document.getElementById('horizon').value;

  const response = await fetch(`/predecir?horizon=${horizon}`);
  const data = await response.json();

  const prediccion = data.prediccion;
  document.getElementById('output').textContent = JSON.stringify(prediccion, null, 2);

  const labels = prediccion.map((_, i) => `Día ${i + 1}`);

  // Crea o actualiza gráfico
  if (chart) {
    chart.data.labels = labels;
    chart.data.datasets[0].data = prediccion;
    chart.update();
  } else {
    const ctx = document.getElementById('chart').getContext('2d');
    chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Predicción del Oro',
          data: prediccion,
          fill: false,
          borderColor: '#007bff',
          tension: 0.3
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: true },
          tooltip: { mode: 'index' }
        },
        scales: {
          y: { title: { display: true, text: 'Precio (normalizado)' } },
          x: { title: { display: true, text: 'Horizonte futuro' } }
        }
      }
    });
  }
});
