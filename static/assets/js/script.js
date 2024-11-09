

function downloadDiv(button, isSave=false) {
    // Traverse up the DOM to find the parent containing the target div
    let parentDiv = button.parentElement.parentElement;

    // Find the div with an ID starting with "t-"
    let targetDiv = Array.from(parentDiv.querySelectorAll("div")).find(div => div.id && div.id.startsWith("t-"));

    if (targetDiv) {
        // Use html2canvas to capture the targetDiv
        html2canvas(targetDiv).then(function (canvas) {
            // Create a download link and set the PNG as the source
            var link = document.createElement("a");
            link.href = canvas.toDataURL("image/png");
            link.download = "client_info.png";

            // Trigger the download
            link.click();

            if(isSave){
                console.log("saving image");
                // Send the image, client, and festival data to the API
                sendToAPI(canvas.toDataURL("image/png"));
            }
        });
    } else {
        console.error("Div with ID starting with 't-' not found.");
    }
}

function sendToAPI(imageData) {
    var selectedClient = 9;
    var selectedFestival = 6;
    
    // Convert Base64 image data to a Blob
    const byteCharacters = atob(imageData.split(',')[1]); // Remove the "data:image/png;base64," part
    const byteArrays = [];

    for (let offset = 0; offset < byteCharacters.length; offset += 1024) {
        const slice = byteCharacters.slice(offset, offset + 1024);
        const byteNumbers = new Array(slice.length);
        
        for (let i = 0; i < slice.length; i++) {
            byteNumbers[i] = slice.charCodeAt(i);
        }

        const byteArray = new Uint8Array(byteNumbers);
        byteArrays.push(byteArray);
    }

    const blob = new Blob(byteArrays, { type: 'image/png' });

    // Create FormData to send as multipart/form-data
    const formData = new FormData();
    formData.append('greeting_cards', blob, 'client_info.png');
    formData.append('client', selectedClient);
    formData.append('festival', selectedFestival);

    // Send the data to the API
    fetch('http://127.0.0.1:8000/api/greetings/', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (response.status === 201) {
            console.log("Saved successfully");
        } else {
            throw new Error(`Failed to save: ${response.statusText}`);
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}


function saveAndDownload(button) {
    // Any additional actions for saving, then download
    downloadDiv(button, true);
}