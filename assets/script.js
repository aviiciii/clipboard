// dom content loaded
document.addEventListener("DOMContentLoaded", () => {

    // get existing clipboards from api and return them
    const getClipboards = async () => {

        let headers = new Headers();
        headers.append('Access-Control-Allow-Origin', '*');
        headers.append('Access-Control-Allow-Credentials', 'true');
        headers.append('Access-Control-Allow-Methods', 'GET,HEAD,OPTIONS,POST,PUT');
        headers.append('Access-Control-Allow-Headers', 'Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers');
        
        const response = await fetch("https://aviiciii-clipboard.azurewebsites.net/api", {method: 'GET', headers: headers});
        const data = await response.json();
        return data;
    };

    getClipboards().then(data => {
        var clipboards = data;
        var clips = Object.values(clipboards);

        console.log(clips);

        // get the clipboard list group
        const clipboardListItem = document.querySelector(".list-group");

        // loop through the clipboards and add them to the list
        for (let i = 0; i < clips.length; i++) {
            console.log(i);
            console.log(clips[i]);
            const clipboard = clips[i];

            // create the list item
            const listItem = createClipboardListItem(clipboard);


        }
        // remove loading list item
        const loading = document.querySelector("#loading");
        loading.remove();

    });

    // get the form button and add event listener
    const formButton = document.querySelector("#submit");

    formButton.addEventListener("click", (e) => {
        e.preventDefault();

        // get the form
        const content = document.querySelector("#text");

        // data to send to api
        const data = {
            "body": content.value.trim()
        };
        
        // post the clipboard to the api
        fetch("https://aviiciii-clipboard.azurewebsites.net/api", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            console.log(response);
        })
        .catch(error => {
            console.log(error);
        });

        // clear the form
        content.value = "";

        // add the clipboard to the list
        createClipboardListItem(data.body);

    });


    // copy to clipboard
    document.addEventListener("click", (e) => {
        // check if the target is the copy button by class containing copy-to-clipboard
        if (e.target.classList.contains("copy-to-clipboard-button") ) {

            // get the clipboard text
            const clipboardText = e.target.parentElement.innerText;

            // save to clipboard
            navigator.clipboard.writeText(clipboardText).then(() => {
            });


        }
        else if (e.target.classList.contains("copy-to-clipboard-img")) {

            // get the clipboard text
            const clipboardText = e.target.parentElement.parentElement.innerText;

            // save to clipboard
            navigator.clipboard.writeText(clipboardText).then(() => {
                console.log("copied to clipboard");
            });
        }

    });


    // create a clipboard list item
    const createClipboardListItem = (clipboard) => {
        // create the list item
        const listItem = document.createElement("li");
        listItem.className = "list-group-item d-flex justify-content-between align-items-center";
        listItem.innerHTML = clipboard;

        // add button to list item
        const button = document.createElement("button");
        button.className = "badge rounded-pill copy-to-clipboard-button";

        // add img to span
        const img = document.createElement("img");
        img.src = "https://img.icons8.com/fluency-systems-regular/96/null/clipboard.png";
        img.className = "img-fluid";
        img.alt = "copy";
        img.className = "copy-to-clipboard-img";
        button.appendChild(img);

        // add span to list item
        listItem.appendChild(button);

        // add list item to list
        const clipboardListItem = document.querySelector(".list-group");
        clipboardListItem.appendChild(listItem);


        return listItem;
    }

    
});
