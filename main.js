const toogleBtn1 = document.querySelector('.map1_toogleBtn');
const toogleBtn2 = document.querySelector('.map2_toogleBtn');
const toogleBtn3 = document.querySelector('.map3_toogleBtn');
const map1 = document.querySelector('.map1');
const map2 = document.querySelector('.map2');
const map3 = document.querySelector('.map3');

toogleBtn1.addEventListener('click', () => {
    map1.classList.toggle('active');
})
toogleBtn2.addEventListener('click', () => {
    map2.classList.toggle('active');
})
toogleBtn3.addEventListener('click', () => {
    map3.classList.toggle('active');
})

function initMap() {
    // The location of Uluru
    const uluru = { lat: -25.344, lng: 131.031 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: uluru,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
        position: uluru,
        map: map,
    });
}

window.initMap = initMap;