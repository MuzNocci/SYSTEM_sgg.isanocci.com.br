    // Selecionar os elementos
    const inputFile = document.getElementById('upload-input');
    const previewImage = document.getElementById('image-preview');

    // Adicionar evento de mudança no input
    inputFile.addEventListener('change', function(event) {
      const file = event.target.files[0]; // Obter o arquivo selecionado

      // Verificar se o arquivo é válido
      if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();

        // Quando a leitura for concluída
        reader.onload = function(e) {
          previewImage.src = e.target.result; // Definir a imagem no src
          previewImage.style.display = 'block'; // Tornar visível
        };

        reader.readAsDataURL(file); // Ler o arquivo como URL base64
      } else {
        previewImage.style.display = 'none'; // Ocultar caso não seja uma imagem
      }
    });