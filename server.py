from flask import Flask, render_template, request, redirect, jsonify
from src.monKeyData.DataGenerators.MonKeyDataGenerator import MonKeyDataGenerator
from src.monKeyVisual.ImageGenerator import ImageGenerator
from flask_s3 import FlaskS3
from flask_cors import CORS
import re, os, boto3, warnings
from botocore.client import Config
from botocore.exceptions import ClientError


warnings.filterwarnings("ignore")

def is_a_banano_address(address):

    pattern = '^ban_[13][013-9a-km-uw-z]{59}$'
    match = re.match(pattern, address, flags=0)
    return match is not None


def connect_to_s3_bucket():

    s3_resource = boto3.resource(
        's3',
        aws_access_key_id=os.environ.get('AWS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'),
        config=Config(signature_version='s3v4')
    )

    return s3_resource


def file_exists_in_s3_bucket(file_name):

    try:
        s3_resource.Object('bananomonkeys', file_name).load()
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            return False
        else:
            # Something else has gone wrong.
            raise
    else:
        return True


monkey_data_generator = MonKeyDataGenerator()
monkey_image_generator = ImageGenerator()

app = Flask(__name__)
app.config['FLASKS3_BUCKET_NAME'] = os.environ.get('S3_BUCKET_NAMEING')
app.config['USE_S3_DEBUG'] = True
s3 = FlaskS3(app)
s3_resource = connect_to_s3_bucket()
CORS(app)


@app.route("/")
def address():
    return render_template('home.html')

# ==================METADATA API==================

@app.route("/api")
def get_monkey_api():
    banano_address = request.args.get('address', None)
    if banano_address and is_a_banano_address(banano_address):
        return monkey_api(banano_address)
    else:
        return render_template("NotABananoAddress.html"), 400

@app.route("/api/<address>")
def monkey_api(address):
    if address and is_a_banano_address(address):
        monKey = monkey_data_generator.generate_monKey(address)
        if monKey.status is not 'Citizen':
            return "API data on vanity monKeys does not exist"
        return jsonify(monKey.serialize())
    else:
        return render_template("NotABananoAddress.html"), 400

# ==================IMAGE API==================

@app.route('/image', methods=['GET'])
def get_monkey_image():
    banano_address = request.args.get('address', None)
    background = request.args.get('bg', 'nobg')
    format = request.args.get('format', 'svg')
    accesories = request.args.get('acc', 'full')
    if banano_address and is_a_banano_address(banano_address):
        return monkey_image(banano_address, background, accesories, format)
    else:
        return render_template("NotABananoAddress.html"), 400


@app.route('/image/<accesories>/<format>/<background>/<address>', methods=['GET'])
def monkey_image(address, background='nobg', accesories='full', format='svg'):
    path = 'images/' + format + '/' + 'monKeys/' + background + '/' + format + accesories + 'monKey-' + address + '.' + format
    s3_bucket_key = 'static/' + path
    # if a monkey image does not exist, generate it and upload it to the s3 bucket
    if not file_exists_in_s3_bucket(s3_bucket_key):
        monKey = monkey_data_generator.generate_monKey(address)
        if monKey.status is 'Citizen':
            monKey_image = monkey_image_generator.generate_monKey_image(monKey, background, format, accesories)
            content_type = 'image/svg+xml'
            if format == 'png':
                content_type = 'image/png'
            s3_resource.Bucket(os.environ.get('S3_BUCKET_NAMEING')).put_object(Key=s3_bucket_key, Body=monKey_image, ACL='public-read', ContentType=content_type, ContentDisposition='inline', ContentLength=len(monKey_image), CacheControl='max-age=604800')
        # This is a rigged/vanity address
        else:
            path = 'images/' + format + '/vanity/Vanity-' + address + '.' + format
    # For non cloudfront serving: return redirect(url_for('static', filename=path))
    # Retrieve the image from cloudfront
    return redirect('https://d3tynpbz5c31ci.cloudfront.net/static/' + path)


if __name__ == "__main__":
    app.run(debug=True)
