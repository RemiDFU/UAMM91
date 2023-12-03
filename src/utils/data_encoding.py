from sklearn.preprocessing import LabelEncoder

def encode_information_level(data):
    label_encoder = LabelEncoder()
    encoded_data = label_encoder.fit_transform(data)
    return encoded_data
