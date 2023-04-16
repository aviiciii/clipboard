// dom content loaded
document.addEventListener("DOMContentLoaded", () => {

    // get the form
    const form = document.getElementById("save");

    // add event listener
    form.addEventListener("submit", (e) => {
        // prevent default behaviour
        e.preventDefault();

        // get the text
        const text = document.getElementById("text").value;

        // append the text to the local storage clipboard
        localStorage.setItem("clipboard", text);
    });

    // get the text
    const clipboard = localStorage.getItem("clipboard");

    console.log(clipboard);
    // add the text to the list group
    const listGroup = document.querySelector(".list-group");
    const listItem = document.createElement("li");
    listItem.classList.add("list-group-item", "d-flex", "justify-content-between", "align-items-center");
    listItem.innerHTML = clipboard;
    listGroup.appendChild(listItem);
    
});
