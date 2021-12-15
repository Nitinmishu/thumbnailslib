import os.path
import uuid

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.validators import FileExtensionValidator
from django.db import models


def get_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename


class Photo(models.Model):
    photo = models.ImageField(null=True, upload_to=get_file_name,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    thumbnail = models.ImageField(null=True, upload_to=get_file_name, editable=False)

    def save(self, *args, **kwargs):

        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(Photo, self).save(*args, **kwargs)

    def make_thumbnail(self):
        thumb_size = 250, 250
        image = Image.open(self.photo)
        image.thumbnail(thumb_size, Image.ANTIALIAS)

        thumbnail_name, thumbnail_extension = os.path.splitext(self.photo.name)
        thumbnail_extension = thumbnail_extension.lower()

        thumbnail_filename = thumbnail_name + '_thumbnail' + thumbnail_extension

        if thumbnail_extension in ['.jpg', '.jpeg']:
            file_type = 'JPEG'
        elif thumbnail_extension == '.png':
            file_type = 'PNG'
        else:
            return False  # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temporary_thumbnail = BytesIO()
        image.save(temporary_thumbnail, file_type)
        temporary_thumbnail.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumbnail_filename, ContentFile(temporary_thumbnail.read()), save=False)
        temporary_thumbnail.close()

        return True

    class Meta:
        abstract = True
