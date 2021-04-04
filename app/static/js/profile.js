window.onload = function(event){
    event.preventDefault();

    const addbtn = document.querySelector('.add');
    const input = document.querySelector('.hidden');
    const closebtn = document.querySelector('.x');

    addbtn.addEventListener('click', (event) => {

        event.preventDefault();

        console.log('Add Button was clicked');

        input.classList.add('active');
    });

    closebtn.addEventListener('click', (event) =>{

        event.preventDefault();
        
        input.classList.remove('active');

    });

}