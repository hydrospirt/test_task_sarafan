def extract_media_path(input_string):
    parts = input_string.split('media/')
    if len(parts) > 1:
        return parts[-1]
    return None
