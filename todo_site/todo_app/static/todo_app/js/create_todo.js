document.addEventListener('DOMContentLoaded', function () {
    // Add a click event handler for the "Finish" button
    function fetchCities(countryId) {
        citySelect.innerHTML = '<option value="">Select a city</option>';
        if (!countryId) {
            return
        }
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
    function fetchCityTemperature(cityId) {
        fetch(`/get_city_temperature?city_id=${cityId}`, { credentials: 'same-origin' })
            .then(response => response.json())
            .then(data => {
                document.getElementById('create-task-wrapper').style.backgroundColor = data.color_code;

                const tempWrapper = document.getElementById('temperature-wrapper');
                while (tempWrapper.firstChild) {
                    tempWrapper.removeChild(tempWrapper.firstChild);
                }
                const newTextElement = document.createTextNode(`Temperature: ${data.temperature}`);
                tempWrapper.appendChild(newTextElement);
            })
            .catch(error => {
                console.error('Error fetching cities:', error);
            });

    }
    const countrySelect = document.getElementById('id_country');
    const citySelect = document.getElementById('id_city');
    const selectedCityId = citySelect.value;
    if (selectedCityId) {
        // On initial load and if city is loaded fetch its temperature
        fetchCityTemperature(selectedCityId)
    }

    // Handle country dropdown change event
    countrySelect.addEventListener('change', function () {
        const countryId = this.value;
        fetchCities(countryId)

    });
    citySelect.addEventListener('change', function () {
        const cityId = this.value;
        if (!cityId) {
            return;
        }
        fetchCityTemperature(cityId);
    });
});