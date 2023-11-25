document.addEventListener('DOMContentLoaded', function () {
    // Add a click event handler for the "Finish" button
    var finishBtns = document.querySelectorAll('.finish-btn');
    finishBtns.forEach(function (finishBtn) {
        finishBtn.addEventListener('click', function () {
            var todoId = finishBtn.getAttribute('data-todo-id');
            console.debug("Clicked on: " + todoId)
            fetch('/change_todo_status/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    todo_id: todoId,
                    status: 'finished',
                }),
            })
                .then(function (response) {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(function (data) {
                    // TODO: change status
                    alert('Todo status changed to finished');
                })
                .catch(function (error) {
                    // Handle any errors that occur during the API request
                    console.error('Error:', error);
                });
        });

        // Add a click event handler for the "Edit" button
        var editBtns = document.querySelectorAll('.edit-btn');
        editBtns.forEach(function (editBtn) {
            var todoId = finishBtn.getAttribute('data-todo-id');
            editBtn.addEventListener('click', function () {
                window.location.href = '/create_todo/' + todoId;
            });
        });
    })
});