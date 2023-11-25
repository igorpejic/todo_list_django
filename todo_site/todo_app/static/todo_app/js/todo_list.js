document.addEventListener('DOMContentLoaded', function () {
    const csrftoken = getCookie('csrftoken');
    // Add a click event handler for the "Finish" button
    var finishBtns = document.querySelectorAll('.finish-btn');
    finishBtns.forEach(function (finishBtn) {
        finishBtn.addEventListener('click', function () {
            var todoId = finishBtn.getAttribute('data-todo-id');
            console.debug("Clicked on: " + todoId)
            fetch(`/toggle_todo_status/${todoId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                credentials: 'same-origin'
            })
                .then(function () {
                    location.reload();
                })
                .catch(function (error) {
                    // Handle any errors that occur during the API request, for now we just log.
                    console.error('Error:', error);
                });
        });
    });

    // Add a click event handler for the "Edit" button
    var editBtns = document.querySelectorAll('.edit-btn');
    editBtns.forEach(function (editBtn) {
        var todoId = editBtn.getAttribute('data-todo-id');
        editBtn.addEventListener('click', function () {
            window.location.href = `/todo/${todoId}/update`;
        });
    });
});