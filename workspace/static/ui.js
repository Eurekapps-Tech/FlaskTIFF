// Get HTML elements and create widgets if necessary

let contrast = document.getElementById("contrast_slider");
var SliderValueElement = document.getElementById('contrast_slider_value');

let overlay_slider = document.getElementById("overlay_slider");
var overlaySliderValueElement = document.getElementById('overlay_slider_value');

let channel = document.getElementById('channel_slider');
let overlay = document.getElementById('overlay');


noUiSlider.create(contrast, {
    start: [100, 65535],
    connect: [true, false, true],
    margin: 1,
    // tooltips: [true, true],
    range: {
        min: 0,
        max: 65535,
    },
    // step: 1,
    format: {
        to: function (value) {
            return Math.round(value);
        },
        from: function (value) {
            return value.replace(',_', '');
        }
    }
});


contrast.noUiSlider.on('update', function (values) {
    SliderValueElement.innerHTML = values.join(' - ');
});

noUiSlider.create(overlay_slider, {
    start: [0, 6535],
    connect: [true, false, true],
    margin: 1,
    // tooltips: [true, true],
    range: {
        min: 0,
        max: 65535,
    },
    // step: 1,
    format: {
        to: function (value) {
            return Math.round(value);
        },
        from: function (value) {
            return value.replace(',_', '');
        }
    }
});

overlay_slider.noUiSlider.on('update', function (values) {
    overlaySliderValueElement.innerHTML = values.join(' - ');
});