from flask import Flask, render_template, request
from flask.json import jsonify
import utils

app = Flask(__name__)

@app.route('/')
def index():
    # Read the TIFF file
    tiff_data = utils.read_tiff('workspace/test.tif')
    np_tiff_data = utils.map_uint16_to_uint8(tiff_data, 0, 65535)
    img = utils.numpy_to_b64_string(np_tiff_data)
    # Get the first channel image
    # channel_image = get_channel_image(tiff_data, 0)
    
    # Render the HTML template with the channel image and number of channels
    return render_template('index.html', channel_image=img, num_channels=3)

@app.route('/channel', methods=['POST'])
def channel():
    # Get the selected channel from the slider
    channel = int(request.form['channel'])
    contrast = [int(float(value)) for value in request.form['contrast'].split(',')]
    overlay_contrast = [int(float(value)) for value in request.form['overlay_contrast'].split(',')]
    overlay = request.form['overlay']
    # print(overlay)


    tiff_data = utils.read_tiff('test.tif', channel=channel)
    np_tiff_data = utils.map_uint16_to_uint8(tiff_data, contrast[0], contrast[1])
    channel_image = utils.numpy_to_b64_string(np_tiff_data)

    if overlay == 'true':
        channel_image = utils.extract_overlay('workspace/test.tif', contrast[0], contrast[1], overlay_contrast[0], overlay_contrast[1], path=True)
        channel_image = utils.numpy_to_b64_string(channel_image)

    
#     # Return the selected channel image as a response
    return jsonify({'channel_image': channel_image})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)

