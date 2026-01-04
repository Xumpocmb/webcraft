document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contact-form');
    const formMessages = document.getElementById('form-messages');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(this);
            const xhr = new XMLHttpRequest();
            xhr.open('POST', this.action, true);
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest'); // Indicate an AJAX request

            xhr.onload = function () {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    formMessages.innerHTML = ''; // Clear previous messages
                    const messageElement = document.createElement('ul');
                    messageElement.classList.add('messages');
                    const listItem = document.createElement('li');
                    listItem.textContent = response.message;

                    if (response.status === 'success') {
                        listItem.classList.add('success');
                        contactForm.reset(); // Clear the form
                    } else if (response.status === 'error') {
                        listItem.classList.add('error');
                    } else if (response.status === 'warning') {
                        listItem.classList.add('warning');
                    }
                    messageElement.appendChild(listItem);
                    formMessages.appendChild(messageElement);
                } else {
                    formMessages.innerHTML = `<ul class="messages"><li class="error">Произошла ошибка при отправке формы. Попробуйте еще раз.</li></ul>`;
                }
            };

            xhr.onerror = function () {
                formMessages.innerHTML = `<ul class="messages"><li class="error">Произошла ошибка сети. Проверьте ваше соединение.</li></ul>`;
            };

            xhr.send(formData);
        });
    }
});
