const API_URL = "https://vercel.com/snikers/sneakers";

async function loadSneakers() {
    try {
        const response = await fetch(`${API_URL}/sneakers`);
        const data = await response.json();
        displaySneakers(data.sneakers);
    } catch (error) {
        console.error(error);
        document.getElementById("sneakerList").innerHTML = "Unable to connect to the API.";
    }
}

// DISPLAY SNEAKERS
function displaySneakers(sneakers) {
    const sneakerList = document.getElementById("sneakerList");
    sneakerList.innerHTML = "";

    sneakers.forEach(sneaker => {
        const card = document.createElement("div");
        card.className = "sneaker-card";
        card.innerHTML = `
            <div class="sneaker-year">${sneaker.release_year}</div>
            <h3>${sneaker.brand} ${sneaker.model}</h3>
            <p class="sneaker-colorway">${sneaker.colorway}</p>
            <p>$${sneaker.price}</p>
            <p>${sneaker.description}</p>
            <button onclick="viewSneaker(${sneaker.id})">View Details</button>
        `;

        sneakerList.appendChild(card);
    });
}

// GET ONE SNEAKER
async function viewSneaker(id) {
    try {
        const response = await fetch(`${API_URL}/sneakers/${id}`);
        const sneaker = await response.json();

        alert(`
            ${sneaker.brand} ${sneaker.model} (${sneaker.release_year})
            Colorway:
            ${sneaker.colorway}

            Price:
            $${sneaker.price}

            Description:
            ${sneaker.description}
        `);
    } catch (error) {
        console.error(error);
        alert("Unable to retrieve sneaker.");
    }
}

// SEARCH
async function searchSneakers() {
    const query = document.getElementById("searchInput").value;
    if (!query) {
        loadSneakers();
        return;
    }
    try {
        const response = await fetch(`${API_URL}/sneakers/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        displaySneakers(data.results);
    } catch (error) {
        console.error(error);
        alert("Search failed.");
    }
}

loadSneakers();