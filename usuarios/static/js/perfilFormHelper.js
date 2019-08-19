const name = document.getElementById('id_name')
const email = document.getElementById('id_email')
const newPassword1 = document.getElementById('id_new_password1')
const newPassword2 = document.getElementById('id_new_password2')
const oldPassword = document.getElementById('id_old_password')

name.classList = 'form-control mb-3'
email.classList = 'form-control mb-3'
newPassword1.classList = 'form-control mb-3'
newPassword2.classList = 'form-control mb-3'
oldPassword.classList = 'form-control mb-3'

name.placeholder = "Nome completo"
email.placeholder = "E-mail"
newPassword1.placeholder = "Nova senha"
newPassword2.placeholder = "Confirmação de senha"
oldPassword.placeholder = "Senha antiga"