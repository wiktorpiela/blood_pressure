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

// DELETE ITEM POPUP
const delPopups = document.querySelectorAll(".popup-delete")
const delBtns = document.querySelectorAll(".deleteItemBtns")

let i=0;
delBtns.forEach((delBtn) =>{

    let delPopup = delPopups[i];
    delBtn.addEventListener("click", ()=>{
        delPopup.classList.add("open-popup")
    })

    i++;
})

