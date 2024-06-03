        document.getElementById('upload-button').addEventListener('click', function() {
            var formData = new FormData();
            formData.append('image', document.getElementById('image-input').files[0]);
            formData.append('additional_data', document.getElementById('additional-data-input').value);

            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/process-image/', true);

            xhr.onload = function() {
                if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    document.getElementById('processed-image').src = 'data:image/jpeg;base64,' + response.processed_image;
                    document.getElementById('processed-image-container').style.display = 'block';
                }
            };

            xhr.send(formData);
        });

        document.getElementById('image-input').addEventListener('change', function() {
            var file = this.files[0];
            var reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById('original-image').src = e.target.result;
                document.getElementById('original-image-container').style.display = 'block';
            };
            reader.readAsDataURL(file);
        });