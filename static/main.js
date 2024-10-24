const cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad'];

async function fetchWeatherData() {
    const weatherDisplay = document.getElementById('weatherDisplay');
    weatherDisplay.innerHTML = ''; // Clear previous data
    const unit = document.getElementById('temp-unit').value;

    for (const city of cities) {
        try {
            const response = await fetch(`/api/weather/${city}`);
            if (!response.ok) throw new Error(`Error fetching weather for ${city}`);
            const weather = await response.json();

            // Convert temperature based on user preference
            const temp = unit === 'C' ? Math.round(weather.temp - 273.15) : Math.round((weather.temp - 273.15) * 9/5 + 32);
            const feelsLike = unit === 'C' ? Math.round(weather.feels_like - 273.15) : Math.round((weather.feels_like - 273.15) * 9/5 + 32);
            const tempUnit = unit === 'C' ? '°C' : '°F';

            const card = `
                <div class="weather-card">
                    <h5 class="card-title">${weather.city}</h5>
                    <p class="card-text">Temperature: ${temp} ${tempUnit}</p>
                    <p class="card-text">Feels Like: ${feelsLike} ${tempUnit}</p>
                    <p class="card-text">Condition: ${weather.condition}</p>
                    <p class="card-text">Last Updated: ${new Date(weather.timestamp * 1000).toLocaleString()}</p>
                </div>
            `;
            weatherDisplay.innerHTML += card;
        } catch (error) {
            console.error(error);
            weatherDisplay.innerHTML += `<p>Error fetching weather for ${city}</p>`;
        }
    }
}

async function getWeather() {
    const apiKey = 'fa2bb54898a54fa40789305a253b0fda';
    const city = document.getElementById('city').value;
    const unit = document.getElementById('temp-unit').value;

    if (!city) {
        alert('Please enter a city');
        return;
    }

    const currentWeatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;
    const forecastUrl = `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${apiKey}`;

    try {
        const currentWeatherResponse = await fetch(currentWeatherUrl);
        const currentWeatherData = await currentWeatherResponse.json();
        displayWeather(currentWeatherData, unit);

        const forecastResponse = await fetch(forecastUrl);
        const forecastData = await forecastResponse.json();
        displayHourlyForecast(forecastData.list, unit);
    } catch (error) {
        console.error('Error fetching weather data:', error);
        alert('Error fetching weather data. Please try again.');
    }
}

function displayWeather(data, unit) {
    const tempDivInfo = document.getElementById('temp-div');
    const weatherInfoDiv = document.getElementById('weather-info');
    const weatherIcon = document.getElementById('weather-icon');
    const hourlyForecastDiv = document.getElementById('hourly-forecast');

    // Clear previous content
    weatherInfoDiv.innerHTML = '';
    hourlyForecastDiv.innerHTML = '';
    tempDivInfo.innerHTML = '';

    if (data.cod === '404') {
        weatherInfoDiv.innerHTML = `<p>${data.message}</p>`;
    } else {
        const cityName = data.name;
        const temperature = unit === 'C' ? Math.round(data.main.temp - 273.15) : Math.round((data.main.temp - 273.15) * 9/5 + 32);
        const tempUnit = unit === 'C' ? '°C' : '°F';
        const description = data.weather[0].description;
        const iconCode = data.weather[0].icon;
        const iconUrl = `https://openweathermap.org/img/wn/${iconCode}@4x.png`;

        const temperatureHTML = `<p>${temperature}${tempUnit}</p>`;
        const weatherHtml = `<p>${cityName}</p><p>${description}</p>`;

        tempDivInfo.innerHTML = temperatureHTML;
        weatherInfoDiv.innerHTML = weatherHtml;
        weatherIcon.src = iconUrl;
        weatherIcon.alt = description;

        showImage();
    }
}

function displayHourlyForecast(hourlyData, unit) {
    const hourlyForecastDiv = document.getElementById('hourly-forecast');
    const next24Hours = hourlyData.slice(0, 8); // Display the next 24 hours (3-hour intervals)

    next24Hours.forEach(item => {
        const dateTime = new Date(item.dt * 1000); // Convert timestamp to milliseconds
        const hour = dateTime.getHours();
        const temperature = unit === 'C' ? Math.round(item.main.temp - 273.15) : Math.round((item.main.temp - 273.15) * 9/5 + 32);
        const tempUnit = unit === 'C' ? '°C' : '°F';
        const iconCode = item.weather[0].icon;
        const iconUrl = `https://openweathermap.org/img/wn/${iconCode}.png`;

        const hourlyItemHtml = `
            <div class="hourly-item">
                <span>${hour}:00</span>
                <img src="${iconUrl}" alt="Hourly Weather Icon">
                <span>${temperature}${tempUnit}</span>
            </div>
        `;

        hourlyForecastDiv.innerHTML += hourlyItemHtml;
    });
}

function showImage() {
    const weatherIcon = document.getElementById('weather-icon');
    weatherIcon.style.display = 'block'; // Make the image visible once it's loaded
}

// Call fetchWeatherData on page load to populate the city weather cards
fetchWeatherData();
