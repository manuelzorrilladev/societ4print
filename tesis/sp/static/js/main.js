

const body = document.body;
const theme = document.querySelector('.tema');
const logo = document.querySelectorAll('.logo');
const navbar = document.querySelector('.navbar');
const navBarBtn = document.querySelector('.navBarBtn');
const pageContainer = document.querySelector('.pageContainer');
const icon = document.querySelectorAll('#icon');
const menu = document.querySelectorAll('.menu');
const slider = document.getElementById('slider');
const arrowLeft = document.getElementById('arrowLeft');
const arrowRight = document.getElementById('arrowRight');
const menu2 = document.querySelectorAll('.menu2');
const popUp = document.querySelectorAll('#popUp');



let counter1= 0;
let counter2 =1;

let move = ['translateX(0%)','translateX(-31%)','translateX(-63%)','translateX(-94%)'];


if (localStorage){
    body.classList.replace('dark', localStorage.getItem('theme'));
    if (localStorage.getItem('theme')=='dark') {
     /* si el tema es oscuro */

      logo[0].classList.replace('hidden', 'show');
      logo[1].classList.replace('show','hidden');

    }else{
        /* si el tema es claro */
        logo[1].classList.replace('hidden', 'show');
        logo[0].classList.replace('show','hidden');
       
    }
        
}

function cambiarTema() {
    if (body.classList == 'ligth'){
        body.classList.replace('ligth', 'dark');

        logo[0].classList.replace('hidden', 'show');
        logo[1].classList.replace('show','hidden');

        localStorage.setItem('theme', body.classList);    
        
    } else{
        body.classList.replace('dark','ligth');

        logo[1].classList.replace('hidden', 'show');
        logo[0].classList.replace('show','hidden');

        localStorage.setItem('theme', body.classList);
    
    }
}


function navBar(){
    navbar.classList.toggle('active');
    navBarBtn.classList.toggle('active');
    pageContainer.classList.toggle('active');
    menu[0].classList.toggle('is-active');

    if (document.getElementById('auth')) {
        if(counter1 == 0){
            menu[1].innerText='MarketPlace';
            menu2[0].innerText='Perfil';
            menu2[1].innerText='Carrito';
            menu2[2].innerText='Cerrar Sesion';
            counter1++;    
    
        } else { 
            menu[1].innerText = 'M';
            menu2[0].innerText = 'P';
            menu2[1].innerText = 'C';
            menu2[2].innerText = 'CS';
            counter1--;
            
        }  
    } else {
        if(counter1 == 0){
            menu[1].innerText='MarketPlace';
            menu[2].innerText='Iniciar sesion';
            menu[3].innerText='Registrarse';
            counter1++;
    
    
        } else {
            
            menu[1].innerText = 'M';
            menu[2].innerText = 'I';
            menu[3].innerText = 'R';
            counter1--;
        }
    }    
}

function popUpCard(pos){
    popUp[pos-1].classList.toggle('show');
    pageContainer.classList.toggle('active');
}


function sliderMoveRight(){

    if (counter1 == 0){
        slider.style.setProperty('transform', move[1]); 
        counter1++;
        
    }else if (counter1 == 1){
        slider.style.setProperty('transform', move[2]); 
        counter1++;
        
    }else if (counter1 == 2){
        slider.style.setProperty('transform', move[3]); 
        counter1++;
        
    }   
            
}

function sliderMoveLeft(){

    if (counter1 == 1){
        slider.style.setProperty('transform', move[0]); 
        counter1 = counter1 - 1;
        
    }else if (counter1 == 2){
        slider.style.setProperty('transform', move[1]); 
        counter1 = counter1 - 1;
        
    }else if (counter1 == 3){
        slider.style.setProperty('transform', move[2]); 
        counter1 = counter1 - 1;
    }
     
}
