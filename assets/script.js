// dom content loaded
document.addEventListener("DOMContentLoaded", () => {

    // get existing clipboards from api
    const getClipboards = async () => {
        fetch('https://aviiciii-clipboard.azurewebsites.net/api', {method: 'GET'})
        .then(res => res.json())
        .then(console.log)
    }
    console.log(getClipboards());
    
});
