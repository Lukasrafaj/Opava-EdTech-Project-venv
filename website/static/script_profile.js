document.addEventListener('DOMContentLoaded', () => {
  
  // Profile/Hamburger Menu Toggle
  const profileBtn = document.getElementById('profileBtn');
  const dropdownMenu = document.getElementById('dropdownMenu');
  const profileArrow = document.getElementById('profileArrow'); // Changed
  
  if (profileBtn && dropdownMenu) {
    profileBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      dropdownMenu.classList.toggle('active');
      if (profileArrow) {
        profileArrow.classList.toggle('rotated');
      }
    });
    
    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.profile-container')) {
        dropdownMenu.classList.remove('active');
        if (profileArrow) {
          profileArrow.classList.remove('rotated');
        }
      }
    });
  }
  
  
  // Profile Option (only when authenticated)
  const profileOption = document.getElementById('profileOption');
  if (profileOption) {
    profileOption.addEventListener('click', () => {
      console.log('Navigating to profile...');
      dropdownMenu.classList.remove('active');
      window.location.href = '/profile';
    });
  }
  
  // Settings Option (only when authenticated)
  const settingsOption = document.getElementById('settingsOption');
  if (settingsOption) {
    settingsOption.addEventListener('click', () => {
      console.log('Navigating to settings...');
      dropdownMenu.classList.remove('active');
      window.location.href = '/settings-name';
    });
  }
  
  // Help Option (only when authenticated)
  const helpOption = document.getElementById('helpOption');
  if (helpOption) {
    helpOption.addEventListener('click', () => {
      console.log('Navigating to help...');
      dropdownMenu.classList.remove('active');
      window.location.href = '/help';
    });
  }
  
  // Logout Option (only when authenticated)
  const logoutOption = document.getElementById('logoutOption');
  if (logoutOption) {
    logoutOption.addEventListener('click', () => {
      console.log('Logging out...');
      dropdownMenu.classList.remove('active');
      window.location.href = '/logout';
    });
  }
  const logo = document.getElementById('logo');
  if (logo) {
    logo.addEventListener('click', () => {
      console.log('Logging out...');
      dropdownMenu.classList.remove('active');
      window.location.href = '/';
    });
  }
  
});