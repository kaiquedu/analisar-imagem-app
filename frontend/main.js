const inputFile = document.getElementById('inputFile');
const buttonAnalyze = document.getElementById('buttonAnalyze');
const img = document.getElementById('imagePreview');
const promptContainer = document.getElementById('promptContainer');
const loadingOverlay = document.getElementById('loadingOverlay');

inputFile.addEventListener('change', (e) => {
    const file = e.target.files[0];

    if (file) {
        const url = URL.createObjectURL(file);
        img.src = url;
        img.style.display = 'block'; 
    } else {
        alert('Por favor, selecione um arquivo de imagem válido.'); 
    }
});

buttonAnalyze.addEventListener('click', async () => {
    const file = inputFile.files[0]; 

    if (file) {
        const formData = new FormData();
        formData.append('image', file); 

        loadingOverlay.style.display = 'flex'; 

        try {
            const response = await axios.post('http://localhost:5000/analyze-image', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data', 
                },
            });
            promptContainer.textContent = `Descrição da Imagem: ${response.data.prompt}`;
        } catch (error) {
            console.error('Erro ao obter prompt:', error);
            promptContainer.textContent = 'Erro ao obter prompt.';
        } finally {
            loadingOverlay.style.display = 'none';
        }
    } else {
        alert('Por favor, selecione um arquivo de imagem válido.');
    }
});
