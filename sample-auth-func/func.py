import io
import oci
import base64
import json
import logging

from fdk import response

signer = oci.auth.signers.get_resource_principals_signer()
client = oci.secrets.SecretsClient({}, signer=signer)

def get_text_secret(secret_ocid):
    get_secret = client.get_secret_bundle(secret_ocid).data.secret_bundle_content.content.encode('utf-8')
    decrypt_secret = base64.b64decode(get_secret).decode("utf-8")
    logging.getLogger().info(get_secret)
    return {"secret content": decrypt_secret}

def handler(ctx, data: io.BytesIO = None):
    logging.getLogger().info("function start")

    secret_ocid = secret_type = ""
    try:
        cfg = dict(ctx.Config())
        secret_ocid = cfg["secret_ocid"]
        logging.getLogger().info("Secret ocid = " + secret_ocid)
    except Exception as e:
        print('ERROR: Missing configuration keys, secret ocid and secret_type', e, flush=True)
        raise

    secret_text = json.dumps(get_text_secret(secret_ocid))
    logging.getLogger().debug("secret detail")
    logging.getLogger().debug(secret_text)

    logging.getLogger().debug("Inside Python Hello World function")
    return response.Response(
        ctx, response_data=secret_text,
        headers={"Content-Type": "application/json"}
    )
