async function predict() {

    const response = await fetch("https://real-estate-ml-s1f5.onrender.com/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            unit_area: parseFloat(document.getElementById("area").value),
            total_rooms: parseInt(document.getElementById("rooms").value),
            bathrooms: parseInt(document.getElementById("bathrooms").value)
        })
    });

    const data = await response.json();

    document.getElementById("result").innerText =
        "Predicted Rent: ₹" + data.prediction;
}