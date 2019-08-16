const username = document.getElementById('id_username')
const name = document.getElementById('id_name')
const email = document.getElementById('id_email')
const password1 = document.getElementById('id_password1')
const password2 = document.getElementById('id_password2')

username.classList = 'form-control mt-2 mb-2';
name.classList = 'form-control mt-2 mb-2';
email.classList = 'form-control mt-2 mb-2';
password1.classList = 'form-control mt-2 mb-2';
password2.classList = 'form-control mt-2 mb-4';

username.placeholder = 'Nome de usuário';
name.placeholder = 'Nome Completo';
email.placeholder = 'E-mail';
password1.placeholder = 'Senha';
password2.placeholder = 'Confirmar Senha';