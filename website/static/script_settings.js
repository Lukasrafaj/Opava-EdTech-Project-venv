document.addEventListener('DOMContentLoaded', () => {
  
  // Profile Option (only when authenticated)
  const name = document.getElementById('NameChange');
  if (name) {
    name.addEventListener('click', () => {
      window.location.href = '/settings-name';
    });
  }
  const password = document.getElementById('PasswordChange');
  if (password) {
    password.addEventListener('click', () => {
      window.location.href = '/settings-password';
    });
  }
  const language = document.getElementById('LanguageChange');
  if (language) {
    language.addEventListener('click', () => {
      window.location.href = '/settings-language';
    });
  }
  const email = document.getElementById('EmailChange');
  if (email) {
    email.addEventListener('click', () => {
      window.location.href = '/settings-email';
    });
  }
});