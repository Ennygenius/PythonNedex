const btn = document.querySelector(".nav-menu");
const navLinks = document.querySelector(".MobileNav")


btn.addEventListener('click', () =>{
    navLinks.classList.toggle('active')
})

