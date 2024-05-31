document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('arithmetic-form')?.addEventListener('submit', async (event) => {
        event.preventDefault();
        const num1 = document.getElementById('num1').value;
        const num2 = document.getElementById('num2').value;
        const operacao = document.getElementById('operacao').value;
        const base_final = document.getElementById('base_final').value;

        try {
            const response = await fetch('/api/arithmetic', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ num1, num2, operacao, base_final }),
            });

            const result = await response.json();
            if (result.resultado) {
                document.getElementById('arithmetic-result').innerText = `Resultado: ${result.resultado}`;
            } else {
                document.getElementById('arithmetic-result').innerText = `Erro: ${result.erro}`;
            }
        } catch (error) {
            console.error('Erro:', error);
            document.getElementById('arithmetic-result').innerText = 'Erro ao obter resultado';
        }
    });

    document.getElementById('gray-form')?.addEventListener('submit', async (event) => {
        event.preventDefault();
        const n_bits = document.getElementById('n_bits').value;

        try {
            const response = await fetch('/api/gray', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ n_bits }),
            });

            const result = await response.json();
            document.getElementById('gray-result').innerText = `Resultado: ${result.resultado.join(', ')}`;
        } catch (error) {
            console.error('Erro:', error);
            document.getElementById('gray-result').innerText = 'Erro ao obter resultado';
        }
    });

    document.getElementById('conversion-form')?.addEventListener('submit', async (event) => {
        event.preventDefault();
        const numero = document.getElementById('numero').value;
        const base_origem = document.getElementById('base_origem').value;
        const base_destino = document.getElementById('base_destino').value;

        try {
            const response = await fetch('/api/convert', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ numero, base_origem, base_destino }),
            });

            const result = await response.json();
            document.getElementById('conversion-result').innerText = `Resultado: ${result.resultado}`;
        } catch (error) {
            console.error('Erro:', error);
            document.getElementById('conversion-result').innerText = 'Erro ao obter resultado';
        }
    });
});
