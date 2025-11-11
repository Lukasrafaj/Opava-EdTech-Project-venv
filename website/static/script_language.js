document.addEventListener('DOMContentLoaded', () => {
    const languageBtn = document.getElementById('languageBtn');
    const dropdown = document.getElementById('dropdown');
    const languageArrow = document.getElementById('languageArrow');
    const selectedFlag = document.getElementById('selectedFlag');
    const selectedLang = document.getElementById('selectedLang');
    const languageOptions = document.querySelectorAll('.language-option');
    
    console.log('Language options found:', languageOptions.length); // Debug
    
    // Toggle dropdown
    if (languageBtn && dropdown) {
        languageBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            dropdown.classList.toggle('active');
            if (languageArrow) {
                languageArrow.classList.toggle('rotated');
            }
            console.log('Dropdown toggled'); // Debug
        });
    }
    
    // Select language
    languageOptions.forEach((option, index) => {
        console.log('Adding listener to option', index); // Debug
        
        option.addEventListener('click', (e) => {
            e.stopPropagation();
            console.log('Language option clicked!'); // Debug
            
            const lang = option.dataset.lang;
            const flagImg = option.querySelector('img');
            const langText = option.querySelector('span');
            
            // Update selected flag
            if (selectedFlag && flagImg) {
                selectedFlag.src = flagImg.src;
                selectedFlag.alt = flagImg.alt;
            }
            
            // Update selected language text
            if (selectedLang && langText) {
                selectedLang.textContent = langText.textContent;
            }
            
            // Close dropdown
            dropdown.classList.remove('active');
            if (languageArrow) {
                languageArrow.classList.remove('rotated');
            }
            
            console.log('Language changed to:', lang);
        });
    });
    
    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.language-selector')) {
            dropdown.classList.remove('active');
            if (languageArrow) {
                languageArrow.classList.remove('rotated');
            }
        }
    });
});