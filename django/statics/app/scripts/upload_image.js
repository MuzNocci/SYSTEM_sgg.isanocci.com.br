const inputFile = document.getElementById('photo');
const previewImage = document.getElementById('image-preview');

inputFile.addEventListener('change', function(event) {
  const file = event.target.files[0];

  if (file && file.type.startsWith('image/')) {
    const reader = new FileReader();

    reader.onload = function(e) {
      previewImage.src = e.target.result;
      previewImage.style.display = 'block';
    };

    reader.readAsDataURL(file);
  } else {
    previewImage.style.display = 'none';
  }
});