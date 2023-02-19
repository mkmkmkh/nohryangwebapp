const toogleBtn1 = document.querySelector('.map1_toogleBtn');
const toogleBtn2 = document.querySelector('.map2_toogleBtn');
const toogleBtn3 = document.querySelector('.map3_toogleBtn');
const toogleBtn4 = document.querySelector('.map4_toogleBtn');
const toogleBtn5 = document.querySelector('.map5_toogleBtn');
const toogleBtn6 = document.querySelector('.map6_toogleBtn');

const map1 = document.querySelector('.map1');
const map2 = document.querySelector('.map2');
const map3 = document.querySelector('.map3');
const map4 = document.querySelector('.map4');
const map5 = document.querySelector('.map5');
const map6 = document.querySelector('.map6');

toogleBtn1.addEventListener('click', () => {
    map1.classList.toggle('active');
})
toogleBtn2.addEventListener('click', () => {
    map2.classList.toggle('active');
})
toogleBtn3.addEventListener('click', () => {
    map3.classList.toggle('active');
})
toogleBtn4.addEventListener('click', () => {
    map4.classList.toggle('active');
})
toogleBtn5.addEventListener('click', () => {
    map5.classList.toggle('active');
})
toogleBtn6.addEventListener('click', () => {
    map6.classList.toggle('active');
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