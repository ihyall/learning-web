// const button = document.querySelector("button");
// const textarea = document.querySelector("textarea");
// const textbox = document.getElementById("textbox");

// button.addEventListener("click", updateTextBox);

// function updateTextBox() {
//     const text = textarea.value;
//     textbox.textContent = text;
// }



const button1 = document.getElementById("button1");
const button2 = document.getElementById("button2");
const textarea = document.querySelector("textarea");
const textbox = document.getElementById("textbox");


button1.addEventListener("click", updateTextBox);
button2.addEventListener("click", getAPIResponse);

function updateTextBox() {
    const text = textarea.value;
    textbox.textContent = text;
}

async function getAPIResponse() {
    let url = 'http://127.0.0.1:8000/';
    let response = await fetch(url);

    console.log(response);

    if (response.ok) { // если HTTP-статус в диапазоне 200-299
    // получаем тело ответа (см. про этот метод ниже)
    let json = await response.json();
    console.log(json);
    } else {
    alert("Ошибка HTTP: " + response.status);
    }
}