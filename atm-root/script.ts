document.addEventListener("DOMContentLoaded", function() {
    const botao = document.querySelector('#btn');
    console.log("Elemento botão:", botao);
    if (botao) {
        botao.addEventListener('click', postDados);
    } else {
        console.warn("Botão não encontrado!");
    }
});

async function postDados() {
    const inputElement = document.getElementById("entradaDados") as HTMLInputElement;

    if (!inputElement || !inputElement.value.trim()) {
        alert("Digite o valor desejado!");
        return;
    }

    let valor = parseInt(inputElement.value.trim());

    if (!Number.isInteger(valor) || valor < 2) {
        alert("Valor fornecido não é um número inteiro ou não pode ser atendido com as células disponíveis");
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/api/saque', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ valor }),
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }

        const result = await response.json();
        console.log('Sucesso:', result);
        
        alert('Requisição bem-sucedida!');
        alert(`Resposta da API: ${JSON.stringify(result)}`);

    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao processar a requisição.');
    }
}
