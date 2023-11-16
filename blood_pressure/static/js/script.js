// ADD NEW ITEM FORM POPUP
const popup = document.querySelector(".popup")
const addBtn = document.querySelector(".addBtn")
const cancelBtn = document.querySelector(".cancelBtn")

addBtn.addEventListener("click", ()=>{
    popup.classList.add("open-popup")
})

cancelBtn.addEventListener("click", ()=>{
    popup.classList.remove("open-popup")
})

