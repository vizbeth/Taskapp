const navSlide = ()=>{
    const nav = document.querySelector('.nav-links');
    const burger = document.querySelector('.burger');
    const navLink = document.querySelectorAll('.nav-links li')

    burger.addEventListener('click', ()=>{
        nav.classList.toggle('nav-active')

        navLink.forEach((link, index)=>{
         if(link.style.animation){
            link.style.animation = ''

         }else{
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 1.5}s`
         }

        });

        burger.classList.toggle('swing');
    });
}
navSlide()

const mainSlide = ()=>{
    const arrowLeft = document.getElementById('arrow-left');
    const arrowRight = document.getElementById('arrow-right');
    const sliderImages = document.querySelectorAll('.slides')
    let current = 0

    function startSlide(){
        reset();
        sliderImages[0].style.display = 'block'
    }

    function reset(){
        for(let i = 0; i < sliderImages.length; i++){
            sliderImages[i].style.display = 'None';
        }
    }

    function slideLeft(){
        reset();
        sliderImages[current - 1].style.display = 'block';
        current --;
    }

    function slideRight(){
        reset()
        sliderImages[current + 1].style.display = 'block';
        current ++;
    }

    arrowLeft.addEventListener('click', ()=>{
        if(current == 0){
            current = sliderImages.length
        }
        slideLeft()
    });

    arrowRight.addEventListener('click', ()=>{
        if(current == sliderImages.length - 1){
            current = -1;
        }
        slideRight()
    });

   startSlide()
}
mainSlide()


const bannerHide = ()=>{

    const alertBox = document.querySelector('.alert-box');
    const closeIcon = document.querySelector('.close-icon');
    
    closeIcon.addEventListener('click', ()=>{
       if(closeIcon){
           alertBox.style.display = 'None'
       }
    })
}
bannerHide







