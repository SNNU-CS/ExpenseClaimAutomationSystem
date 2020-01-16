from time import time


def user_avatar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/avatar/<id>/<time>.<jpg/png>
    name = str(time()).split('.')[0]
    suffix = filename.split('.')[-1]
    return 'avatar/{0}/{1}.{2}'.format(instance.id, name, suffix)
