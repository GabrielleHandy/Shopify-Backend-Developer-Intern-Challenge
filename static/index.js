function changeToClose(event){
let button = event.target;

if (button.innerText === "See Items"){
    button.innerText = "Close";
}
else{
    button.innerText = "See Items";
}
};


function deleteShip(id){

const answer= confirm(`Are you sure you want to delete this Shipment: ${id}?`);
if (answer === true){
    const ship_id = id;
    

    const param = {'ship_id': ship_id}
            
    const options = {
    method: 'POST',
    body: JSON.stringify( param ),  
    headers: {
        'Content-Type': 'application/json'
            }
    };

    fetch("/delete_ship", options)
    .then(data => data.json())
    .then(deleteAlert())
    
}

};



// delete an inventory item
const deleteItemForm = document.querySelector("#deleteitem_inventory");

deleteItemForm.addEventListener('submit', function(e){
    e.preventDefault()
    let item_id = document.querySelector("#item_choice").value;
    deleteItemInventory(item_id);
});





function deleteItemInventory(item_id){

    let answer= confirm(`Are you sure you want to delete this item`);
    if (answer === true){
        const param = {'item_id': item_id}
                
        const options = {
        method: 'POST',
        body: JSON.stringify( param ),  
        headers: {
            'Content-Type': 'application/json'
                }
        };

        fetch("/deleteitem", options)
        .then(data => data.json())
        .then(deleteAlert())
        
    }

    };


function deleteAlert()
{
    let alert = document.querySelector("#Alert");
    let link = window.location.href;
    let message = `Deleted Sucessfully! click <a href= "${link}" class='alert-link'>here</a> to refresh the page!`;
    return alert.innerHTML = '<div class="alert alert-success alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'
};



// Call to delete items in Shipment
function showDelete(event){
    let btn = event.target;
    let text = btn.innerText;
    const listOfItems = document.querySelectorAll(".list_of_items");
    

    

    if (text === 'Cancel delete'){
        btn.innerHTML= "Delete an Item";
        let item_buttons =  document.querySelectorAll(".deleteItemBtn")
        
        while(item_buttons.length > 0){
            for(itemBtn of item_buttons){
               itemBtn.parentNode.removeChild(itemBtn);
            } 
            }
            

    }
    else{
        btn.innerHTML= 'Cancel delete';
        for (item of listOfItems){
            let id = item.getAttribute('delBtnId');
            item.insertAdjacentHTML('beforeEnd', `<button class="deleteItemBtn " id =${id} onclick ="deletItemShip(this, this.id);">Delete</button>`);
        }
    }
};

// Call to edit items in Inventory
function showEdit(id, event){
    let btn = event.target;
    let text = btn.innerText;
    let nameId =`${id}-name`;
    let name = document.getElementById(`${nameId}`);
    let desc = document.getElementById(`${id}-desc`);
    let qty = document.getElementById(`${id}-quantity`);
   
    

    

    if (text === 'Cancel edit'){
        btn.innerHTML= "Edit";
        let nameForm = document.querySelector('#name_form');
        let descForm = document.querySelector('#desc_form');
        let qtyForm = document.querySelector('#qty_form');
        nameForm.remove();
        descForm.remove();
        qtyForm.remove();
        
       
            

    }
    else{
        btn.innerHTML= 'Cancel edit';
        name.insertAdjacentHTML("beforeend", 
        `<form action='/edit_inventory' id='name_form' method='post'>\
        <input style="visibility: hidden; width: 1px;" name='id' type='text' value=${id}>
        <input name='new_name' type='text'>\
        <input type='submit' value='save'>`);
        
        desc.insertAdjacentHTML("beforeend", 
        `<form action='/edit_inventory' id='desc_form' method='post'>\
        <input style="visibility: hidden; width: 1px;" name='id' type='text' value=${id}>
        <textarea name='new_desc' type='text'></textarea>\
        <input type='submit' value='save'>`);

        qty.insertAdjacentHTML("beforeend", 
        `<form action='/edit_inventory' id='qty_form' method='post'>\
        <input style="visibility: hidden; width: 1px;" name='id' type='text' value=${id}>
        <input name='new_qty' type='number' min='1'>\
        <input type='submit' value='save'>`);
    }
};










function addFormShipId(ship_id){
    const shipIdValue = document.querySelector('#ship_id');

    shipIdValue.value = ship_id;

}

function deletItemShip(btn, id){
    let item_id = id;
    let answer= confirm("Are you sure you want to delete this Item?");
    if (answer === true){
        let alert = document.querySelector("#Alert");
        let ship_id = btn.parentNode.getAttribute('data-value');
        
        const param = {'item_id': item_id,
                        'ship_id': ship_id}
                
        const options = {
        method: 'POST',
        body: JSON.stringify( param ),  
        headers: {
            'Content-Type': 'application/json'
                }
        };

        fetch("/delete_item_ship", options)
        .then(data => data.json())
        .then(alert.innerHTML = '<div class="alert alert-success alert-dismissible" role="alert">Deleted Sucessfully!<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    
    

}






