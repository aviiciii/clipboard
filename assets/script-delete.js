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
            
            let headers = new Headers();
            headers.append('Access-Control-Allow-Origin', '*');
            headers.append('Access-Control-Allow-Credentials', 'true');
            headers.append('Access-Control-Allow-Methods', 'GET,HEAD,OPTIONS,POST,PUT');
            headers.append('Access-Control-Allow-Headers', 'Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers');
            
            fetch (url, {method: 'GET', headers: headers})
            .then(response => response.json())
            .then(data => {
                console.log(data);
                alert(data.msg);
            })
            
            
            deleteClipboard.then(data => {
                // print response message

                console.log(data);
                // if (data.status === 200) {
                //     alert("Clipboard deleted");
                // }
                // else if (response.status === 404) {
                //     alert("Clipboard not found");
                // }
                // else {
                //     alert("Something went wrong");
                // }
            })
            .catch(error => {
                console.log(error);
            }
            );

            
            
            // clear the form
            id.value = "";

        }

    });
});