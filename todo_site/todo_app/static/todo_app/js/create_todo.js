document.addEventListener('DOMContentLoaded', function () {
    // Add a click event handler for the "Finish" button
    const countrySelect = document.getElementById('id_country');
    const citySelect = document.getElementById('id_city');

    // Handle country dropdown change event
    countrySelect.addEventListener('change', function () {
        const countryId = this.value;
        // Clear city dropdown
        citySelect.innerHTML = '<option value="">Select a city</option>';
        if (countryId) {
            // Make an AJAX request to fetch cities based on the selected country
            fetch(`/get_cities/?country_id=${countryId}`, { credentials: 'same-origin' })
                .then(response => response.json())
                .then(data => {
                    data?.cities.forEach(city => {
                        const option = document.createElement('option');
                        option.value = city.id;
                        option.textContent = city.name;
                        citySelect.appendChild(option);
                    });
                })
                .catch(error => {
                    console.error('Error fetching cities:', error);
                });
        }
    });
});