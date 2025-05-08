function isValidURL(string) {
    var res = string.match(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g);
    return (res !== null)
};

function clearInput() {
    document.getElementById("url-input").value = "";
};

function showResult(shortUrl) {
    document.getElementById('short-url').textContent = shortUrl;
    document.getElementById('short-url').href = shortUrl;
    document.getElementById('result').style.display = "inline";
};

function copyTxtShort() {
    // Get the text field
    var copyText = document.getElementById("short-url");

    // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.href);
};

function short_url() {
    url_input = document.getElementById("url-input").value;

    if( isValidURL(url_input) == false ){
        clearInput();
        alert("Digite uma URL válida!");
        return false;
    }
    
    fetch('/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url_input })
    })
    .then(response => {
        if(response.status == 200){
            return response.json(); 
        } else {
            throw new Error(`Erro HTTP: ${response.status}`);
        }
    })
    .then(data_return => {
        shortUrl = data_return.shortUrl;
        idUrl = data_return.idUrl;

        // Showing the div with the result:
        showResult(shortUrl);
    })
    .catch(error => {
        console.log("Erro:", error);
    });
};