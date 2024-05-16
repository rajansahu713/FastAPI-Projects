// static/script.js

function deleteTask(index) {
    fetch("/delete-task/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `task_index=${index}`,
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload(); // Reload page to reflect changes
    })
    .catch(error => console.error("Error:", error));
}
