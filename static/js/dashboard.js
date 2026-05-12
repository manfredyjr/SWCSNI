// ==============================
// GRÁFICA 1: EVOLUCIÓN NUTRICIONAL
// ==============================

const ctx1 = document.getElementById('graficaEvolucion');

if (ctx1) {
    new Chart(ctx1, {
        type: 'line',
        data: {
            labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul'],
            datasets: [
                {
                    label: 'Normal',
                    data: [300, 320, 310, 330, 340, 350, 360],
                    borderColor: 'green',
                    backgroundColor: 'rgba(0,128,0,0.2)',
                    fill: true
                },
                {
                    label: 'Riesgo',
                    data: [200, 180, 190, 170, 160, 150, 140],
                    borderColor: 'orange',
                    backgroundColor: 'rgba(255,165,0,0.2)',
                    fill: true
                },
                {
                    label: 'Desnutrición',
                    data: [100, 120, 110, 130, 140, 150, 160],
                    borderColor: 'red',
                    backgroundColor: 'rgba(255,0,0,0.2)',
                    fill: true
                }
            ]
        }
    });
}

// ==============================
// GRÁFICA 2: CLASIFICACIÓN
// ==============================

const ctx2 = document.getElementById('graficaClasificacion');

if (ctx2) {
    new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: ['Normal', 'Riesgo', 'Desnutrición'],
            datasets: [{
                label: 'Niños',
                data: [150, 120, 80],
                backgroundColor: ['green', 'orange', 'red']
            }]
        }
    });
}