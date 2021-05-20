window.navigator.geolocation.getCurrentPosition((position) => {
    console.log(position);
    const lat = document.querySelector("#lat");
    const lng = document.querySelector("#lng");
    lat.value = position.coords.latitude;
    lng.value = position.coords.longitude;
});