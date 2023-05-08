addEventListener("DOMContentLoaded", () => {
    // listen of the form submit
    const formButton = document.querySelector("#submit");
    formButton.addEventListener("click", (e) => {
        e.preventDefault();

        // get the form
        const id = document.querySelector("#number");

        // check if id is empty
        if (id.value.trim() === "") {
            alert("Please enter a number");
        }
        // check if id is a number
        else{
            // post id to api using get
            // let url = `https://aviiciii-clipboard.azurewebsites.net/delete/${id.value.trim()}`;
            let url = `http://127.0.0.1:5000/delete/${id.value.trim()}`;
            fetch(url, {
                method: "GET"
            })
            .then(response => {
                console.log(response);
            })
            .catch(error => {
                console.log(error);
            }
            );
            alert("Clipboard deleted");
            // clear the form
            id.value = "";

        }

    });
});