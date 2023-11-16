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
const goBackBtns = document.querySelectorAll(".goBackBtns")

let i=0;
delBtns.forEach((delBtn) =>{

    let delPopup = delPopups[i];
    let goBackBtn = goBackBtns[i];

    delBtn.addEventListener("click", ()=>{
        delPopup.classList.add("open-popup")
    })

    goBackBtn.addEventListener("click", ()=>{
        delPopup.classList.remove("open-popup")
    })

    i++;
})

// edit ITEM POPUP
const editPopups = document.querySelectorAll(".popup-edit")
const editBtns = document.querySelectorAll(".editItemBtns")
const cancelEditBtns = document.querySelectorAll(".cancelEditBtns")

let j=0;
editBtns.forEach((editBtn) =>{

    let editPopup = editPopups[j];
    let cancelEditBtn = cancelEditBtns[j];

    editBtn.addEventListener("click", ()=>{
        editPopup.classList.add("open-popup")
    })

    cancelEditBtn.addEventListener("click", ()=>{
        editPopup.classList.remove("open-popup")
    })

    j++;
})

