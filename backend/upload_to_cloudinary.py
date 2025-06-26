import cloudinary
import cloudinary.uploader
from io import BytesIO

cloudinary.config(
  cloud_name="dip9yp9kg",
  api_key="639352329466436",
  api_secret="Oce1_5nE1FQ9_dr6iz5D5_tp7-4",
  secure=True
)

def upload_encrypted_file(file_bytes, filename):
    try:
        result = cloudinary.uploader.upload(
            BytesIO(file_bytes),
            resource_type="raw",
            public_id=f"securefiles/{filename}",
            use_filename=True,
            unique_filename=False,
            overwrite=True
        )
        return result["secure_url"]
    except Exception as e:
        print("Cloudinary upload failed:", e)
        return None
