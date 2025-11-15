document.addEventListener('DOMContentLoaded', () => {
  
  const physicsButton = document.getElementById('physicsButton');
  if (physicsButton) {
    physicsButton.addEventListener('click', () => {
      window.location.href = '/courses/physics';
    });
  }
});