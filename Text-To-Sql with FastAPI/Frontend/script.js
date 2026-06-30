const API_URL = "http://127.0.0.1:8000/api/v1/chat";

async function sendQuestion() {

    const input = document.getElementById("question");
    const question = input.value.trim();

    if(question==="")
        return;

    const chatBox = document.getElementById("chat-box");

    // User Message

    chatBox.innerHTML += `
        <div class="user-message">
            ${question}
        </div>
    `;

    input.value="";

    // Loading

    const loading = document.createElement("div");

    loading.className="loading";

    loading.innerHTML="🤖 Thinking...";

    chatBox.appendChild(loading);

    chatBox.scrollTop=chatBox.scrollHeight;

    try{

        const response = await fetch(API_URL,{

            method:"POST",

            headers:{
                "Content-Type":"application/json",
                "accept":"application/json"
            },

            body:JSON.stringify({
                question:question
            })

        });

        const data = await response.json();

        loading.remove();

        chatBox.innerHTML += `

        <div class="bot-message">

            <b>Generated SQL</b>

            <div class="sql">

${data.data.sql}

            </div>

            <div class="answer">

                <b>Answer</b>

                <br><br>

                ${data.data.answer}

            </div>

        </div>

        `;

        chatBox.scrollTop=chatBox.scrollHeight;

    }
    catch(err){

        loading.remove();

        chatBox.innerHTML += `
            <div class="bot-message">

                Error calling API.

            </div>
        `;

        console.log(err);

    }

}

// Press Enter

document
.getElementById("question")
.addEventListener("keypress",function(event){

    if(event.key==="Enter"){

        sendQuestion();

    }

});