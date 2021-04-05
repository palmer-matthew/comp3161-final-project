window.onload = function(event){
    event.preventDefault();

    const $addrecbtn = document.querySelector('.add');



    $addrecbtn.addEventListener('click', (event) => {

        event.preventDefault();

        console.log('You added something');
        alert("CLick");

        
    });




    document.querySelector(".add_btn").addEventListener('click', function(event) {

        event.preventDefault();

        // let $recipe = false;
        // let $calories = false;
        // let $serving = false;
        // let $prep = false;
        // // Two missing fields 1: Image Upload
        // // 2: Select Ingredients
        // let $inst = false

        // let $recipe = document.getElementsByClassName("")
    })
}