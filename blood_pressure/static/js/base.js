const start = new Date(document.querySelector(".start_date").value);
const end = new Date(document.querySelector(".end_date").value);
const filter = document.querySelector(".filterBtn");

filter.addEventListener("click", ()=>{
    console.log("hello")
    console.log(start.getDate())
    console.log(end.getDate())
    if(start.getTime() < end.getTime()){
        console.log("wrong")
    }
    
})

