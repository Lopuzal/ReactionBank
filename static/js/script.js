document.addEventListener('paste', function (evt) {
    // Get the data of clipboard
    const clipboardItems = evt.clipboardData.items;
    const items = [].slice.call(clipboardItems).filter(function (item) {
        // Filter the image items only
        return item.type.indexOf('image') !== -1;
    });
    if (items.length === 0) {
        return;
    }

    const item = items[0];
    // Get the blob of image
    const blob = item.getAsFile();

    
    const imageEle = document.getElementById('preview');
    imageEle.src = URL.createObjectURL(blob);

    // Create a new FormData
    const formData = new FormData();
    formData.append('image', blob, 'filename');

    // Create new Ajax request
    const req = new XMLHttpRequest();
    req.open('POST', '/', true);

    // Send it
    req.send(formData);
});