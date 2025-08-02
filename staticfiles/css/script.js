const signInBtnLink = document.querySelector('.signInBtn-link');
const signUpBtnLink = document.querySelector('.signUpBtn-link');
const wrapper = document.querySelector('.wrapper');
signUpBtnLink.addEventListener('click', () => {
    wrapper.classList.toggle('active');
});
signInBtnLink.addEventListener('click', () => {
    wrapper.classList.toggle('active');
});

document.getElementById('scroll-to-top').addEventListener('click', function(e) {
    e.preventDefault();  // prevent default anchor behavior
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
