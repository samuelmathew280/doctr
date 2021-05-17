import os
from doctr.models.artefacts import FaceDetector
from doctr.documents import DocumentFile


def test_face_detector(mock_image_folder):
    detector = FaceDetector(n_faces=1)
    for img in os.listdir(mock_image_folder):
        image = DocumentFile.from_images(os.path.join(mock_image_folder, img))[0]
        faces = detector(image)
        assert len(faces) <= 1