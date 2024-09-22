let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let jsonResponse = JSON.parse(xhttp.responseText);
            document.getElementById("system_response").innerHTML = jsonResponse.response;
        } else if (this.readyState == 4 && this.status == 400) {
            let jsonResponse = JSON.parse(xhttp.responseText);
            document.getElementById("system_response").innerHTML = jsonResponse.error;
        }
    };
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}
